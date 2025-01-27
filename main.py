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
        # Read first row as data since it doesn't have headers
        data_row = next(reader, [])
        return []  # Return empty list since there are no headers

def add_columns_to_csv(input_file, new_column_names, chunk_size=1000):
    """
    Add new columns to existing CSV file, skipping any duplicate column names.
    """
    try:
        # Create backup first
        backup_file = input_file + '.backup'
        print(f"\nCreating backup at {backup_file}")
        shutil.copy2(input_file, backup_file)
        print(f"Backup created successfully at: {backup_file}")
       
        # Create temporary file
        temp_file = NamedTemporaryFile(mode='w', delete=False, newline='')
        start_time = time.time()
       
        try:
            with open(input_file, 'r', newline='') as csvfile, temp_file:
                reader = csv.reader(csvfile)
                writer = csv.writer(temp_file)
               
                # Write header row first
                writer.writerow(new_column_names)
                
                # Process all rows
                rows_processed = 0
                total_rows = sum(1 for _ in open(input_file))
               
                with tqdm(total=total_rows, desc="Processing rows") as pbar:
                    for row in reader:
                        # Keep original data, pad with empty strings if needed
                        new_row = row[:len(new_column_names)]
                        if len(new_row) < len(new_column_names):
                            new_row.extend([''] * (len(new_column_names) - len(new_row)))
                        writer.writerow(new_row)
                        rows_processed += 1
                       
                        if rows_processed % chunk_size == 0:
                            pbar.update(chunk_size)
           
            # Replace original file
            shutil.move(temp_file.name, input_file)
           
            print("\nFile updated successfully with new column headers")
           
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
    # Option 1: Use forward slashes
    
    input_file = "data/NRD_2019/NRD_2019_Severity.CSV"
    #input_file ="data/NRD_2019/NRD_2019_Hospital.CSV"
    #input_file ="data/NRD_2019/NRD_2019_Severity.CSV"
    #input_file ="data/NRD_2019/NRD_2019_DX_PR_GRPS.CSV" ##This file is too large to move from D drive to C drive 
    #input_file = "data/NEDS_2019/NEDS_2019_CORE.csv"
    #input_file = "data/NEDS_2019/NEDS_2019_DX_PR.csv"  
    #input_file = "data/NEDS_2019/NEDS_2019_ED.csv"
    #input_file = "data/NEDS_2019/NEDS_2019_HOSPITAL.csv"
    #input_file = "data/NEDS_2019/NEDS_2019_IP.csv"
    ## KID_2019 and NIS_2019 folders only seem to have ASC file. Not sure if this is correct.   

    
    # OR Option 2: Use double backslashes
    # input_file = "data\\NRD_2019\\NRD_2019_CORE\\NRD_2019_Core.CSV"
    
    # OR Option 3: Use raw string with 'r' prefix
    # input_file = r"data\NRD_2019\NRD_2019_CORE\NRD_2019_Core.CSV"

    column_names = [
        'KEY_NRD',           # HCUP record identifier
        'HOSP_NRD',          # NRD hospital identifier
        'APRDRG',            # All Patient Refined DRG
        'APRDRG_Risk_Mortality',  # All Patient Refined DRG: Risk of Mortality Subclass
        'APRDRG_Severity',   # All Patient Refined DRG: Severity of Illness Subclass
        'CM_AIDS',           # AHRQ comorbidity measure: Acquired immune deficiency syndrome
        'CM_ALCOHOL',        # AHRQ comorbidity measure: Alcohol abuse
        'CM_ANEMDEF',        # AHRQ comorbidity measure: Deficiency anemias
        'CM_ARTH',           # AHRQ comorbidity measure: Rheumatoid arthritis/collagen vascular diseases
        'CM_BLDLOSS',        # AHRQ comorbidity measure: Chronic blood loss anemia
        'CM_CHF',            # AHRQ comorbidity measure: Congestive heart failure
        'CM_CHRNLUNG',       # AHRQ comorbidity measure: Chronic pulmonary disease
        'CM_COAG',           # AHRQ comorbidity measure: Coagulopathy
        'CM_DEPRESS',        # AHRQ comorbidity measure: Depression
        'CM_DM',             # AHRQ comorbidity measure: Diabetes, uncomplicated
        'CM_DMCX',           # AHRQ comorbidity measure: Diabetes with chronic complications
        'CM_DRUG',           # AHRQ comorbidity measure: Drug abuse
        'CM_HTN_C',          # AHRQ comorbidity measure: Hypertension
        'CM_HYPOTHY',        # AHRQ comorbidity measure: Hypothyroidism
        'CM_LIVER',          # AHRQ comorbidity measure: Liver disease
        'CM_LYMPH',          # AHRQ comorbidity measure: Lymphoma
        'CM_LYTES',          # AHRQ comorbidity measure: Fluid and electrolyte disorders
        'CM_METS',           # AHRQ comorbidity measure: Metastatic cancer
        'CM_NEURO',          # AHRQ comorbidity measure: Other neurological disorders
        'CM_OBESE',          # AHRQ comorbidity measure: Obesity
        'CM_PARA',           # AHRQ comorbidity measure: Paralysis
        'CM_PERIVASC',       # AHRQ comorbidity measure: Peripheral vascular disorders
        'CM_PSYCH',          # AHRQ comorbidity measure: Psychoses
        'CM_PULMCIRC',       # AHRQ comorbidity measure: Pulmonary circulation disorders
        'CM_RENLFAIL',       # AHRQ comorbidity measure: Renal failure
        'CM_TUMOR',          # AHRQ comorbidity measure: Solid tumor without metastasis
        'CM_ULCER',          # AHRQ comorbidity measure: Peptic ulcer disease excluding bleeding
        'CM_VALVE',          # AHRQ comorbidity measure: Valvular disease
        'CM_WGHTLOSS',       # AHRQ comorbidity measure: Weight loss
        'HOSP_DIVISION',     # Census Division of hospital
]
   
    try:
        add_columns_to_csv(input_file, column_names)
    except Exception as e:
        print(f"Program terminated with error: {str(e)}")