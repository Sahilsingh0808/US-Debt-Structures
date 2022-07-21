from ast import In
from calendar import c
from fileinput import filename
from os import walk
from re import A
from sqlite3 import TimestampFromTicks
import pandas as pd
import pickle
from collections import Counter
import numpy as np
from regex import B

threshold=0
def equalsAprox(a,b):
    if(a+threshold)>=b and (a-threshold)<=b:
        return True
    return  False

df = pd.read_excel(
    r'/home/sahil/Dropbox/MigrationData/CAFR_states_output/2012.xlsx')
df.fillna(0)
df.replace(np.nan,0, regex=True)
total = list(df['Total'])
principal = list(df['Principal'])
swap = list(df['Swap Net Payment'])
interest = list(df['Interest'])
rowsList=[]
for i in range(len(total)):
    if total[i] == 0:
        PrincipalInd=0
        InterestInd=0
        SwapNetInd=0
        TotalInd=0
        head=list(df.iloc[[i]])
        row=(df.iloc[[i]].values).tolist()
        print(head)
        print(row)
        startInd=-1
        for j in range(0,len(head)):
            if 'Principal' in str(head[j]):
                PrincipalInd=j
            if 'Interest' in str(head[j]):
                InterestInd=j
            if 'Swap Net Payment' in str(head[j]):
                SwapNetInd=j
            if 'Total' in str(head[j]):
                TotalInd=j
        for j in range(0,len(head)):
            if 'Total' == str(head[j]):
                startInd=j+1
                break
        print(startInd)
        checkNonZeroes=0
        NonZeroesIndex=[]
        row=row[0]
        for j in range(startInd,len(row)):
            if row[j]>0:
                checkNonZeroes+=1
                NonZeroesIndex.append(j)
        print(checkNonZeroes)
        if checkNonZeroes==1:
            row[TotalInd]=row[NonZeroesIndex[0]]
            row[NonZeroesIndex[0]]=0
        if checkNonZeroes==2:
            row[PrincipalInd]=row[NonZeroesIndex[0]]
            row[InterestInd]=row[NonZeroesIndex[1]]
            row[TotalInd]=row[PrincipalInd]+row[InterestInd]
            row[NonZeroesIndex[0]]=0
            row[NonZeroesIndex[1]]=0
        if checkNonZeroes==3:
            a=row[NonZeroesIndex[0]]
            b=row[NonZeroesIndex[1]]
            c=row[NonZeroesIndex[2]]
            if equalsAprox((a+b),c):
                row[PrincipalInd]=a
                row[InterestInd]=b
                row[TotalInd]=c
            if equalsAprox((a+c),b):
                row[PrincipalInd]=a
                row[InterestInd]=c
                row[TotalInd]=b
            if equalsAprox((c+b),a):
                row[PrincipalInd]=b
                row[InterestInd]=c
                row[TotalInd]=a
            else:
                row[PrincipalInd]=a
                row[InterestInd]=b
                row[TotalInd]=c
            row[NonZeroesIndex[0]]=0
            row[NonZeroesIndex[1]]=0
            row[NonZeroesIndex[2]]=0
        if checkNonZeroes==4:
            a=row[NonZeroesIndex[0]]
            b=row[NonZeroesIndex[1]]
            c=row[NonZeroesIndex[2]]
            d=row[NonZeroesIndex[3]]
            if equalsAprox((a+b+c),d):
                row[PrincipalInd]=a
                row[InterestInd]=b
                row[SwapNetInd]=c
                row[TotalInd]=d
            if equalsAprox((a+b+d),c):
                row[PrincipalInd]=a
                row[InterestInd]=b
                row[SwapNetInd]=d
                row[TotalInd]=c
            if equalsAprox((a+d+c),b):
                row[PrincipalInd]=a
                row[InterestInd]=c
                row[SwapNetInd]=d
                row[TotalInd]=b
            if equalsAprox((d+b+c),a):
                row[PrincipalInd]=b
                row[InterestInd]=c
                row[SwapNetInd]=d
                row[TotalInd]=a
            else:
                row[PrincipalInd]=a
                row[InterestInd]=b
                row[SwapNetInd]=c
                row[TotalInd]=d
            row[NonZeroesIndex[0]]=0
            row[NonZeroesIndex[1]]=0
            row[NonZeroesIndex[2]]=0
            row[NonZeroesIndex[3]]=0
        if checkNonZeroes==6:
            a=row[NonZeroesIndex[0]]
            b=row[NonZeroesIndex[1]]
            c=row[NonZeroesIndex[2]]
            d=row[NonZeroesIndex[3]]
            e=row[NonZeroesIndex[4]]
            f=row[NonZeroesIndex[5]]
            if (a+b)==c:
                rowCopy=row.copy()
                row[PrincipalInd]=a
                row[InterestInd]=b
                row[TotalInd]=c
                row[NonZeroesIndex[0]]=0
                row[NonZeroesIndex[1]]=0
                row[NonZeroesIndex[2]]=0
                rowCopy[PrincipalInd]=d
                rowCopy[InterestInd]=e
                rowCopy[TotalInd]=f
                rowCopy[NonZeroesIndex[0]]=0
                rowCopy[NonZeroesIndex[1]]=0
                rowCopy[NonZeroesIndex[2]]=0
                rowCopy[NonZeroesIndex[3]]=0
                rowCopy[NonZeroesIndex[4]]=0
                rowCopy[NonZeroesIndex[5]]=0
                rowsList.append(rowCopy)
            else:
                rowCopy1=row.copy()
                rowCopy2=row.copy()
                row[PrincipalInd]=a
                row[InterestInd]=b
                row[TotalInd]=a+b
                row[NonZeroesIndex[0]]=0
                row[NonZeroesIndex[1]]=0
                rowCopy1[PrincipalInd]=c
                rowCopy1[InterestInd]=d
                rowCopy1[TotalInd]=d+c
                rowCopy1[NonZeroesIndex[0]]=0
                rowCopy1[NonZeroesIndex[1]]=0
                rowCopy1[NonZeroesIndex[2]]=0
                rowCopy1[NonZeroesIndex[3]]=0
                rowCopy2[PrincipalInd]=e
                rowCopy2[InterestInd]=f
                rowCopy2[TotalInd]=f+e
                rowCopy2[NonZeroesIndex[0]]=0
                rowCopy2[NonZeroesIndex[1]]=0
                rowCopy2[NonZeroesIndex[2]]=0
                rowCopy2[NonZeroesIndex[3]]=0
                rowCopy2[NonZeroesIndex[4]]=0
                rowCopy2[NonZeroesIndex[5]]=0
                rowsList.append(rowCopy1)
                rowsList.append(rowCopy2)
                
        print(row)
        df.iloc[i]=row
        print()

for i in range(0,len(rowsList)):
    df.loc[len(df)]=rowsList[i]
df=df.iloc[:,1:9]
print(df)
            
df.to_excel(
    "/home/sahil/Dropbox/MigrationData/CAFR_states_output/2012_cleaned.xlsx")