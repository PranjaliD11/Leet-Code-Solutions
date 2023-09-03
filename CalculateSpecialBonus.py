import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    bonus = []
    for index, row in employees.iterrows():
        id=row['employee_id']
        name=row['name']
        salary=row['salary']
        if id%2==0  or name.startswith('M'):
            bonus.append(0)
        else :
            bonus.append(salary)
    employees['bonus']= bonus
    result_df=employees.sort_values(by='employee_id')
    return result_df[['employee_id','bonus']]
