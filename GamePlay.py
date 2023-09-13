import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    #sorting values by the primary keys in ascending  order
    activity.sort_values(by=['player_id','event_date'],ascending=True,inplace=True)
    #dropping all the other logins and keeping the first one
    activity.drop_duplicates(subset='player_id',keep='first',inplace=True)
    result_df=activity[['player_id','event_date']]
    result_df.columns=(['player_id','first_login'])
    return result_df
