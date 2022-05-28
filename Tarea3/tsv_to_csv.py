#%%
# Change tabs to commas in a csv file "AFINN_full.csv"
import pandas as pd
from requests import head
df = pd.read_csv('AFINN_full.csv', sep='\t', header=None)
df.to_csv('AFINN_full.csv', sep=',', index=False)
df.head()
# %%
