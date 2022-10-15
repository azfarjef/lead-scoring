import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz

def main():
	df = pd.read_excel('Sampledata_Comet_Allcolumns_updated28thAug.xlsx', sheet_name='fuzzy')
	df = clean_partial_duplicates(df)
	print(df)

def clean_partial_duplicates(df, col):
	# First round fuzzy
	df['real_id'] = find_partitions(col, 1, df=df, match_func=similar)

	print("\nAssign id for partial_duplicates--------------------------------------------------")
	print(df)

	to_remove = [
			col["unique_id"],
			col["source_type"],
			col["score"],
			"Options"
		]
	fields = exclude_field(df, to_remove)

	df = df.replace(r'^\s+$', np.nan, regex=True)
	df["tmp"] = df[fields].isna().sum(1)
	df = df.sort_values(by="tmp").drop(columns="tmp")

	df = (
		df.groupby("real_id", group_keys=False)
		.apply(lambda x: x.ffill().bfill())
		.drop_duplicates("real_id")
	)
	df = df.drop(columns="real_id")

	# Second round fuzzy
	df['real_id'] = find_partitions(col, 2,	df=df, match_func=similar)
	df[col["name"]] = df.groupby("real_id")[col["name"]].transform('first')
	df = df.replace(r'^\s+$', np.nan, regex=True)
	df = df.drop(columns="real_id")

	return (df)

def find_partitions(col, option, df, match_func, max_size=None, block_by=None):
	"""Recursive algorithm for finding duplicates in a DataFrame."""

	# If block_by is provided, then we apply the algorithm to each block and
	# stitch the results back together
	if block_by is not None:
		blocks = df.groupby(block_by).apply(lambda g: find_partitions(
			df=g,
			match_func=match_func,
			max_size=max_size
		))

		keys = blocks.index.unique(block_by)
		for a, b in zip(keys[:-1], keys[1:]):
			blocks.loc[b, :] += blocks.loc[a].iloc[-1] + 1

		return blocks.reset_index(block_by, drop=True)

	def get_record_index(r):
		return r[df.index.name or 'index']

	df.fillna(' ', inplace=True)
	df = df.astype(str)
	# Records are easier to work with than a DataFrame
	records = df.to_records()

	# This is where we store each partition
	partitions = []

	def find_partition(at=0, partition=None, indexes=None):

		r1 = records[at]

		if partition is None:
			partition = {get_record_index(r1)}
			indexes = [at]

		# Stop if enough duplicates have been found
		if max_size is not None and len(partition) == max_size:
			return partition, indexes

		for i, r2 in enumerate(records):

			if get_record_index(r2) in partition or i == at:
				continue

			if match_func(r1, r2, df, col, option):
				partition.add(get_record_index(r2))
				indexes.append(i)
				find_partition(at=i, partition=partition, indexes=indexes)
		
		return partition, indexes

	while len(records) > 0:
		partition, indexes = find_partition()
		partitions.append(partition)
		records = np.delete(records, indexes)

	print(partitions)
	return pd.Series({
		idx: partition_id
		for partition_id, idxs in enumerate(partitions)
		for idx in idxs
	})

def similar(one, two, df, col, opt):
	base_ratio = 93
	if (opt == 1):
		to_remove = [
				col["unique_id"],
				col["source_type"],
				col["score"],
				"Options"
			]
		base_ratio = 93
	else:
		to_remove = [
				col["unique_id"],
				col["source_type"],
				col["score"],
				"Options",
				col["main_phone"],
				col["contact_name"],
				col["contact_email"],
				col["contact_designation"],
				col["contact_phone"]
			]
		base_ratio = 95
	fields = exclude_field(df, to_remove)
	ratio = 0
	len = 0
	name_weightage = 100
	for field in fields:
		if " " == one[field] and " " == two[field]:
			continue
		if field == col["name"] and opt == 2:
			ratio += (fuzz.ratio(one[field], two[field]) * name_weightage)
			len += name_weightage
		else:
			ratio += fuzz.ratio(one[field], two[field])
			len += 1
	# ratio = ratio/len(fields)
	if len == 0:
		len = 1
	ratio = ratio/len
	if (ratio > base_ratio) or one[col["name"]] == "ddd automotive":
		print(f'{one[col["name"]]}, {two[col["name"]]} = {ratio}')
	return (ratio > base_ratio)

def exclude_field(df, columns):
	fields = df.columns.values.tolist()
	for field in columns:
		if field in fields:
			fields.remove(field)
	return (fields)

if __name__ == "__main__":
	main()
