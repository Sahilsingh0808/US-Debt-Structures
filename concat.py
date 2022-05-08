import pickle
import pandas as pd
from os import walk

filenames = next(walk(r'/home/sahilsingh/Downloads/output/2019/Tables_new'), (None, None, []))[2]
finalData=pd.DataFrame(columns=['Due Year','State','Table ID','Table Category','Principal','Interest','Swap Net Payment','Total'])
for i in range(len(filenames)):
    with open(f"/home/sahilsingh/Downloads/output/2019/Tables_new/{filenames[i]}", 'rb') as f:  
        data=pickle.load(f)
        finalData=pd.concat((finalData,data),axis=0)

state=finalData['Entity Name']
finalData['State']=state
total=finalData['Total']
finalData.drop(['index','Entity Name','Total'], inplace=True, axis=1)
finalData.insert(loc=len(finalData.columns),column='Total',value=total)
finalData=finalData.fillna(0)
finalData=finalData.reset_index(drop=True)
finalData.index = range(1,len(finalData)+1)
print(finalData)
finalData.to_excel("2019.xlsx")
