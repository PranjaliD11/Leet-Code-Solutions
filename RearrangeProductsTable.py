import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    rearraged_products=products.melt(id_vars=['product_id'],value_vars=['store1','store2','store3'],var_name='store',value_name='price')
    rearraged_products.dropna(axis=0,inplace=True)
    return rearraged_products
