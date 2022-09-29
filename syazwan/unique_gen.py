from sqlite3 import DatabaseError
import	pandas as pd
import  numpy as np

df = pd.read_excel("/home/ssyazz/python/group/Scoring.xlsx", sheet_name = "b")

def	unique_id(df):
    df['Unique Lead Assignment Number '] = df.groupby(['Customer Name']).ngroup()
    return (df)
    
def	new_unique_id(df):
    sorted = df.sort_values(by = ["Unique Lead Assignment Number ", "Customer Name"])
    sorted["Unique Lead Assignment Number "] = sorted.groupby(['Customer Name'])["Unique Lead Assignment Number "].transform("max")
    sorted["Unique Lead Assignment Number "] = sorted["Unique Lead Assignment Number "].fillna(sorted["Unique Lead Assignment Number "].isna().cumsum() + sorted["Unique Lead Assignment Number "].max())
    sorted_final = sorted.sort_values(by = ["Unique Lead Assignment Number ", "Customer Name"])
    df = sorted_final
    df = df.astype({"Unique Lead Assignment Number " : "int"})
    return(df)

def unique(df):
    if df['Unique Lead Assignment Number '].replace(r'^\s*$', np.nan, regex=True).isna().all():
        unique_id(df)
        return(df)
    else:
        new_unique_id(df)
        return (df)

def	main():
    #f = unique_id(df)
    f = new_unique_id(df)
    print(f)
    print(type(f.at[1, "Unique Lead Assignment Number "]))

if __name__ == "__main__":    
    main()