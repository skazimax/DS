import pandas as pd
data=pd.read_csv('Mountains.csv')
dataNew=data.groupby('Parent mountain').size()
print(data.loc[dataNew[dataNew>3]])