import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
   person=person['email'].drop_duplicates(inplace=True)
