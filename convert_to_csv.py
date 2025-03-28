import csv

def convert_nis_columns_to_csv():
    # Create header row for CSV
    headers = ['Column_Name', 'Start_Position', 'End_Position', 'Length', 'Type', 'Description']
    
    # Open new CSV file for writing
    with open('NIS_Columns.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write headers
        writer.writerow(headers)
        
        # Core file columns
        core_data = [
            ['AGE', '1', '3', '3', 'Num', 'Age in years at admission'],
            ['AGE_NEONATE', '4', '5', '2', 'Num', 'Neonatal age indicator'],
            ['AMONTH', '6', '7', '2', 'Num', 'Admission month'],
            ['AWEEKEND', '8', '9', '2', 'Num', 'Admission day is a weekend'],
            ['DIED', '10', '11', '2', 'Num', 'Died during hospitalization'],
            ['DISCWT', '12', '22', '11', 'Num', 'NIS discharge weight'],
            ['DISPUNIFORM', '23', '24', '2', 'Num', 'Disposition of patient (uniform)'],
            ['DQTR', '25', '26', '2', 'Num', 'Discharge quarter'],
            ['DRG', '27', '29', '3', 'Num', 'DRG in effect on discharge date'],
            ['DRGVER', '30', '31', '2', 'Num', 'DRG grouper version used on discharge date'],
            ['DRG_NoPOA', '32', '34', '3', 'Num', 'DRG without POA'],
            ['APRDRG', '35', '37', '3', 'Num', 'All Patient Refined DRG'],
            ['APRDRG_Risk_Mortality', '38', '39', '2', 'Num', 'All Patient Refined DRG: Risk of Mortality Subclass'],
            ['APRDRG_Severity', '40', '41', '2', 'Num', 'All Patient Refined DRG: Severity of Illness Subclass'],
            ['HOSP_DIVISION', '42', '43', '2', 'Num', 'Census Division of hospital'],
            ['HOSP_NIS', '44', '48', '5', 'Num', 'NIS hospital number'],
            ['LOS', '531', '535', '5', 'Num', 'Length of stay (cleaned)'],
            ['TOTCHG', '628', '637', '10', 'Num', 'Total charges (cleaned)'],
            ['YEAR', '642', '645', '4', 'Num', 'Calendar year']
        ]
        
        # Hospital file columns
        hospital_data = [
            ['HOSP_BEDSIZE', '12', '13', '2', 'Num', 'Bed size of hospital'],
            ['HOSP_LOCTEACH', '16', '17', '2', 'Num', 'Location/teaching status of hospital'],
            ['HOSP_REGION', '23', '24', '2', 'Num', 'Region of hospital'],
            ['H_CONTRL', '25', '26', '2', 'Num', 'Control/ownership of hospital'],
            ['TOTAL_DISC', '55', '60', '6', 'Num', 'Total number of discharges']
        ]
        
        # DX_PR_GRPS file columns (adding relevant DRG-related columns)
        dx_pr_grps_data = [
            ['CMR_VERSION', '16', '21', '6', 'Char', 'Version of Elixhauser Comorbidity Software'],
            ['PCLASS_VERSION', '137', '142', '6', 'Char', 'Version of ICD-10-PCS Procedure class'],
            ['DXCCSR_Default_DX1', '143', '148', '6', 'Char', 'Default CCSR for principal diagnosis']
        ]
        
        # Write all data rows
        writer.writerows(core_data)
        writer.writerows(hospital_data)
        writer.writerows(dx_pr_grps_data)

if __name__ == "__main__":
    convert_nis_columns_to_csv() 