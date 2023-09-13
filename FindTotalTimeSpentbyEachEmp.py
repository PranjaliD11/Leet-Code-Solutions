import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time']=employees['out_time']-employees['in_time']
    employees.drop(['in_time','out_time'],axis=1, inplace=True)
    #group by day and employee id and then sum up the time
    total_time.df=employees.groupby(['event_day','emp_id']).sum().reset_index()
    total_time.df=total_time.df.sort_values(by='emp_id')
    total_time.df.rename(columns={'event_day':'day'}, inplace=True)
    return total_time.df
    
