import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate_count = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']].shape[0]
    total_orders=delivery.shape[0]
    immediate_pct=(immediate_count/total_orders)*100
    result_df=pd.DataFrame({'immediate_percentage':[round(immediate_pct,2)]})
    return result_df
