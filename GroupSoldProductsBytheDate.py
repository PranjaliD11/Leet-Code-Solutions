import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    grouping_products_df=activities.groupby('sell_date')['product'].agg(['nunique' ,lambda x:','.join(sorted(set(x)))]).reset_index()
    grouping_products_df.columns = ['sell_date', 'num_sold', 'products']
    return grouping_products_df
