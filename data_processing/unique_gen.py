import	pandas as pd

df = pd.read_excel("/home/ssyazz/python/group/Scoring.xlsx", sheet_name = "b")

def	unique_id(df):
    df['Unique ID'] = df.groupby(['Customer Name']).ngroup()
    return (df)
    
def	new_unique_id(df):
    sorted = df.sort_values(by = ["Unique ID", "Customer Name"])
    sorted["Unique ID"] = sorted.groupby(['Customer Name'])["Unique ID"].transform("max")
    sorted["Unique ID"] = sorted["Unique ID"].fillna(sorted["Unique ID"].isna().cumsum() + sorted["Unique ID"].max())
    sorted_final = sorted.sort_values(by = ["Unique ID", "Customer Name"])
    df = sorted_final
    df = df.astype({"Unique ID" : "int"})
    return(df)

def	main():
    #f = unique_id(df)
    f = new_unique_id(df)
    print(f)
    print(type(f.at[1, "Unique ID"]))
    
main()
