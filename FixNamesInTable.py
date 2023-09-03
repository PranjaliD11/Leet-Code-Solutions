import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    #str.capitalize function capitalizes the first letter of the string
    users['name']=users['name'].str.capitalize()
    users=users.sort_values(by='user_id')
    return users
