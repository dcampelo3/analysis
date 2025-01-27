# KID 2019 Column Specifications

# Core File Columns
core_columns = [
    'AGE',              # Age in years at admission
    'AWEEKEND',         # Admission on weekend
    'DIED',             # Died during hospitalization
    'DISCWT',           # Weight to discharges in AHA universe
    'DISPUNIFORM',      # Disposition of patient, uniform coding
    'DMONTH',           # Discharge month
    'DQTR',             # Discharge quarter
    'DRG',              # DRG in effect on discharge date
    'DRGVER',           # DRG grouper version used on discharge date
    'DRG_NoPOA',        # DRG assignment without POA
    'ELECTIVE',         # Elective versus non-elective admission
    'FEMALE',           # Indicator of sex
    'HCUP_ED',          # HCUP Emergency Department service indicator
    'HOSP_KID',         # KID hospital number
    'I10_DX1',          # ICD-10-CM Principal diagnosis
    'I10_DX2',          # ICD-10-CM Diagnosis 2
    'I10_DX3',          # ICD-10-CM Diagnosis 3
    'I10_DX4',          # ICD-10-CM Diagnosis 4
    'I10_DX5',          # ICD-10-CM Diagnosis 5
    'I10_DX6',          # ICD-10-CM Diagnosis 6
    'I10_DX7',          # ICD-10-CM Diagnosis 7
    'I10_DX8',          # ICD-10-CM Diagnosis 8
    'I10_DX9',          # ICD-10-CM Diagnosis 9
    'I10_DX10',         # ICD-10-CM Diagnosis 10
    'I10_DX11',         # ICD-10-CM Diagnosis 11
    'I10_DX12',         # ICD-10-CM Diagnosis 12
    'I10_DX13',         # ICD-10-CM Diagnosis 13
    'I10_DX14',         # ICD-10-CM Diagnosis 14
    'I10_DX15',         # ICD-10-CM Diagnosis 15
    'I10_DX16',         # ICD-10-CM Diagnosis 16
    'I10_DX17',         # ICD-10-CM Diagnosis 17
    'I10_DX18',         # ICD-10-CM Diagnosis 18
    'I10_DX19',         # ICD-10-CM Diagnosis 19
    'I10_DX20',         # ICD-10-CM Diagnosis 20
    'I10_DX21',         # ICD-10-CM Diagnosis 21
    'I10_DX22',         # ICD-10-CM Diagnosis 22
    'I10_DX23',         # ICD-10-CM Diagnosis 23
    'I10_DX24',         # ICD-10-CM Diagnosis 24
    'I10_DX25',         # ICD-10-CM Diagnosis 25
    'I10_ECAUSE1',      # ICD-10-CM External cause 1
    'I10_ECAUSE2',      # ICD-10-CM External cause 2
    'I10_ECAUSE3',      # ICD-10-CM External cause 3
    'I10_ECAUSE4',      # ICD-10-CM External cause 4
    'I10_NDX',          # Number of ICD-10-CM diagnoses on this record
    'I10_NECAUSE',      # Number of external cause codes on this record
    'I10_NPR',          # Number of procedures on this record
    'I10_PR1',          # ICD-10-PCS Principal procedure
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
    'KEY_KID',          # HCUP record identifier
    'KID_STRATUM',      # Stratum used to post-stratify hospital
    'LOS',              # Length of stay, cleaned
    'MDC',              # MDC in effect on discharge date
    'MDC_NoPOA',        # MDC assignment without POA
    'NCHRONIC',         # Number of chronic conditions
    'NDX',              # Number of diagnoses on this record
    'NEOMAT',           # Neonatal/maternal DX and PR indicators
    'NPR',              # Number of procedures on this record
    'PAY1',             # Primary expected payer
    'PAY2',             # Secondary expected payer
    'PL_NCHS',          # Patient Location: NCHS Urban-Rural Code
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
    'RACE',             # Race (uniform)
    'TOTCHG',           # Total charges, cleaned
    'TRAN_IN',          # Transfer in indicator
    'TRAN_OUT',         # Transfer out indicator
    'YEAR',             # Calendar year
    'ZIPINC_QRTL',      # Median household income quartile for patient's ZIP Code
    'UNCBRTH',          # Uncomplicated in-hospital birth indicator
    'HOSPBRTH',         # In-hospital birth indicator
    'POINT_OF_ORIGIN_UNIF',  # Point of origin for admission or visit, uniform coding
    'PointOfOriginUB04',     # Point of origin for admission or visit, UB-04 standard coding
]

# Severity File Columns
severity_columns = [
    'KEY_KID',          # HCUP record identifier
    'HOSP_KID',         # KID hospital identifier
    'APRDRG',           # All Patient Refined DRG
    'APRDRG_Risk_Mortality',  # All Patient Refined DRG: Risk of Mortality Subclass
    'APRDRG_Severity',  # All Patient Refined DRG: Severity of Illness Subclass
    'CM_AIDS',          # AHRQ comorbidity measure: Acquired immune deficiency syndrome
    'CM_ALCOHOL',       # AHRQ comorbidity measure: Alcohol abuse
    'CM_ANEMDEF',       # AHRQ comorbidity measure: Deficiency anemias
    'CM_ARTH',          # AHRQ comorbidity measure: Rheumatoid arthritis/collagen vascular diseases
    'CM_BLDLOSS',       # AHRQ comorbidity measure: Chronic blood loss anemia
    'CM_CHF',           # AHRQ comorbidity measure: Congestive heart failure
    'CM_CHRNLUNG',      # AHRQ comorbidity measure: Chronic pulmonary disease
    'CM_COAG',          # AHRQ comorbidity measure: Coagulopathy
    'CM_DEPRESS',       # AHRQ comorbidity measure: Depression
    'CM_DM',            # AHRQ comorbidity measure: Diabetes, uncomplicated
    'CM_DMCX',          # AHRQ comorbidity measure: Diabetes with chronic complications
    'CM_DRUG',          # AHRQ comorbidity measure: Drug abuse
    'CM_HTN_C',         # AHRQ comorbidity measure: Hypertension
    'CM_HYPOTHY',       # AHRQ comorbidity measure: Hypothyroidism
    'CM_LIVER',         # AHRQ comorbidity measure: Liver disease
    'CM_LYMPH',         # AHRQ comorbidity measure: Lymphoma
    'CM_LYTES',         # AHRQ comorbidity measure: Fluid and electrolyte disorders
    'CM_METS',          # AHRQ comorbidity measure: Metastatic cancer
    'CM_NEURO',         # AHRQ comorbidity measure: Other neurological disorders
    'CM_OBESE',         # AHRQ comorbidity measure: Obesity
    'CM_PARA',          # AHRQ comorbidity measure: Paralysis
    'CM_PERIVASC',      # AHRQ comorbidity measure: Peripheral vascular disorders
    'CM_PSYCH',         # AHRQ comorbidity measure: Psychoses
    'CM_PULMCIRC',      # AHRQ comorbidity measure: Pulmonary circulation disorders
    'CM_RENLFAIL',      # AHRQ comorbidity measure: Renal failure
    'CM_TUMOR',         # AHRQ comorbidity measure: Solid tumor without metastasis
    'CM_ULCER',         # AHRQ comorbidity measure: Peptic ulcer disease excluding bleeding
    'CM_VALVE',         # AHRQ comorbidity measure: Valvular disease
    'CM_WGHTLOSS',      # AHRQ comorbidity measure: Weight loss
]

# Hospital File Columns
hospital_columns = [
    'HOSP_KID',         # KID hospital number
    'HOSP_BEDSIZE',     # Bed size of hospital
    'H_CONTRL',         # Control/ownership of hospital
    'HOSP_LOCTEACH',    # Location/teaching status of hospital
    'HOSP_REGION',      # Region of hospital
    'HOSP_RNPCT',       # Percentage of RN among licensed nurses
    'HOSP_URCAT4',      # Hospital urban-rural designation
    'KID_STRATUM',      # Stratum used to post-stratify hospital
    'N_DISC_U',         # Number of AHA universe discharges in KID_STRATUM
    'N_HOSP_U',         # Number of AHA universe hospitals in KID_STRATUM
    'N_KID_U',          # Number of KID universe discharges in KID_STRATUM
    'S_DISC_U',         # Number of sample discharges in KID_STRATUM
    'S_HOSP_U',         # Number of sample hospitals in KID_STRATUM
    'S_KID_U',          # Number of sample KID discharges in KID_STRATUM
    'TOTAL_DISC',       # Total hospital discharges
    'YEAR',             # Calendar year
]

# DX_PR_GRPS File Columns
dx_pr_grps_columns = [
    'KEY_KID',          # HCUP record identifier
    'HOSP_KID',         # KID hospital number
    'BODYSYSTEM1',      # Body system for principal procedure
    'BODYSYSTEM2',      # Body system for procedure 2
    'BODYSYSTEM3',      # Body system for procedure 3
    'BODYSYSTEM4',      # Body system for procedure 4
    'BODYSYSTEM5',      # Body system for procedure 5
    'BODYSYSTEM6',      # Body system for procedure 6
    'BODYSYSTEM7',      # Body system for procedure 7
    'BODYSYSTEM8',      # Body system for procedure 8
    'BODYSYSTEM9',      # Body system for procedure 9
    'BODYSYSTEM10',     # Body system for procedure 10
    'BODYSYSTEM11',     # Body system for procedure 11
    'BODYSYSTEM12',     # Body system for procedure 12
    'BODYSYSTEM13',     # Body system for procedure 13
    'BODYSYSTEM14',     # Body system for procedure 14
    'BODYSYSTEM15',     # Body system for procedure 15
    'DXCCSR_DEFAULT_DX1',  # Default CCSR category for principal diagnosis
    'DXCCSR_DEFAULT_DX2',  # Default CCSR category for diagnosis 2
    'DXCCSR_DEFAULT_DX3',  # Default CCSR category for diagnosis 3
    'DXCCSR_DEFAULT_DX4',  # Default CCSR category for diagnosis 4
    'DXCCSR_DEFAULT_DX5',  # Default CCSR category for diagnosis 5
    'DXCCSR_DEFAULT_DX6',  # Default CCSR category for diagnosis 6
    'DXCCSR_DEFAULT_DX7',  # Default CCSR category for diagnosis 7
    'DXCCSR_DEFAULT_DX8',  # Default CCSR category for diagnosis 8
    'DXCCSR_DEFAULT_DX9',  # Default CCSR category for diagnosis 9
    'DXCCSR_DEFAULT_DX10', # Default CCSR category for diagnosis 10
    'DXCCSR_DEFAULT_DX11', # Default CCSR category for diagnosis 11
    'DXCCSR_DEFAULT_DX12', # Default CCSR category for diagnosis 12
    'DXCCSR_DEFAULT_DX13', # Default CCSR category for diagnosis 13
    'DXCCSR_DEFAULT_DX14', # Default CCSR category for diagnosis 14
    'DXCCSR_DEFAULT_DX15', # Default CCSR category for diagnosis 15
    'DXCCSR_DEFAULT_DX16', # Default CCSR category for diagnosis 16
    'DXCCSR_DEFAULT_DX17', # Default CCSR category for diagnosis 17
    'DXCCSR_DEFAULT_DX18', # Default CCSR category for diagnosis 18
    'DXCCSR_DEFAULT_DX19', # Default CCSR category for diagnosis 19
    'DXCCSR_DEFAULT_DX20', # Default CCSR category for diagnosis 20
    'DXCCSR_DEFAULT_DX21', # Default CCSR category for diagnosis 21
    'DXCCSR_DEFAULT_DX22', # Default CCSR category for diagnosis 22
    'DXCCSR_DEFAULT_DX23', # Default CCSR category for diagnosis 23
    'DXCCSR_DEFAULT_DX24', # Default CCSR category for diagnosis 24
    'DXCCSR_DEFAULT_DX25', # Default CCSR category for diagnosis 25
    'DXCCSR_DEFAULT_DX26', # Default CCSR category for diagnosis 26
    'DXCCSR_DEFAULT_DX27', # Default CCSR category for diagnosis 27
    'DXCCSR_DEFAULT_DX28', # Default CCSR category for diagnosis 28
    'DXCCSR_DEFAULT_DX29', # Default CCSR category for diagnosis 29
    'DXCCSR_DEFAULT_DX30', # Default CCSR category for diagnosis 30
    'DXCCSR_DEFAULT_DX31', # Default CCSR category for diagnosis 31
    'DXCCSR_DEFAULT_DX32', # Default CCSR category for diagnosis 32
    'DXCCSR_DEFAULT_DX33', # Default CCSR category for diagnosis 33
    'DXCCSR_DEFAULT_DX34', # Default CCSR category for diagnosis 34
    'DXCCSR_DEFAULT_DX35', # Default CCSR category for diagnosis 35
    'DXCCSR_DEFAULT_DX36', # Default CCSR category for diagnosis 36
    'DXCCSR_DEFAULT_DX37', # Default CCSR category for diagnosis 37
    'DXCCSR_DEFAULT_DX38', # Default CCSR category for diagnosis 38
    'DXCCSR_DEFAULT_DX39', # Default CCSR category for diagnosis 39
    'DXCCSR_DEFAULT_DX40', # Default CCSR category for diagnosis 40
    'DXCCSR_VERSION',      # Version of CCSR for diagnoses
    'I10_BIRTH',           # Indicator of birth diagnosis
    'I10_DELIVERY',        # Indicator of delivery diagnosis
    'I10_INJURY',          # Indicator of injury diagnosis
    'I10_INJURY_CUT',      # Injury by cutting or piercing
    'I10_INJURY_DROWN',    # Injury by drowning or submersion
    'I10_INJURY_FALL',     # Injury by falling
    'I10_INJURY_FIRE',     # Injury by fire, flame, or hot object
    'I10_INJURY_FIREARM',  # Injury by firearm
    'I10_INJURY_MACHINERY',# Injury by machinery
    'I10_INJURY_MVT',      # Injury by motor vehicle traffic
    'I10_INJURY_NATURE',   # Injury by natural or environmental causes
    'I10_INJURY_POISON',   # Injury by poison
    'I10_INJURY_SEVERITY', # Injury severity score
    'I10_INJURY_STRUCK',   # Injury by being struck by or against
    'I10_INJURY_SUFFOCATION', # Injury by suffocation
    'I10_INTENT_ASSAULT',  # Assault injury
    'I10_INTENT_SELF_HARM',# Self-inflicted injury
    'I10_INTENT_UNINTENTIONAL', # Unintentional injury
    'I10_MULTINJURY',      # Multiple injuries
    'I10_SERVICELINE',     # Primary service line for this record
    'PRCCSR_DEFAULT_PR1',  # Default CCSR category for principal procedure
    'PRCCSR_DEFAULT_PR2',  # Default CCSR category for procedure 2
    'PRCCSR_DEFAULT_PR3',  # Default CCSR category for procedure 3
    'PRCCSR_DEFAULT_PR4',  # Default CCSR category for procedure 4
    'PRCCSR_DEFAULT_PR5',  # Default CCSR category for procedure 5
    'PRCCSR_DEFAULT_PR6',  # Default CCSR category for procedure 6
    'PRCCSR_DEFAULT_PR7',  # Default CCSR category for procedure 7
    'PRCCSR_DEFAULT_PR8',  # Default CCSR category for procedure 8
    'PRCCSR_DEFAULT_PR9',  # Default CCSR category for procedure 9
    'PRCCSR_DEFAULT_PR10', # Default CCSR category for procedure 10
    'PRCCSR_DEFAULT_PR11', # Default CCSR category for procedure 11
    'PRCCSR_DEFAULT_PR12', # Default CCSR category for procedure 12
    'PRCCSR_DEFAULT_PR13', # Default CCSR category for procedure 13
    'PRCCSR_DEFAULT_PR14', # Default CCSR category for procedure 14
    'PRCCSR_DEFAULT_PR15', # Default CCSR category for procedure 15
    'PRCCSR_VERSION',      # Version of CCSR for procedures
    'E_POA1',           # Present on admission indicator for E code 1
    'E_POA2',           # Present on admission indicator for E code 2
    'E_POA3',           # Present on admission indicator for E code 3
    'E_POA4',           # Present on admission indicator for E code 4
    'DX1_POA',          # Present on admission indicator for diagnosis 1
    'DX2_POA',          # Present on admission indicator for diagnosis 2
    'DX3_POA',          # Present on admission indicator for diagnosis 3
    'DX4_POA',          # Present on admission indicator for diagnosis 4
    'DX5_POA',          # Present on admission indicator for diagnosis 5
    'DX6_POA',          # Present on admission indicator for diagnosis 6
    'DX7_POA',          # Present on admission indicator for diagnosis 7
    'DX8_POA',          # Present on admission indicator for diagnosis 8
    'DX9_POA',          # Present on admission indicator for diagnosis 9
    'DX10_POA',         # Present on admission indicator for diagnosis 10
    'DX11_POA',         # Present on admission indicator for diagnosis 11
    'DX12_POA',         # Present on admission indicator for diagnosis 12
    'DX13_POA',         # Present on admission indicator for diagnosis 13
    'DX14_POA',         # Present on admission indicator for diagnosis 14
    'DX15_POA',         # Present on admission indicator for diagnosis 15
    'DX16_POA',         # Present on admission indicator for diagnosis 16
    'DX17_POA',         # Present on admission indicator for diagnosis 17
    'DX18_POA',         # Present on admission indicator for diagnosis 18
    'DX19_POA',         # Present on admission indicator for diagnosis 19
    'DX20_POA',         # Present on admission indicator for diagnosis 20
    'DX21_POA',         # Present on admission indicator for diagnosis 21
    'DX22_POA',         # Present on admission indicator for diagnosis 22
    'DX23_POA',         # Present on admission indicator for diagnosis 23
    'DX24_POA',         # Present on admission indicator for diagnosis 24
    'DX25_POA',         # Present on admission indicator for diagnosis 25
    'DX26_POA',         # Present on admission indicator for diagnosis 26
    'DX27_POA',         # Present on admission indicator for diagnosis 27
    'DX28_POA',         # Present on admission indicator for diagnosis 28
    'DX29_POA',         # Present on admission indicator for diagnosis 29
    'DX30_POA',         # Present on admission indicator for diagnosis 30
    'DX31_POA',         # Present on admission indicator for diagnosis 31
    'DX32_POA',         # Present on admission indicator for diagnosis 32
    'DX33_POA',         # Present on admission indicator for diagnosis 33
    'DX34_POA',         # Present on admission indicator for diagnosis 34
    'DX35_POA',         # Present on admission indicator for diagnosis 35
    'DX36_POA',         # Present on admission indicator for diagnosis 36
    'DX37_POA',         # Present on admission indicator for diagnosis 37
    'DX38_POA',         # Present on admission indicator for diagnosis 38
    'DX39_POA',         # Present on admission indicator for diagnosis 39
    'DX40_POA',         # Present on admission indicator for diagnosis 40
]

# Dictionary mapping file types to their columns
kid_file_columns = {
    'core': core_columns,
    'severity': severity_columns,
    'hospital': hospital_columns,
    'dx_pr_grps': dx_pr_grps_columns
} 