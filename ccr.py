import pandas as pd
import numpy as np

def analyze_ccr_data():
    try:
        # Read the hospital file
        df = pd.read_csv('data/NIS_2019/NIS_2019_HOSPITAL.CSV')
        
        print("\n=== Hospital Data Analysis ===")
        
        # Convert columns to numeric where possible
        numeric_columns = ['HOSP_BEDSIZE', 'H_CONTRL', 'HOSP_URCAT4', 'HOSP_UR_TEACH', 
                         'N_DISC_U', 'N_HOSP_U', 'S_DISC_U', 'S_HOSP_U', 'TOTAL_DISC']
        
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Hospital Size Analysis
        print("\n1. Hospital Size Distribution:")
        size_mapping = {1: 'Small', 2: 'Medium', 3: 'Large'}
        df['HOSP_BEDSIZE'] = df['HOSP_BEDSIZE'].map(size_mapping)
        print(df['HOSP_BEDSIZE'].value_counts())
        
        # Hospital Control Analysis
        print("\n2. Hospital Control/Ownership:")
        control_mapping = {1: 'Government', 2: 'Private, non-profit', 3: 'Private, invest-own'}
        df['H_CONTRL'] = df['H_CONTRL'].map(control_mapping)
        print(df['H_CONTRL'].value_counts())
        
        # Urban/Rural Status
        print("\n3. Urban/Rural Status:")
        location_mapping = {
            1: 'Large metropolitan areas',
            2: 'Small metropolitan areas',
            3: 'Micropolitan areas',
            4: 'Non-urban residual'
        }
        df['HOSP_URCAT4'] = df['HOSP_URCAT4'].map(location_mapping)
        print(df['HOSP_URCAT4'].value_counts())
        
        # Teaching Status
        print("\n4. Teaching Status:")
        teaching_mapping = {0: 'Non-teaching', 1: 'Teaching'}
        df['HOSP_UR_TEACH'] = df['HOSP_UR_TEACH'].map(teaching_mapping)
        print(df['HOSP_UR_TEACH'].value_counts())
        
        # Hospital Volume Analysis
        print("\n5. Hospital Volume Statistics:")
        volume_stats = df[['N_DISC_U', 'TOTAL_DISC']].describe()
        print(volume_stats)
        
        # Save detailed summary to CSV
        summary_df = pd.DataFrame({
            'Hospital_Size': df['HOSP_BEDSIZE'].value_counts(),
            'Control_Type': df['H_CONTRL'].value_counts(),
            'Location': df['HOSP_URCAT4'].value_counts(),
            'Teaching_Status': df['HOSP_UR_TEACH'].value_counts()
        })
        summary_df.to_csv('hospital_characteristics_summary.csv')
        print("\nDetailed summary saved to hospital_characteristics_summary.csv")
        
    except FileNotFoundError:
        print("Error: Hospital file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    analyze_ccr_data()