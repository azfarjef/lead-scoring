import pandas as pd

def	margin(df):
    for index, row in df.iterrows():
        if row["Scores"] >= 65:
            df.at[index, "Lead Margin"] = "Hot"
        elif row["Scores"] >= 40 and row["Scores"] < 65:
            df.at[index, "Lead Margin"] = "Warm"
        elif row["Scores"] >= 0 and row["Scores"] < 40:
            df.at[index, "Lead Margin"] = "Cold"
        else:
            df.at[index, "Lead Margin"] = "Dead"