import pandas as pd
import pickle
df = pd.read_excel (r'/home/sahilsingh/Documents/Repositories/US-Debt-Structures/2019.xlsx')
df.to_pickle("2019.pkl")
# data=pd.DataFrame()
# with open(f"/home/sahilsingh/Documents/Repositories/US-Debt-Structures/2018.pkl", 'rb') as f:  
#     data=pickle.load(f)
# data.to_excel("2018.xlsx")