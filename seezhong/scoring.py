import pandas as pd
from scoring_utils import scores

def scoring(df, output):
    df["Scores"] = 0
    """
    scores(df)
    """
    sorted_df = df.sort_values("Scores", ascending=False)
    print(sorted_df)
    sorted_df.to_csv(output, index=False)
