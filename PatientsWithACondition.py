import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    find_patients_df=patients.loc[patients['conditions'].str.contains(r'\bDIAB1')]
    return find_patients_df
