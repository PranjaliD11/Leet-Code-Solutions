import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    total_class=courses.groupby('class')['student'].count().reset_index()
    find_classes=total_class.loc[(total_class['student'])>4][["class"]]
    return find_classes
    
