import pandas as pd
from utils import merge_data
from processdata import process_data
from output import output_data
from weightedscore import weightedscore
from unique_gen import unique
from fuzzywuzzy import fuzz

def gen_data(output):
    df = merge_data("/home/ssyazz/python/group/group/complile/data/input_data/scoring_A.csv, /home/ssyazz/python/group/group/complile/data/input_data/scoring_B.csv, /home/ssyazz/python/group/group/complile/data/input_data/scoring_C.csv", output)
    df, df_full = process_data(df)
    output_data([df_full], df)
    df = unique(df)
    df = weightedscore(df)
    print(df)
    df.to_csv(output + ".csv", index=False)
    
gen_data("output")
