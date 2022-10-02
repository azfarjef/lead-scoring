import pandas as pd
import numpy as np
from fuzzyduplicates import clean_partial_duplicates

def main():
	pd.set_option('display.max_columns', 30)
	df = pd.read_excel('Sampledata_Comet_Allcolumns_updated28thAug.xlsx', sheet_name='Sample Records ')
	df = df.dropna(axis=1, how='all')
	df = process_data(df)

def process_data(df, col):
	df.index = range(len(df))

	print("\nOriginal Data---------------------------------------------------------------------------")
	print(df)

	df = to_lowercase(df, col)

	print("\nto_lowercase---------------------------------------------------------------------------")
	print(df)
	
	df = clean_partial_duplicates(df)

	print("\nclean_partial_duplicates---------------------------------------------------------------------------")
	print(df)

	df = sort_by_name(df, col)
	df_full = df.copy()

	print("\nsort_by_name---------------------------------------------------------------------------")
	print(df)

	df = clean_duplicates(df, col)

	print("\nclean_duplicates---------------------------------------------------------------------------")
	print(df)

	# df = output(data, df)

	# print("\nextract columns---------------------------------------------------------------------------")
	# print(df)

	return (df, df_full)


def to_lowercase(df, col):
	to_remove = [
		col["unique_id"],
		col["created_date"],
		col["postcode"],
		col["main_phone"],
		col["contact_email"],
		col["contact_phone"],
		col["website"],
		col["ssm_no"],
		col["revenue"],
		col["employee_count"]
	]
	fields = exclude_field(df, to_remove)
	for field in fields:
		df[field] = df[field].astype(str)
		df[field] = df[field].str.lower()
	df.replace(r'nan', np.nan, regex=True, inplace=True)
	# df.fillna('thisnanwillreplaceback').apply(lambda x :x.str.lower()).replace('thisnanwillreplaceback',np.nan)
	return (df)

def sort_by_name(df, col):
	to_remove = [
			col["unique_id"]
		]
	fields = exclude_field(df, to_remove)
	i = fields.index(col["name"])
	fields.insert(0, fields.pop(i))
	print(fields)
	df = df.drop_duplicates(subset = fields)
	df = df.sort_values(by = fields)
	return (df)

# remove and merge duplicates
def clean_duplicates(df, col):
	df['Options'] = df.duplicated(subset=[col["name"]]).astype(str)
	df['Options'].replace("False", np.nan, inplace=True)

	df["tmp"] = df[df.columns.values.tolist()].isna().sum(1)
	df = df.sort_values(by="tmp").drop(columns="tmp")

	df = (
		df.groupby([col["name"]], group_keys=False)
		.apply(lambda x: x.ffill().bfill())
		.drop_duplicates([col["name"]])
	)
	return (df)

def exclude_field(df, columns):
	fields = df.columns.values.tolist()
	for field in columns:
		fields.remove(field)
	return (fields)

if __name__ == "__main__":
	main()
