import pandas as pd
import os
from tqdm import tqdm
import sys
import logging
from datetime import datetime
import gc  # For garbage collection

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

def get_row_count(file_path, chunk_size=10000):
    """Get total number of rows in a CSV file"""
    total_rows = 0
    for chunk in pd.read_csv(file_path, chunksize=chunk_size, usecols=[0]):
        total_rows += len(chunk)
    return total_rows

def merge_and_save_chunks(file_paths, output_file, chunk_size=10000):
    """Merge files chunk by chunk and save directly to output"""
    try:
        # Get total rows from first file (assuming it's one of the main files)
        logging.info("Counting total rows...")
        total_rows = get_row_count(file_paths[0])
        logging.info(f"Total rows to process: {total_rows:,}")

        # Initialize progress bar
        with tqdm(total=total_rows, desc="Merging", unit="rows") as pbar:
            # Initialize file readers
            readers = [pd.read_csv(f, chunksize=chunk_size, low_memory=False) for f in file_paths]
            first_chunk = True

            while True:
                try:
                    # Read chunks from all files
                    chunks = []
                    for i, reader in enumerate(readers):
                        try:
                            chunk = next(reader)
                            chunks.append(chunk)
                        except StopIteration:
                            # If a file is shorter, reset its reader
                            readers[i] = pd.read_csv(file_paths[i], chunksize=chunk_size, low_memory=False)
                            chunk = next(readers[i])
                            chunks.append(chunk)

                    # Merge chunks
                    merged_chunk = pd.concat(chunks, axis=1)

                    # Save merged chunk
                    if first_chunk:
                        merged_chunk.to_csv(output_file, index=False, mode='w')
                        first_chunk = False
                    else:
                        merged_chunk.to_csv(output_file, index=False, mode='a', header=False)

                    # Update progress
                    pbar.update(len(merged_chunk))

                    # Clear memory
                    del chunks
                    del merged_chunk
                    gc.collect()

                except StopIteration:
                    break

        return True

    except Exception as e:
        logging.error(f"Error during merge: {str(e)}", exc_info=True)
        return False

def main():
    processed_dir = 'processed_data'
    output_file = 'combined_data.csv'
    chunk_size = 10000  # Smaller chunk size for better memory management

    # Get all processed CSV files
    all_files = []
    for root, dirs, files in os.walk(processed_dir):
        for file in files:
            if file.startswith('processed_') and file.endswith('.CSV'):
                all_files.append(os.path.join(root, file))

    if not all_files:
        logging.error("No processed CSV files found!")
        return

    logging.info("Found the following files:")
    for file in all_files:
        logging.info(f"- {file}")

    # Sort files so larger files come first
    all_files.sort(key=lambda x: os.path.getsize(x), reverse=True)

    logging.info("\nStarting merge operation...")
    success = merge_and_save_chunks(all_files, output_file, chunk_size)

    if success:
        final_size = os.path.getsize(output_file) / (1024 * 1024 * 1024)  # Size in GB
        logging.info(f"\nMerge completed successfully!")
        logging.info(f"Combined data saved to: {output_file}")
        logging.info(f"Final file size: {final_size:.2f} GB")
    else:
        logging.error("Merge operation failed!")

if __name__ == "__main__":
    main() 