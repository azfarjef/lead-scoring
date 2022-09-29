import pandas as pd
from re import sub
from decimal import Decimal
from datetime import date
from margin import margin

weight1 = 0.3   # Industry
weight2 = 0.15  # Suspect creation date
weight3 = 0.1   # Employee Count
weight4 = 0.1   # Total potential revenue
weight5 = 0.05  # Physical Channel
weight6 = 0.1   # Lead source
weight7 = 0.2   # Contact person Designation


def Industry(index, row, df):
    if row["Industry"].lower() == "consumer" or row["Industry"].lower() == "retail":
        df.at[index, "Scores"] += weight1 * 100
    elif row["Industry"].lower() == "chemical and energy" or row["Industry"].lower() == "technology" or row["Industry"].lower() == "service logistics" \
            or row["Industry"].lower() == "manufacturing" or row["Industry"].lower() == "distributor":
        df.at[index, "Scores"] += weight1 * 80
    elif row["Industry"].lower() == "life sciences and healthcare":
        df.at[index, "Scores"] += weight1 * 60
    else:
        df.at[index, "Scores"] += weight1 * 40

def last_created(index, row, df):
    if row["Last Created"] < 10:
        df.at[index, "Scores"] += weight2 * 100
    elif row["Last Created"] >= 10 and row["Last Created"] < 31:
        df.at[index, "Scores"] += weight2 * 50
    elif row["Last Created"] >= 31 and row["Last Created"] < 90:
        df.at[index, "Scores"] += weight2 * -50
    else:
        df.at[index, "Scores"] += weight2 * -100

def	employee(index, row, df):
	if row["Employee Count"] > 100:
		df.at[index, "Scores"] += weight3 * 100
	elif row["Employee Count"] <= 100 and row["Employee Count"] > 50:
		df.at[index, "Scores"] += weight3 * 50
	elif row["Employee Count"] <= 50:
		df.at[index, "Scores"] += weight3 * 20

def revenue(index, row, df):
    if row["Total Potential Revenue/Month"] > 1000:
        df.at[index, "Scores"] += weight4 * 100
    elif row ["Total Potential Revenue/Month"] > 500 and row["Total Potential Revenue/Month"] <= 1000:
        df.at[index, "Scores"] += weight4 * 80
    elif row["Total Potential Revenue/Month"] > 100 and row["Total Potential Revenue/Month"] <= 500:
        df.at[index, "Scores"] += weight4 * 50
    else:
        df.at[index, "Scores"] += weight4 * 20

def channel(index, row, df):
    if row["Physical Channel"].lower() == "b2b":
        df.at[index, "Scores"] += weight5 * 100
    elif row["Physical Channel"].lower() == "b2c":
        df.at[index, "Scores"] += weight5 * 80
    else:
        df.at[index, "Scores"] += weight5 * -50

def source(index, row, df):
    if row["Lead Source Name"].lower() == "facebook" or row["Lead Source Name"].lower() == "twitter":
        df.at[index, "Scores"] += weight6 * 70
    elif row["Lead Source Name"].lower() == "ex database" or row["Lead Source Name"].lower() == "content blogs":
        df.at[index, "Scores"] += weight6 * 50
    elif row["Lead Source Name"].lower() == "signup pages" or row["Lead Source Name"].lower() == "exhibitions":
        df.at[index, "Scores"] += weight6 * 100
    else:
        df.at[index, "Scores"] += weight6 * -10

def designation(index, row, df):
    if row["Contact person Designation"].lower() == "ceo" or row["Contact person Designation"].lower() == "sales" or row["Contact person Designation"].lower() == "director" \
        or row["Contact person Designation"].lower() == "logistics":
        df.at[index, "Scores"] += weight7 * 100
    elif row["Contact person Designation"].lower() == "executive" or row["Contact person Designation"].lower() == "secretary":
        df.at[index, "Scores"] += weight7 * 80
    elif row["Contact person Designation"].lower() == "technician":
        df.at[index, "Scores"] += weight7 * 50
    else:
        df.at[index, "Scores"] += weight7 * 0

def negative_score(index, row, df):
    if not pd.isna(row["Competitors"]):
        df.at[index, "Scores"] += 1 * -100
    else:
        df.at[index, "Scores"] += 1 * 0
    if not pd.isna(row["Contact Person Email"]) and not pd.isna(row["Contact Person Phone"]):
        df.at[index, "Scores"] += 1 * 0
    elif pd.isna(row["Contact Person Email"]) and pd.isna(row["Contact Person Phone"]):
        df.at[index, "Scores"] += 1 * -20
    else:
        df.at[index, "Scores"] += 1 * -10

def scores(df):
    for index, row in df.iterrows():
        if pd.isna(row["Scores"]):
            df.at[index, "Scores"] = 0
            if not pd.isna(row["Industry"]):
                Industry(index, row, df)
            else:
                df.at[index, "Scores"] += weight1 * 0
            if not pd.isna(row["Last Created"]):
                last_created(index, row, df)
            else:
                df.at[index, "Scores"] += weight2 * 0
            if not pd.isna(row["Employee Count"]):
                employee(index, row, df)
            else:
                df.at[index, "Scores"] += weight3 * 0
            if not pd.isna(row["Total Potential Revenue/Month"]):
                revenue(index, row, df)
            else:
                df.at[index, "Scores"] += weight4 * 0
            if not pd.isna(row["Physical Channel"]):
                channel(index, row, df)
            else:
                df.at[index, "Scores"] += weight5 * 0
            if not pd.isna(row["Lead Source Name"]):
                source(index, row, df)
            else:
                df.at[index, "Scores"] += weight6 * 0
            if not pd.isna(row["Contact person Designation"]):
                designation(index, row, df)
            else:
                df.at[index, "Scores"] += weight7 * 0
            negative_score(index, row, df)
        
def weightedscore(df):
    # change the variable inside revenue column from str to decimal
    curr = [] * len(df.index)
    for index, row in df.iterrows():
        if isinstance(row["Total Potential Revenue/Month"], str) and not pd.isna(row["Total Potential Revenue/Month"]):
            curr = df.at[index, "Total Potential Revenue/Month"]
            value = Decimal(sub(r'[^\d.]', '', curr))
            df.at[index, "Total Potential Revenue/Month"] = value
    # insert a new column for current date
    today_date = date.today()
    df.insert(3, 'Today Date', today_date)
    # insert a new column for difference between current and suspect created date
    diff = (pd.to_datetime(df["Today Date"]) - pd.to_datetime(df["Suspect Creation date by Lead Originator"])).dt.days
    df.insert(5, "Last Created", diff)
    # scoring
    scores(df)
    margin(df)
    sorted_df = df.sort_values("Scores", ascending=False)
    return (sorted_df)
    
def main():
    df = pd.read_excel(
        "/home/ssyazz/python/group/Scoring.xlsx", sheet_name="a")
    sorted_scored = weightedscore(df)
    print(sorted_scored)
    sorted_scored.to_csv("/home/ssyazz/python/group/new.csv", index=False)

main()
