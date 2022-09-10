# import pandas as pd

# data = pd.read_excel('/home/azfarjef/42KL/DHL/Sampledata_Comet_Allcolumns_updated28thAug.xlsx', sheet_name='Sample Records ')

# print(data)
# print("--------------------------------------------------")

# uniqueFields = [
# 	"Customer Name",
# 	"Address Line 1",
# 	"Main Phone #",
# 	"Contact Person Email",
# 	"Contact Person Phone",
# 	"Website",
# 	"SSM Number /Business Registration Number "
# ]

# for field in uniqueFields:
# 	data = data[(~data[field].duplicated()) | data[field].isna()]

# # data = data.drop_duplicates(subset=["Customer Name"], keep="first")
# # data = data.drop_duplicates(subset=["Address Line 1"], keep="first")
# # data = data.drop_duplicates(subset=["Main Phone #"], keep="first")
# # data = data[(~data['Main Phone #'].duplicated()) | data['Main Phone #'].isna()]
# # data = data.drop_duplicates(subset=["Contact Person Email"], keep="first")
# # data = data.drop_duplicates(subset=["Contact Person Phone"], keep="first")
# # data = data.drop_duplicates(subset=["Website"], keep="first")
# # data = data.drop_duplicates(subset=["SSM Number /Business Registration Number "], keep="first")

# data = data.dropna(axis=1, how='all')
# pd.set_option('display.max_columns', 30)

# print(data)









# combine datasets from multiple sources

# remove duplicates
# remove almost similar duplicates
# unique identifier

# add scoring column
# score the leads using formula

# output to multiple excels for different department

# check nonsense data

# questions

# 1. Which industry dhl targets, no of employee


import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 30)
# data = pd.read_excel('/home/azfarjef/42KL/DHL/Sampledata_Comet_Allcolumns_updated28thAug.xlsx', sheet_name='Sample Records ')
data = pd.read_excel('/home/azfarjef/42KL/DHL/Sampledata_Comet_Allcolumns_updated28thAug.xlsx', sheet_name='test')
data = data.dropna(axis=1, how='all')

print(data)
print("--------------------------------------------------")

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
# # data["tmp"] = data[[data.columns.values.tolist()]].isna().sum(1)
# data["tmp"] = data[["Contact no", "Address", "Website"]].isna().sum(1)
# data = data.sort_values(by="tmp").drop(columns="tmp")

# data = (
#     data.groupby(["name"])
#     .apply(lambda x: x.ffill().bfill())
#     .drop_duplicates(["name"])
# )

# --------------------------------------------------------------------------------------

# Third method
f = lambda x: ','.join(dict.fromkeys(x.dropna()).keys())
data = data.replace('',np.nan).groupby('name', as_index=False).agg(f)
data = data.replace('',np.nan).groupby('Website', as_index=False).agg(f)
data = data.replace('',np.nan).groupby('Address', as_index=False).agg(f)

data.to_csv("testing.csv")

print(data)


