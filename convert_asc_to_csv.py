import os
import pandas as pd
import sys
from tqdm import tqdm

def get_delimiter(file_path, chunk_size=1024):
    """Detect the delimiter by reading the first chunk of the file"""
    with open(file_path, 'r') as f:
        first_line = f.readline()
        
    # Try common delimiters and count their occurrences
    delimiters = [',', '\t', '|']
    counts = {d: first_line.count(d) for d in delimiters}
    most_common = max(counts.items(), key=lambda x: x[1])
    
    return most_common[0] if most_common[1] > 0 else None

def convert_asc_to_csv():
    # Path to KID_2019 folder using absolute path
    kid_folder = r'C:\analysis\data\KID_2019'
    
    # Check if folder exists
    if not os.path.exists(kid_folder):
        print(f"Error: {kid_folder} directory not found")
        return
    
    # Get all .ASC files in the directory
    asc_files = [f for f in os.listdir(kid_folder) if f.endswith('.ASC')]
    
    if not asc_files:
        print(f"No .ASC files found in {kid_folder}")
        # List all files in directory to help debug
        print("\nFiles found in directory:")
        for file in os.listdir(kid_folder):
            print(f"- {file}")
        return
    
    for asc_file in asc_files:
        asc_path = os.path.join(kid_folder, asc_file)
        csv_filename = os.path.splitext(asc_file)[0] + '.csv'
        csv_path = os.path.join(kid_folder, csv_filename)
        
        try:
            # Get file size for progress bar
            file_size = os.path.getsize(asc_path)
            chunk_size = 100000  # Adjust chunk size based on your memory constraints
            
            # Detect delimiter
            delimiter = get_delimiter(asc_path)
            if not delimiter:
                print(f"Could not detect delimiter for {asc_file}")
                continue
                
            print(f"\nProcessing {asc_file} with delimiter '{delimiter}'")
            
            # Read and process the file in chunks
            chunks = pd.read_csv(
                asc_path,
                delimiter=delimiter,
                chunksize=chunk_size,
                low_memory=False,
                on_bad_lines='warn'
            )
            
            # Process first chunk to get headers
            first_chunk = True
            total_rows = 0
            
            with tqdm(total=file_size, unit='B', unit_scale=True, desc="Converting") as pbar:
                for chunk in chunks:
                    if first_chunk:
                        # Write header for the first chunk
                        chunk.to_csv(csv_path, index=False, mode='w')
                        first_chunk = False
                    else:
                        # Append without header for subsequent chunks
                        chunk.to_csv(csv_path, index=False, mode='a', header=False)
                    
                    total_rows += len(chunk)
                    pbar.update(chunk.memory_usage(deep=True).sum())
            
            print(f"Successfully converted {asc_file} to {csv_filename}")
            print(f"Total rows processed: {total_rows:,}")
            
        except Exception as e:
            print(f"Error converting {asc_file}: {str(e)}")
            # Remove partially created CSV file if conversion failed
            if os.path.exists(csv_path):
                os.remove(csv_path)

if __name__ == "__main__":
    convert_asc_to_csv() 