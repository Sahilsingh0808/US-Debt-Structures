import pandas as pd
import glob
from os import walk
import os

folders=r'/home/sahilsingh/Downloads/output (2)/output/2019/Sheets_new'
dfs = []

filenames1 = next(walk(
                r'/home/sahilsingh/Downloads/output (2)/output/2019/Sheets_new'), (None, None, []))[2]

df=pd.DataFrame()
for i in range(len(filenames1)):
    x=pd.read_excel(r'/home/sahilsingh/Downloads/output (2)/output/2019/Sheets_new/'+filenames1[i])
    df=pd.concat((df,x),axis=0)

print(df)
df.to_excel(r'/home/sahilsingh/Dropbox/MigrationData/CAFR_states_output/2019_cleaned.xlsx')