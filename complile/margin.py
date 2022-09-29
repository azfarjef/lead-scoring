import pandas as pd

def	margin(df):
    df["source type"] = df["source type"].astype(str)
    for index, row in df.iterrows():
        if (row["Source Type"] == "nan"):
            if row["lead priority level"] >= 65:
                df.at[index, "source type"] = "Hot"
            elif row["lead priority level"] >= 40 and row["lead priority level"] < 65:
                df.at[index, "source type"] = "Warm"
            elif row["lead priority level"] >= 0 and row["lead priority level"] < 40:
                df.at[index, "source type"] = "Cold"
            else:
                df.at[index, "source type"] = "Dead"
