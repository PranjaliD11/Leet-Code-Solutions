import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    try_df=daily_sales.groupby(["date_id","make_name"]).nunique().reset_index()
    try_df.rename(columns={'lead_id':'unique_leads','partner_id':'unique_partners'},inplace=True)
    return try_df
