import pandas as pd
from re import sub
from decimal import Decimal
from datetime import date
from margin import margin
from unique_gen import unique
import numpy as np

weight1 = 0.3   # Industry
weight2 = 0.15  # Suspect creation date
weight3 = 0.1   # Employee count
weight4 = 0.1   # Total potential revenue
weight5 = 0.05  # Physical channel
weight6 = 0.1   # Lead source
weight7 = 0.2   # contact person designation


def industry(index, row, df, col):
    if row[col["industry"]].lower() == "consumer" or row[col["industry"]].lower() == "retail":
        df.at[index, col["score"]] += weight1 * 100
    elif row[col["industry"]].lower() == "chemical and energy" or row[col["industry"]].lower() == "technology" or row[col["industry"]].lower() == "service logistics" \
            or row[col["industry"]].lower() == "manufacturing" or row[col["industry"]].lower() == "distributor":
        df.at[index, col["score"]] += weight1 * 80
    elif row[col["industry"]].lower() == "life sciences and healthcare":
        df.at[index, col["score"]] += weight1 * 60
    else:
        df.at[index, col["score"]] += weight1 * 40

def last_created(index, row, df, col):
    if row["Last Created"] < 10:
        df.at[index, col["score"]] += weight2 * 100
    elif row["Last Created"] >= 10 and row["Last Created"] < 31:
        df.at[index, col["score"]] += weight2 * 50
    elif row["Last Created"] >= 31 and row["Last Created"] < 90:
        df.at[index, col["score"]] += weight2 * -50
    else:
        df.at[index, col["score"]] += weight2 * -100

def	employee(index, row, df, col):
	if row[col["employee_count"]] > 100:
		df.at[index, col["score"]] += weight3 * 100
	elif row[col["employee_count"]] <= 100 and row[col["employee_count"]] > 50:
		df.at[index, col["score"]] += weight3 * 50
	elif row[col["employee_count"]] <= 50:
		df.at[index, col["score"]] += weight3 * 20

def revenue(index, row, df, col):
    if row[col["revenue"]] > 1000:
        df.at[index, col["score"]] += weight4 * 100
    elif row [col["revenue"]] > 500 and row[col["revenue"]] <= 1000:
        df.at[index, col["score"]] += weight4 * 80
    elif row[col["revenue"]] > 100 and row[col["revenue"]] <= 500:
        df.at[index, col["score"]] += weight4 * 50
    else:
        df.at[index, col["score"]] += weight4 * 20

def channel(index, row, df, col):
    if row[col["physical_channel"]].lower() == "b2b":
        df.at[index, col["score"]] += weight5 * 100
    elif row[col["physical_channel"]].lower() == "b2c":
        df.at[index, col["score"]] += weight5 * 80
    else:
        df.at[index, col["score"]] += weight5 * -50

def source(index, row, df, col):
    if row[col["lead_source"]].lower() == "facebook" or row[col["lead_source"]].lower() == "twitter":
        df.at[index, col["score"]] += weight6 * 70
    elif row[col["lead_source"]].lower() == "ex database" or row[col["lead_source"]].lower() == "content blogs":
        df.at[index, col["score"]] += weight6 * 50
    elif row[col["lead_source"]].lower() == "signup pages" or row[col["lead_source"]].lower() == "exhibitions":
        df.at[index, col["score"]] += weight6 * 100
    else:
        df.at[index, col["score"]] += weight6 * -10

def designation(index, row, df, col):
    if row[col["contact_designation"]].lower() == "ceo" or row[col["contact_designation"]].lower() == "sales" or row[col["contact_designation"]].lower() == "director" \
        or row[col["contact_designation"]].lower() == "logistics":
        df.at[index, col["score"]] += weight7 * 100
    elif row[col["contact_designation"]].lower() == "executive" or row[col["contact_designation"]].lower() == "secretary":
        df.at[index, col["score"]] += weight7 * 80
    elif row[col["contact_designation"]].lower() == "technician":
        df.at[index, col["score"]] += weight7 * 50
    else:
        df.at[index, col["score"]] += weight7 * 0

def negative_score(index, row, df, col):
    if not pd.isna(row[col["competitor"]]):
        df.at[index, col["score"]] += 1 * -100
    else:
        df.at[index, col["score"]] += 1 * 0
    if not pd.isna(row[col["contact_email"]]) and not pd.isna(row[col["contact_phone"]]):
        df.at[index, col["score"]] += 1 * 0
    elif pd.isna(row[col["contact_email"]]) and pd.isna(row[col["contact_phone"]]):
        df.at[index, col["score"]] += 1 * -20
    else:
        df.at[index, col["score"]] += 1 * -10

def scores(df, col):
    for index, row in df.iterrows():
        if pd.isna(row[col["score"]]):
            df.at[index, col["score"]] = 0
            if col["industry"] in df.columns:
                if not pd.isna(row[col["industry"]]):
                    industry(index, row, df, col)
                else:
                    df.at[index, col["score"]] += weight1 * 0
            if "Last Created" in df.columns:
                if not pd.isna(row["Last Created"]):
                   last_created(index, row, df, col)
                else:
                    df.at[index, col["score"]] += weight2 * 0
            if col["employee_count"] in df.columns:
                if not pd.isna(row[col["employee_count"]]):
                    employee(index, row, df, col)
                else:
                    df.at[index, col["score"]] += weight3 * 0
            if col["revenue"] in df.columns:
                if not pd.isna(row[col["revenue"]]):
                    revenue(index, row, df, col)
                else:
                    df.at[index, col["score"]] += weight4 * 0
            if col["physical_channel"] in df.columns:
                if not pd.isna(row[col["physical_channel"]]):
                    channel(index, row, df, col)
                else:
                    df.at[index, col["score"]] += weight5 * 0
            if col["lead_source"] in df.columns:
                if not pd.isna(row[col["lead_source"]]):
                    source(index, row, df, col)
                else:
                    df.at[index, col["score"]] += weight6 * 0
            if col["contact_designation"] in df.columns:
                if not pd.isna(row[col["contact_designation"]]):
                    designation(index, row, df, col)
                else:
                    df.at[index, col["score"]] += weight7 * 0
            negative_score(index, row, df, col)
        
def cleaning(df):
    df.reset_index(inplace=True)
    if 'Unnamed: 0' in df.columns:
        df = df.drop('Unnamed: 0', axis = 1)
    if 'index' in df.columns:
        df = df.drop('index', axis = 1)
    return (df)

def put_last(df, col):
    cols_at_end = [col["source_type"], col["score"]]
    df = df[[c for c in df if c not in cols_at_end]
            + [c for c in cols_at_end if c in df]]
    return (df)

def weightedscore(df, col):
    df = cleaning(df)
    # change the variable inside revenue column from str to decimal
    curr = [] * len(df.index)
    for index, row in df.iterrows():
        if isinstance(row[col["revenue"]], str) and not pd.isna(row[col["revenue"]]):
            curr = df.at[index, col["revenue"]]
            value = Decimal(sub(r'[^\d.]', '', curr))
            df.at[index, col["revenue"]] = value
    # insert a new column for current date
    today_date = date.today()
    df.insert(3, 'Today Date', today_date)
    # insert a new column for difference between current and suspect created date
    diff = (pd.to_datetime(df["Today Date"]) - pd.to_datetime(df[col["created_date"]])).dt.days
    df.insert(5, "Last Created", diff)
    # scoring
    scores(df, col)
    margin(df, col)
    df = put_last(df, col)
    sorted_df = df.sort_values(col["score"], ascending=False)
    return (sorted_df)
    
def main():
    df = pd.read_csv(
        "/home/ssyazz/python/group/merge.csv")
    df = unique(df)
    sorted_scored = weightedscore(df)
    print(sorted_scored)
    sorted_scored.to_csv("/home/ssyazz/python/group/new.csv", index = False)

if __name__ == "__main__":    
    main()
