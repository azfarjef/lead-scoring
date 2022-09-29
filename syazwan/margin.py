import pandas as pd

def	margin(df):
    df["Source Type"] = df["Source Type"].astype(str)
    for index, row in df.iterrows():
    
            if row["Lead Priority Level"] >= 65:
                df.at[index, "Source Type"] = "Hot"
            elif row["Lead Priority Level"] >= 40 and row["Lead Priority Level"] < 65:
                df.at[index, "Source Type"] = "Warm"
            elif row["Lead Priority Level"] >= 0 and row["Lead Priority Level"] < 40:
                df.at[index, "Source Type"] = "Cold"
            else:
                print(type(df.at[index, "Source Type"]))
                df.at[index, "Source Type"] = "Dead"
                print(type(df.at[index, "Source Type"]))