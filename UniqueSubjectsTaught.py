import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    #selecting only unique pairs of teachers and subjects
    unique_sub_df=teacher.drop_duplicates(subset=['teacher_id','subject_id'],keep='first')
    #grouping together teacher id and counting number of subjects
    count_df=unique_sub_df.groupby('teacher_id')['subject_id'].count().reset_index()
    #renaming the columns
    count_df.columns=(['teacher_id','cnt'])
    return count_df
