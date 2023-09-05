import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    #sorting score before submitting
    scores.sort_values(by='score',ascending=False,inplace=True)
    #using 'rank' to rank rows in descending 
    scores['rank']=(scores['score'].rank(method='dense',ascending=False))
    return scores[['score','rank']]
