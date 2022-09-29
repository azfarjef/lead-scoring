import	pandas as pd
import  numpy as np

#df = pd.read_excel("/home/ssyazz/python/group/Scoring.xlsx", sheet_name = "b")

def	unique_id(df):
    df.columns = map(str.lower, df.columns)
    df['unique lead assignment number '] = df.groupby(['customer name']).ngroup()
    return (df)
    
def	new_unique_id(df):
    df.columns = map(str.lower, df.columns)
    sorted = df.sort_values(by = ["unique lead assignment number ", "customer name"])
    sorted["unique lead assignment number "] = sorted.groupby(['customer name'])["unique lead assignment number "].transform("max")
    sorted["unique lead assignment number "] = sorted["unique lead assignment number "].fillna(sorted["unique lead assignment number "].isna().cumsum() + sorted["unique lead assignment number "].max())
    sorted_final = sorted.sort_values(by = ["unique lead assignment number ", "customer name"])
    df = sorted_final
    df = df.astype({"unique lead assignment number " : "int"})
    return(df)

def unique(df):
    df.columns = map(str.lower, df.columns)
    if df['unique lead assignment number '].replace(r'^\s*$', np.nan, regex=True).isna().all():
        df = unique_id(df)
        return(df)
    else:
        df = new_unique_id(df)
        return (df)

def	main():
    #f = unique_id(df)
    f = new_unique_id(df)
    print(f)
    print(type(f.at[1, "unique lead assignment number "]))

if __name__ == "__main__":    
    main()
