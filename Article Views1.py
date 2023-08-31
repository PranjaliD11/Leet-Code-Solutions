```
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    #it contains duplicate values
    authors_viewed_df= views[views['author_id']==views['viewer_id']]
    #removing duplicates
    unique_author_id=authors_viewed_df['author_id'].unique()
    #sorting
    unique_author_id=sorted(unique_author_id)
    result_df=pd.DataFrame({'id':unique_author_id})
    return result_df
  ```
