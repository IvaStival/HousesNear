# %%
import pandas as pd
import math

# %%
df = pd.read_csv("../../bronze/data/houses_full_load.csv")
df.head()
# %%

# REMOVE USELESS COLUMNS     
df = df.drop(['Unnamed: 0', 'id'], axis=1)

# DROP USELESS ROWS
df = df.drop(df.loc[df["h_url"] == "url"].index)

# %%
## AREA
# CORRECT AREA. REMOVE THE m².
# RELEASES HAVE AREA LIKE THIS: 57-115 m²
# IT MEAN THAT THE APARTMENTS INITIATES WITH 57 m² THAN I WILL GET ONLY 
# THE FIRST NUMBER.
df_edited = df.copy()
df_edited["area"] = df_edited["area"].apply(lambda x : x.split(" ")[0].split("-")[0])

## ROOMS
# SAME PROBLEM THAN AREA
df_edited["rooms"] = df_edited["rooms"].apply(lambda x : x.split(" ")[0].split("-")[0])

## BATHROOM
df_edited["bathroom"] = df_edited["batrooms"].apply(lambda x : x.split(" ")[0])
df_edited = df_edited.drop("batrooms", axis=1)

## GARAGE
df_edited["garage"] = df_edited["garage"].apply(lambda x : x.split(" ")[0].replace("--", "0").split("-")[0])

## VALUE
df_edited["h_value"] = df_edited["h_value"].apply(lambda x : int(x.split(" ")[1].split("\n")[0].replace(".", "")))
# REMOVE THE RENT APARTMENTS
df_edited = df_edited.loc[df_edited["h_value"] < 15000]

## CONDOMINIUM
df_edited.loc[df_edited["condominium"].isna(), "condominium"] = '0'
df_edited["condominium"] = df_edited["condominium"].apply(lambda x : x.split(" ")[-1].replace(".", ""))

# %%
df_edited["condominium"].unique()
# %%
