import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 30)
# data = pd.read_excel('../Sampledata_Comet_Allcolumns_updated28thAug.xlsx', sheet_name='Sample Records ')
data = pd.read_excel('../Sampledata_Comet_Allcolumns_updated28thAug.xlsx', sheet_name='2test')
data = data.dropna(axis=1, how='all')

print(data)
print("---------------------------------------------------------------------------")

fields = data.columns.values.tolist()
fields.remove("no")
data = data.drop_duplicates(subset = fields)

# converts all related fields to lowercase
lowercaseFields = fields
lowercaseFields.remove("Email")
lowercaseFields.remove("Contact no")
for field in lowercaseFields:
	data[field] = data[field].str.lower()

uniqueFields = data.columns.values.tolist()
uniqueFields.remove("no")


data = data.sort_values(by = uniqueFields)

print(data)
print("---------------------------------------------------------------------------")

data['Options'] = data.duplicated(subset=["name"]).astype(str)
data['Options'].replace("False", np.nan, inplace=True)

print(data)
print("---------------------------------------------------------------------------")

# Second method
data["tmp"] = data[data.columns.values.tolist()].isna().sum(1)
data = data.sort_values(by="tmp").drop(columns="tmp")

data = (
    data.groupby(["name"])
    .apply(lambda x: x.ffill().bfill())
    .drop_duplicates(["name"])
)

print(data)
print("---------------------------------------------------------------------------")

# Extract certain column from dataframe

columns = [
	'name',
	'Contact no',
	'Email'
]

df = data[columns]

print(df)




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