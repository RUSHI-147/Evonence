#A dataset has missing values in the "income" column. Write code to: 
#1. Replace missing values with the median if the data is normally distributed. 
#2. Replace with the mode if skewed. Use Pandas and a skewness threshold of 0.5.

import pandas as pd
def handle_missing_income(df):
    skewness = df['income'].skew()
    if abs(skewness) <= 0.5:
        # Normally distributed → use median
        fill_value = df['income'].median()
        strategy = "median"
    else:
        fill_value = df['income'].mode()[0]
        strategy = "mode"
    df['income'] = df['income'].fillna(fill_value)
    print(f"Missing values filled using {strategy} (skewness = {skewness:.2f})")
    return df
