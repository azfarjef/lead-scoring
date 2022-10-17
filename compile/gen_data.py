import pandas as pd
from utils import merge_data
from processdata import process_data
from output import output_data
from weightedscore import weightedscore
from unique_gen import unique
from tkinter import messagebox

def gen_data(sources, output):
    col = get_col_name()
    df = merge_data(sources, output, col)
    # df.to_csv("aftermerge.csv", index=False)
    print(df.columns)
    df, df_full = process_data(df, col)
    # df = unique(df, col)
    df = weightedscore(df, col)
    output_data([df_full], df, output)
    messagebox.showinfo("Successful", "file has been generated")
        
    # df.to_csv(output + ".csv", index=False)

def get_col_name():
    col = {
        "unique_id" : "",
        "lead_source" : "",
        "lead_source_details" : "",
        "created_date" : "",
        "created_name" : "",
        "name" : "",
        "address1" : "",
        "address2" : "",
        "city" : "",
        "state" : "",
        "postcode" : "",
        "main_phone" : "",
        "contact_name" : "",
        "contact_email" : "",
        "contact_designation" : "",
        "contact_phone" : "",
        "website" : "",
        "physical_channel" : "",
        "ssm_no" : "",
        "competitor" : "",
        "revenue" : "",
        "industry" : "",
        "suspect_accepted_by" : "",
        "prospect_accepted_by" : "",
        "source_type" : "",
        "score" : "",
        "employee_count" : "",
    }

    columns = []
    cf = pd.read_csv("data/columns.csv")
    for index, row in cf.iterrows():
        columns.append(row.item())

    for i, key in enumerate(col):
        col[key] = columns[i]

    return col

# gen_data("data/D.csv data/E.csv", "results")
