import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    #counting how many pairs of actor and director id are there
    count_df=actor_director.value_counts(['actor_id','director_id']).reset_index()
    #selecting those who have cooperated for atleast 3 times 
    result_df=count_df.loc[count_df['count']>2]
    return result_df[['actor_id','director_id']]
