# %%
from curses.ascii import isalpha
import re
import pandas as pd
import numpy
import unidecode
numpy.set_printoptions(threshold=sys.maxsize)
pd.options.display.max_colwidth = 100
# %%
df = pd.read_csv("../../bronze/data/houses_full_load.csv")
df.head()
# %%

# REMOVE USELESS COLUMNS     
df = df.drop(['id'], axis=1)

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
df_edited["h_value"] = df_edited["h_value"].apply(lambda x : x.split(" ")[-1].replace(".", ""))
df_edited["h_value"] = df_edited["h_value"].apply(lambda x : x if(x.isnumeric()) else 0)

## CONDOMINIUM
df_edited.loc[df_edited["condominium"].isna(), "condominium"] = '0'
df_edited["condominium"] = df_edited["condominium"].apply(lambda x : x.split(" ")[-1].replace(".", ""))

## AMENITIES
df_edited["amenities"].fillna("Not")
df_edited["amenities"] = df_edited["amenities"].apply(lambda x : unidecode.unidecode(str(x).lower()).replace(" ", "_").replace("...", ""))
df_edited = pd.concat([df_edited, df_edited["amenities"].str.get_dummies(sep="\n")], axis=1)
df_edited = df_edited.drop("amenities", axis=1)

## BAIRROS
address_norm = (df_edited["h_address"].str.lower().str.normalize("NFKD")
                                                .str.encode("ascii", errors="ignore")
                                                .str.decode("utf8"))
df_edited["bairros"] = pd.DataFrame(address_norm)["h_address"].apply(lambda x : re.findall("(^[a-z]+[\s*[a-z]*]*),\s\D|-\s([a-z]+[\s*[a-z]*]*),",x)[0][1])

## CITY 
df_edited["city"] = pd.DataFrame(address_norm)["h_address"].apply(lambda x : re.findall(", ([a-z]+[\s*[a-z]*]*) -",x)[0])

## STREET
df_edited["street"] = pd.DataFrame(address_norm)["h_address"].apply(lambda x : re.findall(" +([a-z]+[\s*[a-z]*]*),* \d* *-",x)[0].replace(" ","_"))
# %%
df_edited
# %%
