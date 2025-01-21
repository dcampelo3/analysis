import pandas as pd
import csv
from tempfile import NamedTemporaryFile
import shutil
import os
from tqdm import tqdm
import time

def get_existing_columns(filename):
    """Get list of existing column names from CSV file"""
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, [])
        return headers

def add_columns_to_csv(input_file, new_column_names, chunk_size=1000):
    """
    Add new columns to existing CSV file, skipping any duplicate column names.
    """
    try:
        # Get existing column names
        existing_headers = get_existing_columns(input_file)
        print(f"\nExisting columns: {len(existing_headers)}")
       
        # Check for duplicates and filter them out
        columns_to_add = []
        skipped_columns = []
        for col in new_column_names:
            if col in existing_headers:
                skipped_columns.append(col)
            else:
                columns_to_add.append(col)
       
        # Print duplicate information
        if skipped_columns:
            print("\nSkipping these columns as they already exist:")
            for col in skipped_columns:
                print(f"- {col}")
       
        if not columns_to_add:
            print("\nNo new columns to add. All specified columns already exist.")
            return
       
        print(f"\nWill add these new columns: {columns_to_add}")
       
        # Create backup
        backup_file = input_file + '.backup'
        print(f"\nCreating backup at {backup_file}")
        shutil.copy2(input_file, backup_file)
       
        # Show initial preview
        print("\nInitial first 5 rows:")
        df_initial = pd.read_csv(input_file, nrows=5)
        print(df_initial)
       
        # Count total rows for progress bar
        print("\nCounting total rows...")
        total_rows = sum(1 for _ in open(input_file)) - 1
        print(f"Total rows to process: {total_rows:,}")
       
        # Create temporary file
        temp_file = NamedTemporaryFile(mode='w', delete=False, newline='')
        start_time = time.time()
       
        try:
            with open(input_file, 'r', newline='') as csvfile, temp_file:
                reader = csv.reader(csvfile)
                writer = csv.writer(temp_file)
               
                # Write headers
                headers = next(reader)
                new_headers = headers + columns_to_add
                writer.writerow(new_headers)
               
                # Process rows with progress bar
                empty_values = [''] * len(columns_to_add)
                rows_processed = 0
               
                with tqdm(total=total_rows, desc="Processing rows") as pbar:
                    for row in reader:
                        writer.writerow(row + empty_values)
                        rows_processed += 1
                       
                        if rows_processed % chunk_size == 0:
                            pbar.update(chunk_size)
                            elapsed_time = time.time() - start_time
                            rows_per_second = rows_processed / elapsed_time
                            pbar.set_postfix({
                                'Speed': f'{rows_per_second:.0f} rows/s',
                                'Elapsed': f'{elapsed_time:.1f}s'
                            })
                   
                    pbar.update(total_rows - rows_processed)
           
            # Replace original file
            print("\nReplacing original file with updated version...")
            shutil.move(temp_file.name, input_file)
           
            # Show result preview
            print("\nAfter adding columns - first 5 rows:")
            df_after = pd.read_csv(input_file, nrows=5)
            print(df_after)
           
            # Display summary
            end_time = time.time()
            total_time = end_time - start_time
            print(f"\nSummary:")
            print(f"- Total rows processed: {rows_processed:,}")
            print(f"- Processing time: {total_time:.2f} seconds")
            print(f"- Average speed: {rows_processed/total_time:.0f} rows/second")
            print(f"- New columns added: {columns_to_add}")
            if skipped_columns:
                print(f"- Columns skipped (already existed): {skipped_columns}")
            print(f"- Backup created at: {backup_file}")
           
        except Exception as e:
            print(f"\nError during processing: {str(e)}")
            print("Restoring from backup...")
            shutil.copy2(backup_file, input_file)
            raise
           
        finally:
            if os.path.exists(temp_file.name):
                os.unlink(temp_file.name)
               
    except Exception as e:
        print(f"\nFatal error: {str(e)}")
        print("No changes were made to the original file.")
        raise

# Example usage
if __name__ == "__main__":
    input_file = "data/NRD_2019/NRD_2019_CORE.csv"  # Update with your correct path
    column_names = [
    'DISCWT', 'HOSPWT', 'HOSP_CONTROL', 'HOSP_ED', 'HOSP_REGION', 'HOSP_TRAUMA', 'HOSP_URCAT4',
    'HOSP_UR_TEACH', 'NEDS_STRATUM', 'N_DISC_U', 'N_HOSP_U', 'S_DISC_U', 'S_HOSP_U', 'TOTAL_EDVisits', 'YEAR'
]
   
    try:
        add_columns_to_csv(input_file, column_names)
    except Exception as e:
        print(f"Program terminated with error: {str(e)}")