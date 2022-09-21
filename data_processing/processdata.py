import pandas as pd
import numpy as np
from fuzzyduplicates import clean_partial_duplicates

def main():
	pd.set_option('display.max_columns', 30)
	df = pd.read_excel('Sampledata_Comet_Allcolumns_updated28thAug.xlsx', sheet_name='2test')
	df = df.dropna(axis=1, how='all')

	print("\nOriginal Data---------------------------------------------------------------------------")
	print(df)

	df = to_lowercase(df)

	print("\nto_lowercase---------------------------------------------------------------------------")
	print(df)
	
	df = clean_partial_duplicates(df)

	print("\nclean_partial_duplicates---------------------------------------------------------------------------")
	print(df)

	df = sort_by_name(df)

	print("\nsort_by_name---------------------------------------------------------------------------")
	print(df)

	df = clean_duplicates(df)

	print("\nclean_duplicates---------------------------------------------------------------------------")
	print(df)

	column = [
		'Contact no',
		'Email',
		'name'
	]
	df = extract_column(df, column)

	print("\nextract columns---------------------------------------------------------------------------")
	print(df)


def to_lowercase(df):
	to_remove = [
		"no",
		"Email",
		"Contact no"
	]
	fields = exclude_field(df, to_remove)
	for field in fields:
		df[field] = df[field].str.lower()
	return (df)

def sort_by_name(df):
	to_remove = [
			"no"
		]
	fields = exclude_field(df, to_remove)
	df = df.drop_duplicates(subset = fields)
	df = df.sort_values(by = fields)
	return (df)

# remove and merge duplicates
def clean_duplicates(df):
	df['Options'] = df.duplicated(subset=["name"]).astype(str)
	df['Options'].replace("False", np.nan, inplace=True)

	df["tmp"] = df[df.columns.values.tolist()].isna().sum(1)
	df = df.sort_values(by="tmp").drop(columns="tmp")

	df = (
		df.groupby(["name"])
		.apply(lambda x: x.ffill().bfill())
		.drop_duplicates(["name"])
	)
	return (df)

def exclude_field(df, columns):
	fields = df.columns.values.tolist()
	for field in columns:
		fields.remove(field)
	return (fields)

# Extract certain column from dataframe
def extract_column(df, column):
	df = df[column]
	return (df)

main()