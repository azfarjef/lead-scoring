import pandas as pd
import sys

def search(unique_id, source):
    try:
        df = pd.read_csv(source)
    except FileNotFoundError:
        print(f"{source} not found")
        return
    ret_df = pd.DataFrame(
        {
            "customer name": [],
            "Address": [],
            "City": [],
            "Business Nature": []
        }
    )

    for index, row in df.iterrows():
        if unique_id in row["customer name"].lower():
            temp = df.iloc[[index], :]
            ret_df = pd.merge(ret_df, temp, how="outer")
    print(ret_df)
    if ret_df.empty:
        error = "No results"
        print(error)
        return error 
    ret_df.to_csv("search_result.csv", index=False)

"""
ret_df = df.iloc[[int(sys.argv[2])], :]
ret_df.to_csv("search_result.csv", index=False)
print(ret_df)
"""
