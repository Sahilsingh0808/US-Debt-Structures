from fileinput import filename
from os import walk
import pandas as pd
import pickle
df = pd.read_excel (r'/home/sahilsingh/Documents/Repositories/US-Debt-Structures/output/2018/2018.xlsx')
df.to_pickle("2018.pkl")
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
states.sort()
docs = ["ok_state_of_oklahoma_2020_tabledirectory",
        "oh_state_of_ohio_2020_tabledirectory",
        "in_state_of_indiana_2020_tabledirectory",
        "pa_state_of_pennsylvania_2020_tabledirectory",
        "mo_state_of_missouri_2020_tabledirectory",
        "dc_state_of_district_of_columbia_2020_tabledirectory",
        "nd_state_of_north_dakota_2020_tabledirectory",
        "wi_state_of_wisconsin_2020_tabledirectory",
        "ga_state_of_georgia_2020_tabledirectory",
        'co_state_of_colorado_2020_tabledirectory',
        "nj_state_of_new_jersey_2020_tabledirectory",
        "ri_state_of_rhode_island_2020_tabledirectory",
        "id_state_of_idaho_2020_tabledirectory",
        "ca_state_of_california_2020_tabledirectory",
        "la_state_of_louisiana_2020_tabledirectory",
        "nh_state_of_new_hampshire_2020_tabledirectory",
        "nv_state_of_nevada_2020_tabledirectory",
        "fl_state_of_florida_2020_tabledirectory",
        "nc_state_of_north_carolina_2020_tabledirectory",
        "mn_state_of_minnesota_2020_tabledirectory",
        "ne_state_of_nebraska_2020_tabledirectory",
        "sd_state_of_south_dakota_2020_tabledirectory",
        "de_state_of_delaware_2020_tabledirectory",
        'tx_state_of_texas_2020_tabledirectory',
        "md_state_of_maryland_2020_tabledirectory",
        "il_state_of_illinois_2020_tabledirectory",
        "vt_state_of_vermont_2020_tabledirectory",
        "ar_state_of_arkansas_2020_tabledirectory",
        "al_state_of_alabama_2020_tabledirectory",
        "ky_state_of_kentucky_2020_tabledirectory",
        "mi_state_of_michigan_2020_tabledirectory",
        "hi_state_of_hawaii_2020_tabledirectory",
        "ms_state_of_mississippi_2020_tabledirectory",
        "wv_state_of_west_virginia_2020_tabledirectory",
        'ma_state_of_massachusetts_2020_tabledirectory',
        "ia_state_of_iowa_2020_tabledirectory",
        "ks_state_of_kansas_2020_tabledirectory",
        "va_state_of_virginia_2020_tabledirectory",
        "ct_state_of_connecticut_2020_tabledirectory",
        "ny_state_of_new_york_2020_tabledirectory",
        "mt_state_of_montana_2020_tabledirectory",
        "sc_state_of_south_carolina_2020_tabledirectory",
        "nm_state_of_new_mexico_2020_tabledirectory",
        'or_state_of_oregon_2020_tabledirectory',
        "me_state_of_maine_2020_tabledirectory",
        "tn_state_of_tennessee_2020_tabledirectory",
        "wa_state_of_washington_2020_tabledirectory",
        "wy_state_of_wyoming_2020_tabledirectory",
        'ut_state_of_utah_2020_tabledirectory',
        "az_state_of_arizona_2020_tabledirectory",
        "ak_state_of_alaska_2020_tabledirectory"]