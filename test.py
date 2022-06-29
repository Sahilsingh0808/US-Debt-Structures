from fileinput import filename
from os import walk
import pandas as pd
import pickle
from collections import Counter

df = pd.read_excel(
    r'/home/sahilsingh/Dropbox/MigrationData/CAFR_states_output/2016.xlsx')
# state=list(df['State'])
# list_set = set(state)
# unique_list = (list(list_set))
# print(len(unique_list))
total = list(df['Total'])
principal = list(df['Principal'])
swap = list(df['Swap Net Payment'])
interest = list(df['Interest'])
for i in range(len(total)):
    if total[i] == 0:
        df.at[(i), "Total"] = principal[i]+interest[i]+swap[i]

print(df)
states=df.State.to_list()
states = list(dict.fromkeys(states))
print(states)
print(len(states))

df.to_excel(
    "/home/sahilsingh/Dropbox/MigrationData/CAFR_states_output/2016_cleaned.xlsx")


# df=pd.read_pickle(r'/home/sahilsingh/Downloads/ca_state_of_california_2017_tabledirectory.pkl')
# print(df)
# df.to_pickle("2018.pkl")
# data=pd.DataFrame()
# with open(f"/home/sahilsingh/Documents/Repositories/US-Debt-Structures/2018.pkl", 'rb') as f:
#     data=pickle.load(f)
# data.to_excel("2018.xlsx")


# filenames = next(walk(r'/home/sahilsingh/Dropbox/MigrationData/CAFR_states_output/2020/dataout/'), (None, None, []))[2]
# states=[]
# for i in range(len(filenames)):
#     state=""
#     a=filenames[i]
#     b=a.split('_')
#     c=b[3]
#     d=b[4]
#     e=b[5]
#     # c=c.capitalize()
#     # d=d.capitalize()
#     # e=e.capitalize()
#     if d[0]=="2":
#         state=c
#     elif d=="Of":
#         state=c+"_"+d+"_"+e
#     else :
#         state=c+"_"+d
#     states.append(state)
# res = []
# for i in states:
#     if i not in res:
#         res.append(i)
# for i in range(len(res)):
#     print(res[i])

# filenames = next(walk(r'/home/sahilsingh/Dropbox/MigrationData/CAFR_states_output/2020/doc/'), (None, None, []))[2]
# for i in range(len(filenames)):
#     print(filename[i])
