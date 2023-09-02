import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    #filtering out strings that have lenght greater than 15
    invalid_tweets_df=tweets[tweets['content'].str.len()>15]
    result_df = invalid_tweets_df[['tweet_id']]
    return result_df
