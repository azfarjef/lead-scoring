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