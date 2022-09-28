import	pandas as pd

df = pd.read_excel("/home/ssyazz/python/group/Scoring.xlsx", sheet_name = "b")

def	unique_id(df):
    df['unique lead assignment number '] = df.groupby(['customer name']).ngroup()
    return (df)
    
def	new_unique_id(df):
    sorted = df.sort_values(by = ["unique Lead assignment number ", "Customer Name"])
    sorted["unique Lead assignment number "] = sorted.groupby(['Customer Name'])["unique Lead assignment number "].transform("max")
    sorted["unique Lead assignment number "] = sorted["unique Lead assignment number "].fillna(sorted["unique Lead assignment number "].isna().cumsum() + sorted["unique Lead assignment number "].max())
    sorted_final = sorted.sort_values(by = ["unique Lead assignment number ", "Customer Name"])
    df = sorted_final
    df = df.astype({"unique Lead assignment number " : "int"})
    return(df)

def	main():
    #f = unique_id(df)
    f = new_unique_id(df)
    print(f)
    print(type(f.at[1, "unique Lead assignment number "]))

if __name__ == "__main__":    
    main()