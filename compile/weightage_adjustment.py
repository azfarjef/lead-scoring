import pandas as pd

def get_industry():
    col = {
        "weightage" : ["", ""],
        "consumer" : ["", ""],
        "retail" : ["", ""],
        "technology" : ["", ""],
        "service_logistics" : ["", ""],
        "manufacturing" : ["", ""],
        "chemical" : ["", ""],
        "distributor" : ["", ""],
        "life_sciences" : ["", ""],
        "automotive" : ["", ""],
        "engineering" : ["", ""],
        "service" : ["", ""]
    }
    column = []
    columns = []
    cf = pd.read_excel("data/weighted_adjustment.xlsx", sheet_name = "industry")
    for index, row in cf.iterrows():
        column.append(row["type"])
    for index, row in cf.iterrows():
        columns.append(row["numeric"])
    
    for i, key in enumerate(col):
        col[key] = [column[i], columns[i]]
    return col

def get_channel():
    col = {
        "weightage": ["", ""],
        "b2b" : ["", ""],
        "b2c" : ["", ""]
    }
    column = []
    columns = []
    cf = pd.read_excel("data/weighted_adjustment.xlsx", sheet_name = "physical_channel")
    for index, row in cf.iterrows():
        column.append(row["type"])
    for index, row in cf.iterrows():
        columns.append(row["numeric"])
    
    for i, key in enumerate(col):
        col[key] = [column[i], columns[i]]
    return col

def get_source():
    col = {
        "weightage": ["", ""],
        "FB" : ["", ""],
        "twitter" : ["", ""],
        "ex_database" : ["", ""],
        "content_blog" : ["", ""],
        "signup_pages" : ["", ""],
        "exhibition" : ["", ""],
        "market" : ["", ""]
    }
    column = []
    columns = []
    cf = pd.read_excel("data/weighted_adjustment.xlsx", sheet_name = "lead_source")
    for index, row in cf.iterrows():
        column.append(row["type"])
    for index, row in cf.iterrows():
        columns.append(row["numeric"])
    
    for i, key in enumerate(col):
        col[key] = [column[i], columns[i]]
    return col

def get_designation():
    col = {
        "weightage": ["", ""],
        "CEO" : ["", ""],
        "sales" : ["", ""],
        "logistics" : ["", ""],
        "executive" : ["", ""],
        "technician" : ["", ""],
        "secretary" : ["", ""],
        "cleaner" : ["", ""],
        "director" : ["", ""]
    }
    column = []
    columns = []
    cf = pd.read_excel("data/weighted_adjustment.xlsx", sheet_name = "designation")
    for index, row in cf.iterrows():
        column.append(row["type"])
    for index, row in cf.iterrows():
        columns.append(row["numeric"])
    
    for i, key in enumerate(col):
        col[key] = [column[i], columns[i]]
    return col