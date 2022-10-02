import pandas as pd

def	margin(df, col):
    df[col["source_type"]] = df[col["source_type"]].astype(str)
    for index, row in df.iterrows():
        if (row[col["source_type"]] == "nan"):
            if row[col["score"]] >= 65:
                df.at[index, col["source_type"]] = "Hot"
            elif row[col["score"]] >= 40 and row[col["score"]] < 65:
                df.at[index, col["source_type"]] = "Warm"
            elif row[col["score"]] >= 0 and row[col["score"]] < 40:
                df.at[index, col["source_type"]] = "Cold"
            else:
                df.at[index, col["source_type"]] = "Dead"
