import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    #using regular expression to locate valid emails
    valid_emails_df=users.loc[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]
    return valid_emails_df
