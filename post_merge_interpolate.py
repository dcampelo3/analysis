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
        logging.FileHandler(f'post_merge_interpolation_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
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

def analyze_columns(df):
    """Analyze columns and their missing value patterns"""
    missing_stats = df.isnull().sum()
    total_rows = len(df)
    
    logging.info("\nColumn Analysis:")
    for col in df.columns:
        missing_count = missing_stats[col]
        if missing_count > 0:
            missing_percentage = (missing_count / total_rows) * 100
            logging.info(f"Column '{col}': {missing_count:,} missing values ({missing_percentage:.2f}%)")
    
    return missing_stats

def handle_missing_values(df, dataset_patterns=None):
    """Handle missing values in the dataframe using advanced interpolation
    
    Args:
        df: pandas DataFrame
        dataset_patterns: dict of column prefixes and their specific handling methods
    """
    # Separate numeric and non-numeric columns
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    non_numeric_columns = df.select_dtypes(exclude=['int64', 'float64']).columns
    
    # Process numeric columns
    for col in numeric_columns:
        # Check if column belongs to a specific dataset
        prefix = col.split('_')[0] if '_' in col else ''
        
        if dataset_patterns and prefix in dataset_patterns:
            # Apply dataset-specific handling
            method = dataset_patterns[prefix].get('numeric_method', 'linear')
            if method == 'linear':
                df[col] = df[col].interpolate(method='linear', limit_direction='both')
            elif method == 'time':
                df[col] = df[col].interpolate(method='time', limit_direction='both')
            elif method == 'polynomial':
                df[col] = df[col].interpolate(method='polynomial', order=2, limit_direction='both')
        else:
            # Default handling
            df[col] = df[col].interpolate(method='linear', limit_direction='both')
        
        # Fill any remaining NaN at edges
        df[col] = df[col].fillna(method='ffill').fillna(method='bfill')
    
    # Process non-numeric columns
    for col in non_numeric_columns:
        prefix = col.split('_')[0] if '_' in col else ''
        
        if dataset_patterns and prefix in dataset_patterns:
            # Apply dataset-specific handling
            method = dataset_patterns[prefix].get('categorical_method', 'mode')
            if method == 'mode':
                mode_value = df[col].mode()[0] if not df[col].mode().empty else 'Unknown'
                df[col] = df[col].fillna(mode_value)
            elif method == 'forward':
                df[col] = df[col].fillna(method='ffill').fillna(method='bfill')
        else:
            # Default to mode for categorical columns
            mode_value = df[col].mode()[0] if not df[col].mode().empty else 'Unknown'
            df[col] = df[col].fillna(mode_value)
    
    return df

def process_merged_file(input_file, output_file):
    """Process the merged CSV file with interpolation"""
    try:
        # Get file size and estimate total rows
        file_size = get_file_size(input_file)
        logging.info(f"\nProcessing merged file: {input_file} (Size: {file_size:.2f} GB)")
        
        # Determine optimal chunk size based on file size
        chunk_size = min(100000, max(10000, int(100000 * (2 / file_size))))
        
        # Count total rows
        logging.info("Counting total rows...")
        total_rows = count_rows(input_file, chunk_size)
        logging.info(f"Total rows to process: {total_rows:,}")
        
        # Define dataset-specific patterns
        dataset_patterns = {
            'NRD': {'numeric_method': 'linear', 'categorical_method': 'mode'},
            'NIS': {'numeric_method': 'linear', 'categorical_method': 'mode'},
            'KID': {'numeric_method': 'linear', 'categorical_method': 'mode'},
            'NEDS': {'numeric_method': 'linear', 'categorical_method': 'mode'}
        }
        
        # Process in chunks
        chunks = []
        processed_rows = 0
        first_chunk = True
        
        with tqdm(total=total_rows, desc="Processing", unit="rows") as pbar:
            for chunk in pd.read_csv(input_file, chunksize=chunk_size):
                if first_chunk:
                    # Analyze first chunk to understand column patterns
                    logging.info("\nAnalyzing data patterns in first chunk...")
                    analyze_columns(chunk)
                    first_chunk = False
                
                # Handle missing values
                chunk = handle_missing_values(chunk, dataset_patterns)
                chunks.append(chunk)
                
                processed_rows += len(chunk)
                pbar.update(len(chunk))
                
                # Periodically save and clear chunks
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
        
        # Verify results
        final_size = get_file_size(output_file)
        logging.info(f"\nPost-merge interpolation completed!")
        logging.info(f"Original size: {file_size:.2f} GB")
        logging.info(f"Final size: {final_size:.2f} GB")
        logging.info(f"Total rows processed: {processed_rows:,}")
        
        return True
        
    except Exception as e:
        logging.error(f"Error processing merged file: {str(e)}", exc_info=True)
        return False

def main():
    input_file = 'combined_data.csv'
    output_file = 'final_interpolated_data.csv'
    
    if not os.path.exists(input_file):
        logging.error(f"Merged file not found: {input_file}")
        logging.error("Please run merge_data.py first.")
        return
    
    logging.info("Starting post-merge interpolation...")
    success = process_merged_file(input_file, output_file)
    
    if success:
        logging.info(f"\nInterpolation completed successfully!")
        logging.info(f"Final dataset saved to: {output_file}")
    else:
        logging.error("Interpolation failed. Check the logs for details.")

if __name__ == "__main__":
    main() 