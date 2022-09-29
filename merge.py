import pandas as pd
import sys

def main():
    data = []
    columns = ["Customer Name", "address", "city", "business nature"]

    i = 1
    while i < len(sys.argv):
        data.append(sys.argv[i])
        i += 1

    i = 0
    while i < len(data) - 1:
        if i == 0:
            df1 = pd.read_csv(data[i])
        else:
            df1 = merged_df
        df2 = pd.read_csv(data[i + 1])
        merged_df = pd.merge(df1, df2, how="outer")
        i += 1

    for column in merged_df.columns:
        if column.lower() in columns:
            continue
        merged_df = merged_df.drop(column, axis=1)
    print(merged_df)
    merged_df.to_csv("output.csv")

    """
    df = pd.DataFrame({
        "Customer Name": [],
        "address": [],
        "city": [],
        "Business Nature": []
    })

    i = 0
    while i < len(data):
        df2 = pd.read_csv(data[i])
        df2 = df2.rename(columns=str.lower)
        merged_df = pd.merge(df, df2[columns], how="outer")
        df = merged_df
        i += 1
    merged_df.to_csv("output.csv")
    print(merged_df)
    """

if __name__ == "__main__":
    main()
