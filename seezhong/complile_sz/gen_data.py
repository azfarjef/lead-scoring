import pandas as pd
from utils import merge_data
from processdata import process_data
from output import output_data
from weightedscore import weightedscore
from unique_gen import unique

def gen_data(sources, output):
    df = merge_data(sources, output)
    df, df_full = process_data(df)
    output_data([df_full], df)
    df = unique(df)
    df = weightedscore(df)
    df.to_csv(output + ".csv", index=False)
