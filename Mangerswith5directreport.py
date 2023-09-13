import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    test=employee.groupby('managerId')[['id']].count().reset_index()
    manager=test[test['id']>4]
    result=employee.loc[employee['id'].isin(manager['managerId'])]
    return result[['name']]
