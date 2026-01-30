#Clean a text column in a DataFrame by: 
#1. Converting to lowercase. 
#2. Removing special characters (e.g., !, @). 
#3. Tokenizing the text.

import pandas as pd
import re
def clean_and_tokenize_text(df, column_name):
    df[column_name] = (
        df[column_name]
        .str.lower()
        .str.replace(r'[^a-z\s]', '', regex=True)
        .str.split()
    )
    return df
