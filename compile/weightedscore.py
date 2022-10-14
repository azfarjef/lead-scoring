import pandas as pd
import numpy as np
import re
from margin import margin
from unique_gen import unique
from weightage_adjustment import get_info
from weighted_utils import cleaning, str_to_dec, diff_date, put_last

weight2 = 0.15  # Suspect creation date
weight3 = 0.1   # Employee count
weight4 = 0.1   # Total potential revenue

def get_score(row, name, cols):
    other = dict((k, cols[k]) for k in ['Others']
        if k in cols)
    for key, value in cols.items():
        if row[name].lower().strip() == value[0].lower().strip():
            return (value[1])
    other = np.array(other.get("Others"))
    if not pd.isna(other).all():
        if not pd.isna(row[name]) and other[0] == "Others":
            val = int(float(other[1]))
            return (val)
    return (0)

def contact_scores(row, name, col, cols):
    full = np.array(cols.get("Have both"))
    phone = np.array(cols.get("Null phone no."))
    null = np.array(cols.get("All Null"))
    email = np.array(cols.get("Null email"))
    if full[1] != "nan" and phone[1] != "nan" and null[1] != "nan" and email[1] != "nan":
        if not pd.isna(row[name]):
            row[name] = str(row[name])
            if ("-" in row[name] or "+" in row[name] or '"' in row[name] or re.search(r'\d', row[name])) and not pd.isna(row[col["contact_email"]]):
                if len(row[name]) >= 8 and len(row[name]) <= 17:
                    val = int(float(full[1]))
                    return (val)
                else:
                    val = int(float(phone[1]))
                    return (val)
            elif not pd.isna(row[col["contact_email"]]):
                val = int(float(phone[1]))
                return (val)
            elif ("-" in row[name] or "+" in row[name] or '"' in row[name] or re.search(r'\d', row[name])) and pd.isna(row[col["contact_email"]]):
                if len(row[name]) >= 8 and len(row[name]) <= 17:
                    val = int(float(email[1]))
                    return (val)
                else:
                    val = int(float(null[1]))
                    return (val)
        elif not pd.isna(row[col["contact_email"]]):
            val = int(float(phone[1]))
            return (val)
        else:
            val = int(float(null[1]))
            return (val)
    return (0)

def industry(index, row, df, col, cols):
    if col["industry"] in df.columns:
        if not pd.isna(row[col["industry"]]):
            score = get_score(row, col["industry"], cols)
            df.at[index, col["score"]] += cols["weightage"][1] * score
        else:
            df.at[index, col["score"]] += cols["weightage"][1] * 0

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

def channel(index, row, df, col, cols):
    if col["physical_channel"] in df.columns:
        # cols = get_channel()
        if not pd.isna(row[col["physical_channel"]]):
            score = get_score(row, col["physical_channel"], cols)
            if (score == 0):
                score = -50
            df.at[index, col["score"]] += cols["weightage"][1] * score
        else:
            df.at[index, col["score"]] += cols["weightage"][1] * 0

def channel(index, row, df, col, cols):
    if col["physical_channel"] in df.columns:
        if not pd.isna(row[col["physical_channel"]]):
            score = get_score(row, col["physical_channel"], cols)
            df.at[index, col["score"]] += cols["weightage"][1] * score
        else:
            df.at[index, col["score"]] += cols["weightage"][1] * 0

def source(index, row, df, col, cols):
    if col["lead_source"] in df.columns:
        if not pd.isna(row[col["lead_source"]]):
            score = get_score(row, col["lead_source"], cols)
            df.at[index, col["score"]] += cols["weightage"][1] * score
        else:
            df.at[index, col["score"]] += cols["weightage"][1] * 0

def designation(index, row, df, col, cols):
    if col["contact_designation"] in df.columns:
        if not pd.isna(row[col["contact_designation"]]):
            score = get_score(row, col["contact_designation"], cols)
            df.at[index, col["score"]] += cols["weightage"][1] * score
        else:
            df.at[index, col["score"]] += cols["weightage"][1] * 0
            
def competitor(index, row, df, col, cols):
    if col["competitor"] in df.columns:
        if not pd.isna(row[col["competitor"]]):
            score = get_score(row, col["competitor"], cols)
            df.at[index, col["score"]] += cols["weightage"][1] * score
        else:
            df.at[index, col["score"]] += cols["weightage"][1] * 0

def negative_score(index, row, df, col, cols):
    score = contact_scores(row, col["contact_phone"], col, cols)
    df.at[index, col["score"]] += cols["weightage"][1] * score

def scores(df, col):
    cols_industry = get_info("industry")
    cols_channel = get_info("physical_channel")
    cols_source = get_info("lead_source")
    cols_designation = get_info("designation")
    cols_competitor = get_info("competitor")
    cols_negative = get_info("negative_score")
    for index, row in df.iterrows():
        if pd.isna(row[col["score"]]):
            df.at[index, col["score"]] = 0
            industry(index, row, df, col, cols_industry)
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
            channel(index, row, df, col, cols_channel)
            source(index, row, df, col, cols_source)
            designation(index, row, df, col, cols_designation)
            competitor(index, row, df, col, cols_competitor)
            negative_score(index, row, df, col, cols_negative)

def weightedscore(df, col):
    df = cleaning(df)
    # change the variable inside revenue column from str to decimal
    df = str_to_dec(df, col["revenue"])
    df = str_to_dec(df, col["employee_count"])
    # df = str_to_dec(df, col["created_date"])
    # insert a new column for current date and calculate the difference with last_created
    diff_date(df, col)
    # scoring
    scores(df, col)
    margin(df, col)
    df = put_last(df, col)
    print(df)
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
