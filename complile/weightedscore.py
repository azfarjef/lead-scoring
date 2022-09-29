import pandas as pd
from re import sub
from decimal import Decimal
from datetime import date
from margin import margin
from unique_gen import unique

weight1 = 0.3   # Industry
weight2 = 0.15  # Suspect creation date
weight3 = 0.1   # Employee count
weight4 = 0.1   # Total potential revenue
weight5 = 0.05  # Physical channel
weight6 = 0.1   # Lead source
weight7 = 0.2   # contact person designation


def industry(index, row, df):
    if row["industry"].lower() == "consumer" or row["industry"].lower() == "retail":
        df.at[index, "lead priority level"] += weight1 * 100
    elif row["industry"].lower() == "chemical and energy" or row["industry"].lower() == "technology" or row["industry"].lower() == "service logistics" \
            or row["industry"].lower() == "manufacturing" or row["industry"].lower() == "distributor":
        df.at[index, "lead priority level"] += weight1 * 80
    elif row["industry"].lower() == "life sciences and healthcare":
        df.at[index, "lead priority level"] += weight1 * 60
    else:
        df.at[index, "lead priority level"] += weight1 * 40

def last_created(index, row, df):
    if row["Last Created"] < 10:
        df.at[index, "lead priority level"] += weight2 * 100
    elif row["Last Created"] >= 10 and row["Last Created"] < 31:
        df.at[index, "lead priority level"] += weight2 * 50
    elif row["Last Created"] >= 31 and row["Last Created"] < 90:
        df.at[index, "lead priority level"] += weight2 * -50
    else:
        df.at[index, "lead priority level"] += weight2 * -100

def	employee(index, row, df):
	if row["employee count"] > 100:
		df.at[index, "lead priority level"] += weight3 * 100
	elif row["employee count"] <= 100 and row["employee count"] > 50:
		df.at[index, "lead priority level"] += weight3 * 50
	elif row["employee count"] <= 50:
		df.at[index, "lead priority level"] += weight3 * 20

def revenue(index, row, df):
    if row["total potential revenue/month"] > 1000:
        df.at[index, "lead priority level"] += weight4 * 100
    elif row ["total potential revenue/month"] > 500 and row["total potential revenue/month"] <= 1000:
        df.at[index, "lead priority level"] += weight4 * 80
    elif row["total potential revenue/month"] > 100 and row["total potential revenue/month"] <= 500:
        df.at[index, "lead priority level"] += weight4 * 50
    else:
        df.at[index, "lead priority level"] += weight4 * 20

def channel(index, row, df):
    if row["physical channel"].lower() == "b2b":
        df.at[index, "lead priority level"] += weight5 * 100
    elif row["physical channel"].lower() == "b2c":
        df.at[index, "lead priority level"] += weight5 * 80
    else:
        df.at[index, "lead priority level"] += weight5 * -50

def source(index, row, df):
    if row["lead source name"].lower() == "facebook" or row["lead source name"].lower() == "twitter":
        df.at[index, "lead priority level"] += weight6 * 70
    elif row["lead source name"].lower() == "ex database" or row["lead source name"].lower() == "content blogs":
        df.at[index, "lead priority level"] += weight6 * 50
    elif row["lead source name"].lower() == "signup pages" or row["lead source name"].lower() == "exhibitions":
        df.at[index, "lead priority level"] += weight6 * 100
    else:
        df.at[index, "lead priority level"] += weight6 * -10

def designation(index, row, df):
    if row["contact person designation"].lower() == "ceo" or row["contact person designation"].lower() == "sales" or row["contact person designation"].lower() == "director" \
        or row["contact person designation"].lower() == "logistics":
        df.at[index, "lead priority level"] += weight7 * 100
    elif row["contact person designation"].lower() == "executive" or row["contact person designation"].lower() == "secretary":
        df.at[index, "lead priority level"] += weight7 * 80
    elif row["contact person designation"].lower() == "technician":
        df.at[index, "lead priority level"] += weight7 * 50
    else:
        df.at[index, "lead priority level"] += weight7 * 0

def negative_score(index, row, df):
    if not pd.isna(row["competitors"]):
        df.at[index, "lead priority level"] += 1 * -100
    else:
        df.at[index, "lead priority level"] += 1 * 0
    if not pd.isna(row["contact person email"]) and not pd.isna(row["contact person phone"]):
        df.at[index, "lead priority level"] += 1 * 0
    elif pd.isna(row["contact person email"]) and pd.isna(row["contact person phone"]):
        df.at[index, "lead priority level"] += 1 * -20
    else:
        df.at[index, "lead priority level"] += 1 * -10

def scores(df):
    for index, row in df.iterrows():
        if pd.isna(row["lead priority level"]):
            df.at[index, "lead priority level"] = 0
            if "industry" in df.columns:
                if not pd.isna(row["industry"]):
                    industry(index, row, df)
                else:
                    df.at[index, "lead priority level"] += weight1 * 0
            if "Last Created" in df.columns:
                if not pd.isna(row["Last Created"]):
                   last_created(index, row, df)
                else:
                    df.at[index, "lead priority level"] += weight2 * 0
            if "employee count" in df.columns:
                if not pd.isna(row["employee count"]):
                    employee(index, row, df)
                else:
                    df.at[index, "lead priority level"] += weight3 * 0
            if "total potential revenue/month" in df.columns:
                if not pd.isna(row["total potential revenue/month"]):
                    revenue(index, row, df)
                else:
                    df.at[index, "lead priority level"] += weight4 * 0
            if "physical channel" in df.columns:
                if not pd.isna(row["physical channel"]):
                    channel(index, row, df)
                else:
                    df.at[index, "lead priority level"] += weight5 * 0
            if "lead source name" in df.columns:
                if not pd.isna(row["lead source name"]):
                    source(index, row, df)
                else:
                    df.at[index, "lead priority level"] += weight6 * 0
            if "contact person designation" in df.columns:
                if not pd.isna(row["contact person designation"]):
                    designation(index, row, df)
                else:
                    df.at[index, "lead priority level"] += weight7 * 0
            negative_score(index, row, df)
        
def cleaning(df):
    df.reset_index(inplace=True)
    if 'Unnamed: 0' in df.columns:
        df = df.drop('Unnamed: 0', axis = 1)
    if 'index' in df.columns:
        df = df.drop('index', axis = 1)
    return (df)

def weightedscore(df):
    df = cleaning(df)
    # change the variable inside revenue column from str to decimal
    curr = [] * len(df.index)
    for index, row in df.iterrows():
        if isinstance(row["total potential revenue/month"], str) and not pd.isna(row["total potential revenue/month"]):
            curr = df.at[index, "total potential revenue/month"]
            value = Decimal(sub(r'[^\d.]', '', curr))
            df.at[index, "total potential revenue/month"] = value
    # insert a new column for current date
    today_date = date.today()
    df.insert(3, 'Today Date', today_date)
    # insert a new column for difference between current and suspect created date
    diff = (pd.to_datetime(df["Today Date"]) - pd.to_datetime(df["suspect creation date by lead originator"])).dt.days
    df.insert(5, "Last Created", diff)
    # scoring
    scores(df)
    margin(df)
    sorted_df = df.sort_values("lead priority level", ascending=False)
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
