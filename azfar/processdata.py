import pandas as pd
import numpy as np
from fuzzyduplicates import clean_partial_duplicates

def main():
	pd.set_option('display.max_columns', 30)
	df = pd.read_excel('Sampledata_Comet_Allcolumns_updated28thAug.xlsx', sheet_name='Sample Records ')
	df = df.dropna(axis=1, how='all')
	df = process_data(df)

def process_data(df):
	df.index = range(len(df))

	print("\nOriginal Data---------------------------------------------------------------------------")
	print(df)

	df = to_lowercase(df)

	print("\nto_lowercase---------------------------------------------------------------------------")
	print(df)
	
	df = clean_partial_duplicates(df)

	print("\nclean_partial_duplicates---------------------------------------------------------------------------")
	print(df)

	df = sort_by_name(df)
	df_full = df.copy()

	print("\nsort_by_name---------------------------------------------------------------------------")
	print(df)

	df = clean_duplicates(df)

	print("\nclean_duplicates---------------------------------------------------------------------------")
	print(df)

	# df = output(data, df)

	# print("\nextract columns---------------------------------------------------------------------------")
	# print(df)

	return (df, df_full)


def to_lowercase(df):
	to_remove = [
		"Unique Lead Assignment Number ",
		"Suspect Creation date by Lead Originator",
		"Post Code",
		"Main Phone #",
		"Contact Person Email",
		"Contact Person Phone",
		"Website",
		"SSM Number /Business Registration Number ",
		"Total Potential Revenue/Month",
		"Employee Count"
	]
	fields = exclude_field(df, to_remove)
	for field in fields:
		df[field] = df[field].astype(str)
		df[field] = df[field].str.lower()
	df.replace(r'nan', np.nan, regex=True)
	# df.fillna('thisnanwillreplaceback').apply(lambda x :x.str.lower()).replace('thisnanwillreplaceback',np.nan)
	return (df)

def sort_by_name(df):
	to_remove = [
			"Unique Lead Assignment Number "
		]
	fields = exclude_field(df, to_remove)
	i = fields.index("Customer Name")
	fields.insert(0, fields.pop(i))
	print(fields)
	df = df.drop_duplicates(subset = fields)
	df = df.sort_values(by = fields)
	return (df)

# remove and merge duplicates
def clean_duplicates(df):
	df['Options'] = df.duplicated(subset=["Customer Name"]).astype(str)
	df['Options'].replace("False", np.nan, inplace=True)

	df["tmp"] = df[df.columns.values.tolist()].isna().sum(1)
	df = df.sort_values(by="tmp").drop(columns="tmp")

	df = (
		df.groupby(["Customer Name"])
		.apply(lambda x: x.ffill().bfill())
		.drop_duplicates(["Customer Name"])
	)
	return (df)

def exclude_field(df, columns):
	fields = df.columns.values.tolist()
	for field in columns:
		fields.remove(field)
	return (fields)

if __name__ == "__main__":
	main()
