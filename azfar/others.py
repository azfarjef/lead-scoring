import pandas as pd
from processdata import process_data
from output import output_data

def main():
	df = pd.read_csv("merge.csv", index_col=[0])
	df, df_full = process_data(df)
	print(df)
	print("Full data -----------------------------------------------------------")
	print(df_full)
	print(df_full.dtypes)
	output_data([df_full], df)

main()

# Other methods to remove duplicates

# # Zeroth method
# uniqueFields = [
# 	"name",
# 	"Contact no",
# 	"Address",
# 	"Website"
# ]

# for field in uniqueFields:
# 	data = data[(~data[field].duplicated()) | data[field].isna()]

# # data = data.drop_duplicates(subset=["Main Phone #"], keep="first")
# # data = data[(~data['Main Phone #'].duplicated()) | data['Main Phone #'].isna()]

# --------------------------------------------------------------------------------------

# # First method
# data = data.replace('',np.nan).groupby('name', as_index=False).first().fillna('')

# --------------------------------------------------------------------------------------

# # Second method
# data["tmp"] = data[data.columns.values.tolist()].isna().sum(1)
# # data["tmp"] = data[["Contact no", "Address", "Website"]].isna().sum(1)
# data = data.sort_values(by="tmp").drop(columns="tmp")

# data = (
#     data.groupby(["name"])
#     .apply(lambda x: x.ffill().bfill())
#     .drop_duplicates(["name"])
# )

# --------------------------------------------------------------------------------------

# # Third method
# f = lambda x: ','.join(dict.fromkeys(x.dropna()).keys())
# data = data.replace('',np.nan).groupby('name', as_index=False).agg(f)
# data = data.replace('',np.nan).groupby('Website', as_index=False).agg(f)
# data = data.replace('',np.nan).groupby('Address', as_index=False).agg(f)

# # data.to_csv("testing.csv")

# --------------------------------------------------------------------------------------