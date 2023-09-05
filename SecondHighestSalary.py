import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    #removing duplicates 
    unique_salaries=employee['salary'].drop_duplicates()
    #sorting the values 
    sorted_salaries=unique_salaries.sort_values(ascending=False)
    #checking if there is only one value
    if len(sorted_salaries)==1:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    second_highest_salary=sorted_salaries.iloc[1]
    return pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
