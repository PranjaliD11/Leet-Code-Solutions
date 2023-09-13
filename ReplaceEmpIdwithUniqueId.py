import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    #using merge function left join to join distinct tables
    result_df=employees.merge(employee_uni, how='left', left_on='id',right_on='id')
    return result_df[['name','unique_id']]
