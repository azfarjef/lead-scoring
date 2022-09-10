import	pandas as pd

data = pd.read_csv("Sampledata_Comet_Allcolumns_updated28thAug.csv")

data['Unique Lead Assignment Number'] = data.groupby(['Customer Name']).ngroup()

results = data.head(20)

print(data.head(25))
# print(results)