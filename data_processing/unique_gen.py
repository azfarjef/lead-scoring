import	pandas as pd

df = pd.read_excel("/home/ssyazz/python/group/Scoring.xlsx", sheet_name = "b")

def	unique_id(df):
    df['Unique ID'] = df.groupby(['Customer Name']).ngroup()
    
def	new_unique_id(df):
    sorted = df.sort_values(by = ["Unique ID", "Customer Name"])
    sorted["Unique ID"] = sorted["Unique ID"].fillna(sorted["Unique ID"].isna().cumsum() + sorted["Unique ID"].max())
    df = sorted
    df = df.astype({"Unique ID" : "int"})
    return(df)
    
def	main():
    print(new_unique_id(df))
    print(type(df.at[1, "Unique ID"]))
    
main()
#results = df.head(20)
# print(results)