import pandas as pd
import os
from tqdm import tqdm
import sys
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'merge_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

def get_file_size(file_path):
    """Get file size in GB"""
    return os.path.getsize(file_path) / (1024 * 1024 * 1024)

def add_prefix_to_columns(df, prefix):
    """Add prefix to column names"""
    return df.add_prefix(f"{prefix}_")

def read_csv_with_prefix(file_path, prefix):
    """Read CSV file and add prefix to columns"""
    try:
        # Get file size
        file_size = get_file_size(file_path)
        logging.info(f"\nReading {file_path} (Size: {file_size:.2f} GB)")
        
        # Determine optimal chunk size based on file size
        chunk_size = min(100000, max(10000, int(100000 * (2 / file_size))))
        
        # Count total rows for progress bar
        total_rows = sum(1 for _ in pd.read_csv(file_path, chunksize=chunk_size))
        total_rows *= chunk_size
        
        chunks = []
        processed_rows = 0
        
        with tqdm(total=total_rows, desc="Reading", unit="rows") as pbar:
            for chunk in pd.read_csv(file_path, chunksize=chunk_size):
                # Add prefix to columns
                chunk = add_prefix_to_columns(chunk, prefix)
                chunks.append(chunk)
                
                processed_rows += len(chunk)
                pbar.update(len(chunk))
                
                # Periodically concat and clear chunks to manage memory
                if len(chunks) * chunk_size > 1000000:  # Combine every million rows
                    chunks = [pd.concat(chunks, ignore_index=True)]
        
        final_df = pd.concat(chunks, ignore_index=True)
        logging.info(f"Successfully read {processed_rows:,} rows")
        return final_df
        
    except Exception as e:
        logging.error(f"Error reading {file_path}: {str(e)}", exc_info=True)
        raise

def get_processed_files(base_dir):
    """Get all processed CSV files"""
    csv_files = {}
    
    # Define dataset prefixes
    datasets = ['NRD', 'NIS', 'KID', 'NEDS']
    
    for dataset in datasets:
        dataset_dir = os.path.join(base_dir, f'{dataset}_2019')
        if os.path.exists(dataset_dir):
            for file in os.listdir(dataset_dir):
                if file.startswith('processed_') and file.endswith('.CSV'):
                    full_path = os.path.join(dataset_dir, file)
                    csv_files[full_path] = dataset
    
    return csv_files

def main():
    processed_dir = 'processed_data'
    file_mappings = get_processed_files(processed_dir)
    
    if not file_mappings:
        logging.warning("No processed CSV files found! Please run interpolate_data.py first.")
        return
    
    logging.info("Found the following processed files:")
    for file_path in file_mappings:
        logging.info(f"- {file_path}")
    
    all_dataframes = []
    row_counts = {}
    
    # Process each file
    for file_path, prefix in file_mappings.items():
        if os.path.exists(file_path):
            try:
                df = read_csv_with_prefix(file_path, prefix)
                row_counts[file_path] = len(df)
                all_dataframes.append(df)
            except Exception as e:
                logging.error(f"Error processing {file_path}: {str(e)}")
        else:
            logging.warning(f"File not found - {file_path}")
    
    # Combine all dataframes
    if all_dataframes:
        logging.info("\nMerging all dataframes...")
        try:
            # Print row count information
            logging.info("\nRow counts in each file:")
            for file_path, count in row_counts.items():
                logging.info(f"{file_path}: {count:,} rows")
            
            # Merge dataframes with progress indication
            logging.info("Performing merge operation...")
            final_df = pd.concat(all_dataframes, axis=1)
            
            # Save to CSV
            output_file = 'combined_data.csv'
            logging.info(f"Saving to {output_file}...")
            
            # Write to CSV in chunks with progress bar
            chunk_size = 100000
            total_chunks = len(final_df) // chunk_size + 1
            
            with tqdm(total=total_chunks, desc="Saving", unit="chunks") as pbar:
                for i in range(0, len(final_df), chunk_size):
                    chunk = final_df.iloc[i:i+chunk_size]
                    if i == 0:
                        chunk.to_csv(output_file, index=False, mode='w')
                    else:
                        chunk.to_csv(output_file, index=False, mode='a', header=False)
                    pbar.update(1)
            
            # Log final statistics
            final_size = get_file_size(output_file)
            logging.info(f"\nProcess completed successfully!")
            logging.info(f"Combined data saved to: {output_file}")
            logging.info(f"Final file size: {final_size:.2f} GB")
            logging.info(f"Total columns: {len(final_df.columns):,}")
            logging.info(f"Total rows: {len(final_df):,}")
            
        except Exception as e:
            logging.error(f"Error while merging or saving data: {str(e)}", exc_info=True)
    else:
        logging.warning("No data to process!")

if __name__ == "__main__":
    main() 