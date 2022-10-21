from pandas import ExcelWriter
import pandas as pd
import csv

def main():
	pd.set_option('display.max_columns', 30)
	df = pd.read_excel('Sampledata_Comet_Allcolumns_updated28thAug.xlsx', sheet_name='Sample Records ')
	
	data = [df]
	output_data(data, df)

def output_data(data, df, output):
	# 'Company info', 'Sales', 'Contact info', 'Lead info', 'Lead scores'
	with open('data/output_columns.csv', newline='', mode='r', encoding='utf-8-sig') as f:
		reader = csv.reader(f)
		column = list(reader)
	unique_column = df.columns.values.tolist()
	master_column = df.columns.values.tolist()
	unique_column.insert(0, "Unique data")
	master_column.insert(0, "Master data")
	# print(full_column)
	column.insert(0, unique_column)
	column.insert(0, master_column)
	# print(column)

	# strip() whitespace
	for col in column:
		col[:] = [info.strip() for info in col]

	sheetName = []
	for co in column:
		sheetName.append(co[0])
		co.pop(0)
		while("" in co):
			co.remove("")
	# print(column[0])
	print(sheetName)

	# data = []
	# print(len(column))
	for col in column[1:]:
		tmp = extract_column(df, col)
		data.append(tmp)
	
	# print(len(data))
	# print(data[1].columns.values.tolist())
	save_xls(data, output + ".xlsx", sheetName)

        # added for search function
	save_xls(data, "output_backup.xlsx", sheetName)

	# print(df)

# Extract certain column from dataframe
def extract_column(df, column):
	df = df[column]
	return (df)

def save_xls(list_dfs, xls_path, sheetName):
	with ExcelWriter(xls_path) as writer:
		for n, df in enumerate(list_dfs):
			# print(n)
			df.to_excel(writer, index=False, sheet_name=sheetName[n])

if __name__ == "__main__":
	main()
