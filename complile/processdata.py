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

	if 'Options' in df.columns.values.tolist():
		df = df.drop('Options', axis=1)

	print("\nOriginal Data---------------------------------------------------------------------------")
	print(df)

	df = to_lowercase(df, col, 1)

	print("\nto_lowercase---------------------------------------------------------------------------")
	print(df)
	
	df = clean_partial_duplicates(df, col)

	print("\nclean_partial_duplicates---------------------------------------------------------------------------")
	print(df)

	df = sort_by_name(df, col)
	df_full = df.copy()

	print("\nsort_by_name---------------------------------------------------------------------------")
	print(df)

	df = clean_duplicates(df, col)

	print("\nclean_duplicates---------------------------------------------------------------------------")
	print(df)

	to_lowercase(df_full, col, 2)
	df = to_lowercase(df, col, 2)

	# df = output(data, df)

	# print("\nextract columns---------------------------------------------------------------------------")
	# print(df)

	return (df, df_full)


def to_lowercase(df, col, option):
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
		col["employee_count"],
		col["source_type"],
		col["score"]
	]
	fields = exclude_field(df, to_remove)
	for field in fields:
		df[field] = df[field].astype(str)
		if option == 1:
			df[field] = df[field].str.lower()
			df[field] = df[field].str.strip()
		else:
			df[field] = df[field].str.title()
	if option == 1:
		df.replace(r'^nan$', np.nan, regex=True, inplace=True)
	else:
		df.replace(r'^Nan$', np.nan, regex=True, inplace=True)

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
