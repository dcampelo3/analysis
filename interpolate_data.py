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
        logging.FileHandler(f'interpolation_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

def get_file_size(file_path):
    """Get file size in GB"""
    return os.path.getsize(file_path) / (1024 * 1024 * 1024)

def count_rows(file_path, chunk_size=100000):
    """Count total rows in CSV file"""
    total_rows = 0
    for chunk in pd.read_csv(file_path, chunksize=chunk_size, usecols=[0]):
        total_rows += len(chunk)
    return total_rows

def handle_missing_values(df):
    """Handle missing values in the dataframe using interpolation"""
    # Interpolate numeric values and fill non-numeric with mode
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    non_numeric_columns = df.select_dtypes(exclude=['int64', 'float64']).columns
    
    # Process numeric columns
    for col in numeric_columns:
        df[col] = df[col].interpolate(method='linear', limit_direction='both')
        # Fill any remaining NaN at edges with forward/backward fill
        df[col] = df[col].fillna(method='ffill').fillna(method='bfill')
    
    # Process non-numeric columns
    for col in non_numeric_columns:
        # Calculate mode only once per column
        mode_value = df[col].mode()[0] if not df[col].mode().empty else 'Unknown'
        df[col] = df[col].fillna(mode_value)
    
    return df

def process_file(input_file, output_file):
    """Process a single CSV file with interpolation"""
    try:
        # Get file size and estimate total rows
        file_size = get_file_size(input_file)
        logging.info(f"\nProcessing {input_file} (Size: {file_size:.2f} GB)")
        
        # Determine optimal chunk size based on file size
        chunk_size = min(100000, max(10000, int(100000 * (2 / file_size))))
        
        # Count total rows for progress bar
        logging.info("Counting total rows...")
        total_rows = count_rows(input_file, chunk_size)
        logging.info(f"Total rows to process: {total_rows:,}")
        
        # Process in chunks with progress bar
        chunks = []
        processed_rows = 0
        
        with tqdm(total=total_rows, desc="Processing", unit="rows") as pbar:
            for chunk in pd.read_csv(input_file, chunksize=chunk_size):
                # Handle missing values
                chunk = handle_missing_values(chunk)
                chunks.append(chunk)
                
                processed_rows += len(chunk)
                pbar.update(len(chunk))
                
                # Periodically save and clear chunks to manage memory
                if len(chunks) * chunk_size > 1000000:  # Save every million rows
                    interim_df = pd.concat(chunks, ignore_index=True)
                    if processed_rows == len(interim_df):  # First batch
                        interim_df.to_csv(output_file, index=False, mode='w')
                    else:
                        interim_df.to_csv(output_file, index=False, mode='a', header=False)
                    chunks = []  # Clear chunks from memory
        
        # Save any remaining chunks
        if chunks:
            interim_df = pd.concat(chunks, ignore_index=True)
            if processed_rows == len(interim_df):
                interim_df.to_csv(output_file, index=False, mode='w')
            else:
                interim_df.to_csv(output_file, index=False, mode='a', header=False)
        
        # Verify and log results
        final_size = get_file_size(output_file)
        logging.info(f"\nProcessed file saved to: {output_file}")
        logging.info(f"Original size: {file_size:.2f} GB")
        logging.info(f"Processed size: {final_size:.2f} GB")
        logging.info(f"Total rows processed: {processed_rows:,}")
        
        return True
        
    except Exception as e:
        logging.error(f"Error processing {input_file}: {str(e)}", exc_info=True)
        return False

def main():
    # Specific file path
    input_file = r"C:\analysis\data\KID_2019\KID_2019_Severity.csv"
    
    # Create processed data directory
    processed_dir = 'processed_data/KID_2019'
    os.makedirs(processed_dir, exist_ok=True)
    
    # Define output file path
    output_file = os.path.join(processed_dir, 'processed_KID_2019_SEVERITY.csv')
    
    if os.path.exists(input_file):
        logging.info(f"Processing file: {input_file}")
        process_file(input_file, output_file)
    else:
        logging.error(f"Input file not found: {input_file}")

if __name__ == "__main__":
    main() 