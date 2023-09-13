import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df=students.merge(subjects,how='cross').sort_values(by=['student_id','subject_name'])
    attended_exams = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    #examinations=examinations.value_counts().reset_index(name='attended_exams')
    #df=df.merge(examinations,how='left').rename(columns={'count':'attended_exams'})
    df=df.merge(attended_exams,how='left').fillna(0)
    return df[['student_id','student_name','subject_name','attended_exams']]
