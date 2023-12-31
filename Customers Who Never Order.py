
``` python

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
     #Selecting only the customers that aren't present in the orders table
     df = customers[~customers['id'].isin(orders['customerId'])]
     df = df[['name']].rename(columns={'name': 'Customers'})

     return df
```
