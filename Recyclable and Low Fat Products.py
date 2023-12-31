```
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    find_products_df = products[(products['recyclable']=='Y') & (products['low_fats']=='Y')]
    return find_products_df[['product_id']]
```
