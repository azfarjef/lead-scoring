import pandas as pd

def read_data(source):
    try:
        df = pd.read_excel(source) #sheet_name="")
    except FileNotFoundError:
        print(f"{source} not found")
    return df

def find_and_merge_data(unique_id, df, ret_df):
    for index, row in df.iterrows():
        if unique_id in row["Customer Name"].lower():
            temp = df.iloc[[index], :]
            ret_df = pd.merge(ret_df, temp, how="outer")
    print(ret_df)
    if ret_df.empty:
        error = "No results"
        print(error)
    return ret_df

def search(unique_id, source):
    ret_df = pd.DataFrame(
            {
                "Customer Name": [],
                "Address": [],
                "City": [],
                "Business Nature": []
            }
    )
    try:
        df = read_data(source)
    except:
        return
    ret_df = find_and_merge_data(unique_id, df, ret_df) 
    ret_df.to_csv("search_result.csv", index=False)
