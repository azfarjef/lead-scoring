import pandas as pd
import numpy as np

def unique(df, col):
    if df[col["unique_id"]].replace(r'^\s*$', np.nan, regex=True).isna().all():
        df = unique_id(df, col)
        return (df)
    else:
        df = new_unique_id(df, col)
        return (df)

def	unique_id(df, col):
    df[col["unique_id"]] = df.groupby([col["name"]]).ngroup()
    return (df)
    
def new_unique_id_small(df, col):
    sorted = df.sort_values(by = [col["unique_id"], col["name"]])
    sorted[col["unique_id"]] = sorted.groupby([col["name"]])[col["unique_id"]].transform("max")
    sorted[col["unique_id"]] = sorted[col["unique_id"]].fillna(sorted[col["unique_id"]].isna().cumsum() + sorted[col["unique_id"]].max())
    return (sorted)

def	new_unique_id(df, col):
    df_drop_dup = df.drop_duplicates(subset = [col["unique_id"], col["name"]], keep = 'last').reset_index(drop = True)
    duplicates = df.loc[df.duplicated(subset = [col["unique_id"], col["name"]])]
    sorted = new_unique_id_small(df_drop_dup, col)
    frames = [sorted, duplicates]
    result = pd.concat(frames)
    sorted = new_unique_id_small(result, col)
    sorted_final = sorted.sort_values(by = [col["unique_id"], col["name"]])
    df = sorted_final
    df = df.astype({col["unique_id"] : "int"})
    return (df)

def	main():
    #f = unique_id(df)
    df = pd.read_excel("/home/ssyazz/python/group/Scoring.xlsx", sheet_name = "b")
    f = new_unique_id(df)
    print(f)
    print(type(f.at[1]))#, col["unique_id"]]))

if __name__ == "__main__":    
    main()
