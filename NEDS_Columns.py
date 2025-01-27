# NEDS 2019 Column Specifications

# Core File Columns
core_columns = [
    'AGE',              # Age in years at admission
    'AWEEKEND',         # Admission on weekend
    'DIED_VISIT',       # Died in the ED/during the visit
    'DISCWT',           # Weight to ED visits in AHA universe
    'DISP_ED',          # Disposition from ED
    'DISP_IP',          # Disposition of patient from inpatient admission
    'DMONTH',           # Discharge month
    'DQTR',             # Discharge quarter
    'DX1',              # ICD-10-CM Diagnosis 1
    'DX2',              # ICD-10-CM Diagnosis 2
    'DX3',              # ICD-10-CM Diagnosis 3
    'DX4',              # ICD-10-CM Diagnosis 4
    'DX5',              # ICD-10-CM Diagnosis 5
    'DX6',              # ICD-10-CM Diagnosis 6
    'DX7',              # ICD-10-CM Diagnosis 7
    'DX8',              # ICD-10-CM Diagnosis 8
    'DX9',              # ICD-10-CM Diagnosis 9
    'DX10',             # ICD-10-CM Diagnosis 10
    'DX11',             # ICD-10-CM Diagnosis 11
    'DX12',             # ICD-10-CM Diagnosis 12
    'DX13',             # ICD-10-CM Diagnosis 13
    'DX14',             # ICD-10-CM Diagnosis 14
    'DX15',             # ICD-10-CM Diagnosis 15
    'DXCCS1',           # CCS: First-listed diagnosis
    'DXCCS2',           # CCS: Second-listed diagnosis
    'DXCCS3',           # CCS: Third-listed diagnosis
    'DXCCS4',           # CCS: Fourth-listed diagnosis
    'DXCCS5',           # CCS: Fifth-listed diagnosis
    'EDEVENT',          # Type of ED event
    'FEMALE',           # Indicator of sex
    'HCUPFILE',         # Source of HCUP record
    'HOSP_ED',          # HCUP ED hospital identifier
    'HOSP_REGION',      # Region of hospital
    'CPT1',             # CPT/HCPCS procedure code 1
    'CPT2',             # CPT/HCPCS procedure code 2
    'CPT3',             # CPT/HCPCS procedure code 3
    'CPT4',             # CPT/HCPCS procedure code 4
    'CPT5',             # CPT/HCPCS procedure code 5
    'CPT6',             # CPT/HCPCS procedure code 6
    'CPT7',             # CPT/HCPCS procedure code 7
    'CPT8',             # CPT/HCPCS procedure code 8
    'CPT9',             # CPT/HCPCS procedure code 9
    'CPT10',            # CPT/HCPCS procedure code 10
    'CPT11',            # CPT/HCPCS procedure code 11
    'CPT12',            # CPT/HCPCS procedure code 12
    'CPT13',            # CPT/HCPCS procedure code 13
    'CPT14',            # CPT/HCPCS procedure code 14
    'CPT15',            # CPT/HCPCS procedure code 15
    'CPTCCS1',          # CCS: CPT 1
    'CPTCCS2',          # CCS: CPT 2
    'CPTCCS3',          # CCS: CPT 3
    'CPTCCS4',          # CCS: CPT 4
    'CPTCCS5',          # CCS: CPT 5
    'KEY_ED',           # HCUP record identifier
    'NDX',              # Number of diagnoses on this record
    'NCPT',             # Number of CPT/HCPCS procedures on this record
    'PAY1',             # Primary expected payer
    'PAY2',             # Secondary expected payer
    'PL_NCHS',          # Patient Location: NCHS Urban-Rural Code
    'TOTCHG_ED',        # Total charges for ED services
    'YEAR',             # Calendar year
    'ZIPINC_QRTL',      # Median household income quartile for patient's ZIP Code
    'INJURY',           # General injury flag
    'INJURY_SEVERITY',  # Injury severity score
    'MULTINJURY',       # Multiple injury flag
    'INTENT_SELF_HARM', # Self-inflicted injury flag
    'INTENT_UNINTENTIONAL', # Unintentional injury flag
    'INTENT_ASSAULT',   # Assault injury flag
    'POINT_OF_ORIGIN_UNIF',  # Point of origin, uniform coding
    'PointOfOriginUB04',     # Point of origin, UB-04 coding
    'NEDS_STRATUM',     # Stratum used to post-stratify hospital
    'DX_Visit_Reason1', # Reason for visit diagnosis 1
    'DX_Visit_Reason2', # Reason for visit diagnosis 2
    'DX_Visit_Reason3', # Reason for visit diagnosis 3
    'NEDS_YEAR',        # Year for NEDS
    'NEDS_WEIGHT',      # Weight to NEDS discharges
    'I10_NDX',          # Number of ICD-10-CM diagnoses
    'I10_NPR',          # Number of ICD-10-PCS procedures
]

# Hospital File Columns
hospital_columns = [
    'HOSP_ED',          # HCUP ED hospital identifier
    'CONTROL',          # Control/ownership of hospital
    'REGION',           # Region of hospital
    'TRAUMA',           # Trauma center level
    'URCAT4',           # Urban-rural designation of hospital
    'NEDS_STRATUM',     # Stratum used to sample hospital
    'N_DISC_U',         # Number of AHA universe ED visits in NEDS_STRATUM
    'N_HOSP_U',         # Number of AHA universe hospitals in NEDS_STRATUM
    'N_HOSP_F',         # Number of frame hospitals in NEDS_STRATUM
    'S_DISC_U',         # Number of sample ED visits in NEDS_STRATUM
    'S_HOSP_U',         # Number of sample hospitals in NEDS_STRATUM
    'S_HOSP_F',         # Number of frame hospitals in NEDS_STRATUM
    'EDVISITS',         # Number of ED visits reported by hospital
    'YEAR',             # Calendar year
]

# ED File Columns (Treat-and-Release)
ed_columns = [
    'KEY_ED',           # HCUP record identifier
    'CPT1',             # CPT/HCPCS procedure code 1
    'CPT2',             # CPT/HCPCS procedure code 2
    'CPT3',             # CPT/HCPCS procedure code 3
    'CPT4',             # CPT/HCPCS procedure code 4
    'CPT5',             # CPT/HCPCS procedure code 5
    'CPT6',             # CPT/HCPCS procedure code 6
    'CPT7',             # CPT/HCPCS procedure code 7
    'CPT8',             # CPT/HCPCS procedure code 8
    'CPT9',             # CPT/HCPCS procedure code 9
    'CPT10',            # CPT/HCPCS procedure code 10
    'CPT11',            # CPT/HCPCS procedure code 11
    'CPT12',            # CPT/HCPCS procedure code 12
    'CPT13',            # CPT/HCPCS procedure code 13
    'CPT14',            # CPT/HCPCS procedure code 14
    'CPT15',            # CPT/HCPCS procedure code 15
    'PRCCSED1',         # CCS procedure category for CPT 1
    'PRCCSED2',         # CCS procedure category for CPT 2
    'PRCCSED3',         # CCS procedure category for CPT 3
    'PRCCSED4',         # CCS procedure category for CPT 4
    'PRCCSED5',         # CCS procedure category for CPT 5
    'PRCCSED6',         # CCS procedure category for CPT 6
    'PRCCSED7',         # CCS procedure category for CPT 7
    'PRCCSED8',         # CCS procedure category for CPT 8
    'PRCCSED9',         # CCS procedure category for CPT 9
    'PRCCSED10',        # CCS procedure category for CPT 10
    'PRCCSED11',        # CCS procedure category for CPT 11
    'PRCCSED12',        # CCS procedure category for CPT 12
    'PRCCSED13',        # CCS procedure category for CPT 13
    'PRCCSED14',        # CCS procedure category for CPT 14
    'PRCCSED15',        # CCS procedure category for CPT 15
    'CPTDAY1',          # Days from admission to CPT 1
    'CPTDAY2',          # Days from admission to CPT 2
    'CPTDAY3',          # Days from admission to CPT 3
    'CPTDAY4',          # Days from admission to CPT 4
    'CPTDAY5',          # Days from admission to CPT 5
    'CPTDAY6',          # Days from admission to CPT 6
    'CPTDAY7',          # Days from admission to CPT 7
    'CPTDAY8',          # Days from admission to CPT 8
    'CPTDAY9',          # Days from admission to CPT 9
    'CPTDAY10',         # Days from admission to CPT 10
    'CPTDAY11',         # Days from admission to CPT 11
    'CPTDAY12',         # Days from admission to CPT 12
    'CPTDAY13',         # Days from admission to CPT 13
    'CPTDAY14',         # Days from admission to CPT 14
    'CPTDAY15',         # Days from admission to CPT 15
    'HOSP_ED',          # HCUP ED hospital identifier
    'DX1_POA',          # Present on admission indicator for diagnosis 1
    'DX2_POA',          # Present on admission indicator for diagnosis 2
    'DX3_POA',          # Present on admission indicator for diagnosis 3
    'DX4_POA',          # Present on admission indicator for diagnosis 4
    'DX5_POA',          # Present on admission indicator for diagnosis 5
    'NEDS_YEAR',        # Year for NEDS
    'NEDS_WEIGHT',      # Weight to NEDS discharges
    'PRCCSED10',        # CCS procedure category for CPT 10
    'PRCCSED11',        # CCS procedure category for CPT 11
    'PRCCSED12',        # CCS procedure category for CPT 12
    'PRCCSED13',        # CCS procedure category for CPT 13
    'PRCCSED14',        # CCS procedure category for CPT 14
    'PRCCSED15',        # CCS procedure category for CPT 15
    'REVCD1',           # Revenue code 1
    'REVCD2',           # Revenue code 2
    'REVCD3',           # Revenue code 3
    'REVCD4',           # Revenue code 4
    'REVCD5',           # Revenue code 5
    'REVCD6',           # Revenue code 6
    'REVCD7',           # Revenue code 7
    'REVCD8',           # Revenue code 8
    'REVCD9',           # Revenue code 9
    'REVCD10',          # Revenue code 10
    'REVCD11',          # Revenue code 11
    'REVCD12',          # Revenue code 12
    'REVCD13',          # Revenue code 13
    'REVCD14',          # Revenue code 14
    'REVCD15',          # Revenue code 15
    'SERVDAY1',         # Days from ED admission to service 1
    'SERVDAY2',         # Days from ED admission to service 2
    'SERVDAY3',         # Days from ED admission to service 3
    'SERVDAY4',         # Days from ED admission to service 4
    'SERVDAY5',         # Days from ED admission to service 5
    'SERVDAY6',         # Days from ED admission to service 6
    'SERVDAY7',         # Days from ED admission to service 7
    'SERVDAY8',         # Days from ED admission to service 8
    'SERVDAY9',         # Days from ED admission to service 9
    'SERVDAY10',        # Days from ED admission to service 10
    'SERVDAY11',        # Days from ED admission to service 11
    'SERVDAY12',        # Days from ED admission to service 12
    'SERVDAY13',        # Days from ED admission to service 13
    'SERVDAY14',        # Days from ED admission to service 14
    'SERVDAY15',        # Days from ED admission to service 15
]

# IP File Columns (Admitted Patients)
ip_columns = [
    'KEY_ED',           # HCUP record identifier
    'DRG',              # DRG in effect on discharge date
    'DRG_NoPOA',        # DRG assignment without POA
    'DRGVER',           # DRG grouper version
    'DX_Visit_Reason1', # Reason for visit diagnosis 1
    'DX_Visit_Reason2', # Reason for visit diagnosis 2
    'DX_Visit_Reason3', # Reason for visit diagnosis 3
    'I10_DX1',          # ICD-10-CM Diagnosis 1
    'I10_DX2',          # ICD-10-CM Diagnosis 2
    'I10_DX3',          # ICD-10-CM Diagnosis 3
    'I10_DX4',          # ICD-10-CM Diagnosis 4
    'I10_DX5',          # ICD-10-CM Diagnosis 5
    'I10_PR1',          # ICD-10-PCS Procedure 1
    'I10_PR2',          # ICD-10-PCS Procedure 2
    'I10_PR3',          # ICD-10-PCS Procedure 3
    'I10_PR4',          # ICD-10-PCS Procedure 4
    'I10_PR5',          # ICD-10-PCS Procedure 5
    'I10_PR6',          # ICD-10-PCS Procedure 6
    'I10_PR7',          # ICD-10-PCS Procedure 7
    'I10_PR8',          # ICD-10-PCS Procedure 8
    'I10_PR9',          # ICD-10-PCS Procedure 9
    'I10_PR10',         # ICD-10-PCS Procedure 10
    'I10_PR11',         # ICD-10-PCS Procedure 11
    'I10_PR12',         # ICD-10-PCS Procedure 12
    'I10_PR13',         # ICD-10-PCS Procedure 13
    'I10_PR14',         # ICD-10-PCS Procedure 14
    'I10_PR15',         # ICD-10-PCS Procedure 15
    'LOS_IP',           # Length of inpatient stay
    'MDC',              # MDC in effect on discharge date
    'MDC_NoPOA',        # MDC assignment without POA
    'NPR_IP',           # Number of procedures on this record
    'ORPROC',           # Major operating room procedure indicator
    'TOTCHG_IP',        # Total charges for inpatient services
    'PRDAY1',           # Number of days from admission to PR1
    'PRDAY2',           # Number of days from admission to PR2
    'PRDAY3',           # Number of days from admission to PR3
    'PRDAY4',           # Number of days from admission to PR4
    'PRDAY5',           # Number of days from admission to PR5
    'PRDAY6',           # Number of days from admission to PR6
    'PRDAY7',           # Number of days from admission to PR7
    'PRDAY8',           # Number of days from admission to PR8
    'PRDAY9',           # Number of days from admission to PR9
    'PRDAY10',          # Number of days from admission to PR10
    'PRDAY11',          # Number of days from admission to PR11
    'PRDAY12',          # Number of days from admission to PR12
    'PRDAY13',          # Number of days from admission to PR13
    'PRDAY14',          # Number of days from admission to PR14
    'PRDAY15',          # Number of days from admission to PR15
    'HOSP_ED',          # HCUP ED hospital identifier
    'DX1_POA',          # Present on admission indicator for diagnosis 1
    'DX2_POA',          # Present on admission indicator for diagnosis 2
    'DX3_POA',          # Present on admission indicator for diagnosis 3
    'DX4_POA',          # Present on admission indicator for diagnosis 4
    'DX5_POA',          # Present on admission indicator for diagnosis 5
    'NEDS_YEAR',        # Year for NEDS
    'NEDS_WEIGHT',      # Weight to NEDS discharges
    'NEDS_STRATUM',     # Stratum used to post-stratify
    'I10_NDX',          # Number of ICD-10-CM diagnoses
    'I10_NPR',          # Number of ICD-10-PCS procedures
]

# DX_PR_GRPS File Columns
dx_pr_grps_columns = [
    'KEY_ED',           # HCUP record identifier
    'DXCCSR_Default_DX1', # Default CCSR category for first-listed diagnosis
    'DXCCSR_Default_DX2', # Default CCSR category for second-listed diagnosis
    'DXCCSR_Default_DX3', # Default CCSR category for third-listed diagnosis
    'DXCCSR_Default_DX4', # Default CCSR category for fourth-listed diagnosis
    'DXCCSR_Default_DX5', # Default CCSR category for fifth-listed diagnosis
    'DXCCSR_Default_DX6', # Default CCSR category for sixth-listed diagnosis
    'DXCCSR_Default_DX7', # Default CCSR category for seventh-listed diagnosis
    'DXCCSR_Default_DX8', # Default CCSR category for eighth-listed diagnosis
    'DXCCSR_Default_DX9', # Default CCSR category for ninth-listed diagnosis
    'DXCCSR_Default_DX10', # Default CCSR category for tenth-listed diagnosis
    'DXCCSR_Default_DX11', # Default CCSR category for eleventh-listed diagnosis
    'DXCCSR_Default_DX12', # Default CCSR category for twelfth-listed diagnosis
    'DXCCSR_Default_DX13', # Default CCSR category for thirteenth-listed diagnosis
    'DXCCSR_Default_DX14', # Default CCSR category for fourteenth-listed diagnosis
    'DXCCSR_Default_DX15', # Default CCSR category for fifteenth-listed diagnosis
    'DXCCSR_VERSION',    # Version of CCSR for diagnoses
    'INJURY_CUT',       # Injury by cutting or piercing
    'INJURY_DROWN',     # Injury by drowning or submersion
    'INJURY_FALL',      # Injury by falling
    'INJURY_FIRE',      # Injury by fire, flame, or hot object
    'INJURY_FIREARM',   # Injury by firearm
    'INJURY_MACHINERY', # Injury by machinery
    'INJURY_MVT',       # Injury by motor vehicle traffic
    'INJURY_NATURE',    # Injury by natural or environmental causes
    'INJURY_POISON',    # Injury by poison
    'INJURY_SEVERITY',  # Injury severity score
    'INJURY_STRUCK',    # Injury by being struck by or against
    'INJURY_SUFFOCATION', # Injury by suffocation
    'INTENT_ASSAULT',   # Assault injury
    'INTENT_SELF_HARM', # Self-inflicted injury
    'INTENT_UNINTENTIONAL', # Unintentional injury
    'MULTINJURY',       # Multiple injuries
    'PRCCSR_Default_PR1',  # Default CCSR category for principal procedure
    'PRCCSR_Default_PR2',  # Default CCSR category for procedure 2
    'PRCCSR_Default_PR3',  # Default CCSR category for procedure 3
    'PRCCSR_Default_PR4',  # Default CCSR category for procedure 4
    'PRCCSR_Default_PR5',  # Default CCSR category for procedure 5
    'PRCCSR_Default_PR6',  # Default CCSR category for procedure 6
    'PRCCSR_Default_PR7',  # Default CCSR category for procedure 7
    'PRCCSR_Default_PR8',  # Default CCSR category for procedure 8
    'PRCCSR_Default_PR9',  # Default CCSR category for procedure 9
    'PRCCSR_Default_PR10', # Default CCSR category for procedure 10
    'PRCCSR_Default_PR11', # Default CCSR category for procedure 11
    'PRCCSR_Default_PR12', # Default CCSR category for procedure 12
    'PRCCSR_Default_PR13', # Default CCSR category for procedure 13
    'PRCCSR_Default_PR14', # Default CCSR category for procedure 14
    'PRCCSR_Default_PR15', # Default CCSR category for procedure 15
    'PRCCSR_VERSION',      # Version of CCSR for procedures
]

# Dictionary mapping file types to their columns
neds_file_columns = {
    'core': core_columns,
    'hospital': hospital_columns,
    'ed': ed_columns,
    'ip': ip_columns,
    'dx_pr_grps': dx_pr_grps_columns
} 