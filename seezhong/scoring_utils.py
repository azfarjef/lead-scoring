import pandas as pd

def scores(df):
    for index, row in df.iterrows():
        if row["Head Count"] > 20:
            df.at[index, "Scores"] += 1
        if row["Physical Channel"].lower() == "b2b":
            df.at[index, "Scores"] += 1
        if row["State"].lower() == "penang":
            df.at[index, "Scores"] += 1
        if "sales" in row["Contact Designation"].lower():
            df.at[index, "Scores"] += 1
        if row["Business Nature"].lower() == "manufacturing":
            df.at[index, "Scores"] += 1
