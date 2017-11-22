import pandas as pd
data=pd.read_csv('Mountains.csv')
dataNew=data.groupby('Parent mountain').size()
print(dataNew[dataNew>3])