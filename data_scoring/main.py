import pandas as pd
from scoring import scores

def main():
    df = pd.read_excel("/home/ssyazz/python/group/sample_lead_generation_database.xlsx", sheet_name = "sample_lead_generation_database")
    df["Scores"] = 0
    scores(df)
    sorted_df = df.sort_values("Scores", ascending=False)
    print(sorted_df)
    sorted_df.to_csv("/home/ssyazz/python/group/sample_lead_generation_database.csv", index=False)

if __name__ == "__main__":
    main()