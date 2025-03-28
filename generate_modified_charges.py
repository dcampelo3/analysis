# Check for required packages at the start of the script
try:
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import StandardScaler
    from tqdm import tqdm
except ImportError as e:
    print("Missing required packages. Please run the following command to install them:")
    print("pip install pandas numpy scikit-learn tqdm")
    exit(1)

import logging
from datetime import datetime
import os

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'charge_modification_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)

def add_random_factors(df, n_factors=3):
    """Add random error factors for additional variation"""
    for i in range(n_factors):
        df[f'random_factor_{i}'] = np.random.normal(0, 1, size=len(df))
    return df

def count_rows(file_path, chunk_size=100000):
    """Count total rows in CSV file"""
    print("Counting total rows (this may take a moment)...")
    total_rows = 0
    for chunk in pd.read_csv(file_path, chunksize=chunk_size, usecols=[0]):
        total_rows += len(chunk)
    return total_rows

def generate_modified_charges(input_file, output_file):
    """
    Generate modified total charges using multiple linear regression
    with controlled variation between 15-55% of original amounts
    """
    try:
        print("Starting to read the input file...")
        logging.info(f"Reading input file: {input_file}")
        
        # Get total rows for progress bar
        total_rows = count_rows(input_file)
        print(f"Total rows to process: {total_rows:,}")
        
        # Process in chunks with progress bar
        chunks = []
        chunk_size = 100000
        
        with tqdm(total=total_rows, desc="Reading data", unit="rows") as pbar:
            for chunk in pd.read_csv(input_file, chunksize=chunk_size, low_memory=False):
                chunks.append(chunk)
                pbar.update(len(chunk))
        
        print("Combining chunks...")
        df = pd.concat(chunks, ignore_index=True)
        print(f"Successfully read {len(df):,} rows")
        
        print("Processing data...")
        features = ['LOS', 'APRDRG', 'PAY1']
        
        with tqdm(total=4, desc="Converting columns") as pbar:
            df['LOS'] = pd.to_numeric(df['LOS'], errors='coerce')
            pbar.update(1)
            df['APRDRG'] = pd.to_numeric(df['APRDRG'], errors='coerce')
            pbar.update(1)
            df['PAY1'] = pd.to_numeric(df['PAY1'], errors='coerce')
            pbar.update(1)
            df['TOTCHG'] = pd.to_numeric(df['TOTCHG'], errors='coerce')
            pbar.update(1)
        
        print("Handling missing values...")
        df = df.dropna(subset=['TOTCHG', 'LOS', 'APRDRG', 'PAY1'])
        print(f"Rows after dropping missing values: {len(df):,}")
        
        print("Adding random factors...")
        df = add_random_factors(df)
        features.extend([f'random_factor_{i}' for i in range(3)])
        
        print("Preparing model...")
        X = df[features]
        y = df['TOTCHG']
        
        print("Scaling features...")
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        print("Fitting regression model...")
        model = LinearRegression()
        model.fit(X_scaled, y)
        
        print("Generating predictions...")
        predicted_charges = model.predict(X_scaled)
        
        print("Calculating modified charges...")
        variation_factors = np.random.uniform(0.15, 0.55, size=len(df))
        variation_direction = np.random.choice([-1, 1], size=len(df))
        modified_charges = df['TOTCHG'] * (1 + variation_factors * variation_direction)
        
        print("Preparing output dataframe...")
        output_df = df.copy()
        output_df['TOTCHG_ORIGINAL'] = df['TOTCHG']
        output_df['TOTCHG_MODIFIED'] = modified_charges
        output_df['MODIFICATION_PCT'] = ((modified_charges - df['TOTCHG']) / df['TOTCHG'] * 100).round(2)
        
        # Remove temporary random factors
        for i in range(3):
            output_df = output_df.drop(f'random_factor_{i}', axis=1)
        
        print("Saving results...")
        output_df.to_csv(output_file, index=False)
        
        # Log summary statistics
        print("\nSummary Statistics:")
        print(f"Total records processed: {len(output_df):,}")
        print(f"Average modification: {output_df['MODIFICATION_PCT'].mean():.2f}%")
        print(f"Modification range: {output_df['MODIFICATION_PCT'].min():.2f}% to {output_df['MODIFICATION_PCT'].max():.2f}%")
        
        return True
        
    except Exception as e:
        logging.error(f"Error generating modified charges: {str(e)}", exc_info=True)
        print(f"Error: {str(e)}")
        return False

def main():
    # Use the specific processed file
    input_file = r"C:\analysis\data\NRD_2019\processed\NRD_2019_Core_processed.csv"
    output_file = r"C:\analysis\data\NRD_2019\processed\NRD_2019_Modified_Charges.csv"
    
    logging.info("Starting charge modification process")
    logging.info(f"Input file: {input_file}")
    logging.info(f"Output file: {output_file}")
    
    # Generate modified charges from the processed file
    success = generate_modified_charges(input_file, output_file)
    
    if success:
        logging.info("Charge modification completed successfully")
        logging.info(f"Modified charges saved to: {output_file}")
    else:
        logging.error("Charge modification process failed")

if __name__ == "__main__":
    main() 