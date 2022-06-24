from fileinput import filename
from os import walk
import pandas as pd
import pickle
from collections import Counter

df = pd.read_excel(
    r'/home/sahilsingh/Dropbox/MigrationData/CAFR_states_output/2017.xlsx')
# state=list(df['State'])
# list_set = set(state)
# unique_list = (list(list_set))
# print(len(unique_list))
total=list(df['Total'])
principal=list(df['Principal'])
swap=list(df['Swap Net Payment'])
interest=list(df['Interest'])
for i in range(len(total)):
    if total[i] == 0:
        df.at[(i),"Total"]=principal[i]+interest[i]+swap[i]

print(df)
df.to_excel("/home/sahilsingh/Dropbox/MigrationData/CAFR_states_output/2017_cleaned.xlsx")


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


states = ["north_carolina",
          "nevada",
          "illinois",
          "new_mexico",
          "connecticut",
          "colorado",
          "oregon",
          "louisiana",
          "idaho",
          "florida",
          "kansas",
          "california",
          "south_dakota",
          "alabama",
          'massachusetts',
          "oklahoma",
          "north_dakota",
          "tennessee",
          "mississippi",
          "wyoming",
          "michigan",
          "maine",
          "virginia",
          "arkansas",
          "kentucky",
          "indiana",
          "montana",
          "west_virginia",
          "ohio",
          "rhode_island",
          "new_york",
          "utah",
          "delaware",
          "georgia",
          "missouri",
          "maryland",
          "arizona",
          "nebraska",
          "washington",
          'texas',
          "new_hampshire",
          "minnesota",
          "south_carolina",
          "pennsylvania",
          "new_jersey",
          "vermont",
          "wisconsin",
          "district_of_columbia",
          "hawaii",
          "alaska"]
docs = ["ok_state_of_oklahoma_",
        "oh_state_of_ohio_",
        "in_state_of_indiana_",
        "pa_state_of_pennsylvania_",
        "mo_state_of_missouri_",
        "dc_state_of_district_of_columbia_",
        "nd_state_of_north_dakota_",
        "wi_state_of_wisconsin_",
        "ga_state_of_georgia_",
        'co_state_of_colorado_',
        "nj_state_of_new_jersey_",
        "ri_state_of_rhode_island_",
        "id_state_of_idaho_",
        "ca_state_of_california_",
        "la_state_of_louisiana_",
        "nh_state_of_new_hampshire_",
        "nv_state_of_nevada_",
        "fl_state_of_florida_",
        "nc_state_of_north_carolina_",
        "mn_state_of_minnesota_",
        "ne_state_of_nebraska_",
        "sd_state_of_south_dakota_",
        "de_state_of_delaware_",
        'tx_state_of_texas_',
        "md_state_of_maryland_",
        "il_state_of_illinois_",
        "vt_state_of_vermont_",
        "ar_state_of_arkansas_",
        "al_state_of_alabama_",
        "ky_state_of_kentucky_",
        "mi_state_of_michigan_",
        "hi_state_of_hawaii_",
        "ms_state_of_mississippi_",
        "wv_state_of_west_virginia_",
        'ma_state_of_massachusetts_',
        "ia_state_of_iowa_",
        "ks_state_of_kansas_",
        "va_state_of_virginia_",
        "ct_state_of_connecticut_",
        "ny_state_of_new_york_",
        "mt_state_of_montana_",
        "sc_state_of_south_carolina_",
        "nm_state_of_new_mexico_",
        'or_state_of_oregon_',
        "me_state_of_maine_",
        "tn_state_of_tennessee_",
        "wa_state_of_washington_",
        "wy_state_of_wyoming_",
        'ut_state_of_utah_',
        "az_state_of_arizona_",
        "ak_state_of_alaska_"]
codes = []
for i in range(len(states)):
    state = states[i]
    for j in range(len(docs)):
        if state in docs[j]:
            codes.append(docs[j])
            break
for i in range(len(codes)):
    print(codes[i])
# print(len(states))
# print(len(docs))

codes = ["nc_state_of_north_carolina_",
         "nv_state_of_nevada_",
         "il_state_of_illinois_",
         "nm_state_of_new_mexico_",
         "ct_state_of_connecticut_",
         "co_state_of_colorado_",
         "or_state_of_oregon_",
         "la_state_of_louisiana_",
         "id_state_of_idaho_",
         "fl_state_of_florida_",
         "ar_state_of_arkansas_",
         "ca_state_of_california_",
         "sd_state_of_south_dakota_",
         "al_state_of_alabama_",
         "ma_state_of_massachusetts_",
         "ok_state_of_oklahoma_",
         "nd_state_of_north_dakota_",
         "tn_state_of_tennessee_",
         "ms_state_of_mississippi_",
         "wy_state_of_wyoming_",
         "mi_state_of_michigan_",
         "me_state_of_maine_",
         "wv_state_of_west_virginia_",
         "ar_state_of_arkansas_",
         "ky_state_of_kentucky_",
         "in_state_of_indiana_",
         "mt_state_of_montana_",
         "wv_state_of_west_virginia_",
         "oh_state_of_ohio_",
         "ri_state_of_rhode_island_",
         "ny_state_of_new_york_",
         "ut_state_of_utah_",
         "de_state_of_delaware_",
         "ga_state_of_georgia_",
         "mo_state_of_missouri_"
         "md_state_of_maryland_",
         "az_state_of_arizona_",
         "ne_state_of_nebraska_",
         "wa_state_of_washington_",
         "tx_state_of_texas_",
         "nh_state_of_new_hampshire_",
         "mn_state_of_minnesota_",
         "sc_state_of_south_carolina_",
         "pa_state_of_pennsylvania_",
         "nj_state_of_new_jersey_",
         "vt_state_of_vermont_",
         "wi_state_of_wisconsin_",
         "dc_state_of_district_of_columbia_",
         "hi_state_of_hawaii_",
         "ak_state_of_alaska_"]
