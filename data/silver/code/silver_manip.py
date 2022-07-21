# %%

import re
import pandas as pd
import numpy
import unidecode
numpy.set_printoptions(threshold=sys.maxsize)
pd.options.display.max_colwidth = 100


def data_clean(df):
    # DATA CLEAN =============================================
    df_edited = df.copy()
    # REMOVE USELESS COLUMNS     
    df_edited = df_edited.drop(['id'], axis=1)

    # DROP USELESS ROWS
    df_edited = df_edited.drop(df_edited.loc[df_edited["h_url"] == "url"].index)

    ## AREA
    # CORRECT THE AREA REMOVING THE m².
    # RELEASES HAVE AREA LIKE THIS: 57-115 m²
    # IT MEAN THAT THE APARTMENTS INITIATES WITH 57 m² THAN I WILL GET ONLY 
    # THE FIRST NUMBER.
    
    df_edited["area"] = df_edited["area"].apply(lambda x : x.split(" ")[0].split("-")[0]).astype(int)

    ## ROOMS
    # SAME PROBLEM THAN AREA
    df_edited["rooms"] = df_edited["rooms"].apply(lambda x : x.split(" ")[0].split("-")[0])
    df_edited.loc[df_edited["rooms"] == '', "rooms"] = 0
    df_edited["rooms"] = df_edited["rooms"].astype(int)

    ## BATHROOM
    df_edited["bathrooms"] = df_edited["batrooms"].apply(lambda x : x.split(" ")[0].split("-")[0])
    df_edited = df_edited.drop("batrooms", axis=1)
    df_edited.loc[df_edited["bathrooms"] == '', "bathrooms"] = None

    ## GARAGE
    df_edited["garage"] = df_edited["garage"].apply(lambda x : x.split(" ")[0].replace("--", '').split("-")[0])
    df_edited.loc[df_edited["garage"] == '', "garage"] = 0
    df_edited["garage"] = df_edited["garage"].astype(int)

    ## VALUE
    df_edited["value"] = df_edited["h_value"].apply(lambda x : x.split("\n")[0].split(" ")[-1].replace(".", ""))
    df_edited["value"] = df_edited["value"].apply(lambda x : x if(x.isnumeric()) else None)

    for id, row in df_edited.iterrows():
        if row["value"] == None:
            df_edited.loc[id, "value"] = df_edited.loc[id, "h_value"].split("\n")[-1].split(" ")[-1].replace(".", "")


    ## CONDOMINIUM
    df_edited.loc[df_edited["condominium"].isna(), "condominium"] = '0'
    df_edited["condominium"] = df_edited["condominium"].apply(lambda x : x.split(" ")[-1].replace(".", ""))

    ## BAIRROS
    df_edited["h_address"] = df_edited["h_address"].apply(lambda x : x.lower().replace(", s/n", "").replace(", ap102", ""))
    address_norm = (df_edited["h_address"].str.normalize("NFKD")
                                            .str.encode("ascii", errors="ignore")
                                            .str.decode("utf8"))

    df_edited["district"] = pd.DataFrame(address_norm)["h_address"].apply(lambda x :    re.findall("(^[a-z]+[\s*[a-z]*]*),\s\D|-\s([a-z]+[\s*[a-z]*]*),", x)[0][0].replace(" ", "_") or 
                                                                                        re.findall("(^[a-z]+[\s*[a-z]*]*),\s\D|-\s([a-z]+[\s*[a-z]*]*),", x)[0][1].replace(" ", "_"))
    # df_edited["district"] = pd.DataFrame(address_norm)["h_address"].apply(lambda x : re.findall("^[a-z]+[\s*.*[a-z]*]*,? ?\d*.?\d*[a-z]*/?[a-z]* ?-? ?([a-z]+[\s*[a-z]*]*)",x)[0].replace(" ", "_"))

    ## AMENITIES
    # df_edited["amenities"].fillna("Not")
    # df_edited["amenities"] = df_edited["amenities"].apply(lambda x : unidecode.unidecode(str(x).lower()).replace(" ", "_").replace("...", ""))
    # df_edited = pd.concat([df_edited, df_edited["amenities"].str.get_dummies(sep="\n")], axis=1)
    # df_edited = df_edited.drop("amenities", axis=1)

    # ## CITY 
    # df_edited["city"] = pd.DataFrame(address_norm)["h_address"].apply(lambda x : re.findall(", ([a-z]+[\s*[a-z]*]*) -",x)[0])

    return df_edited

 # %%
## REMOVE MISSING VALULES ==================================================================
def data_missing_values(df):
    df_edit = df.copy()

    # pd.qcut(df_edit["area"], 4).value_counts()
    # (9.999, 51.0]  
    # (51.0, 71.0]   
    # (71.0, 109.0]  
    # (109.0, 5000.0]

    # ROOMS
    rooms_9_50 = df_edit.loc[((df_edit["area"] >= 9) & (df_edit["area"] < 51)), ["rooms"]].median()[0]
    rooms_51_70 = df_edit.loc[((df_edit["area"] >= 51) & (df_edit["area"] < 71)), ["rooms"]].median()[0]
    rooms_71_108 = df_edit.loc[((df_edit["area"] >= 71) & (df_edit["area"] < 109)), ["rooms"]].median()[0]
    rooms_109_500 = df_edit.loc[((df_edit["area"] >= 109)), ["rooms"]].median()[0]

    df_edit.loc[((df_edit["area"] >= 9) & (df_edit["area"] < 51) & (df_edit["rooms"] == 0))] = rooms_9_50
    df_edit.loc[((df_edit["area"] >= 51) & (df_edit["area"] < 71) & (df_edit["rooms"] == 0))] = rooms_51_70
    df_edit.loc[((df_edit["area"] >= 71) & (df_edit["area"] < 109)& (df_edit["rooms"] == 0))] = rooms_71_108
    df_edit.loc[((df_edit["area"] >= 109) & (df_edit["rooms"] == 0))] = rooms_109_500

    # GARAGE
    garage_9_50 = df_edit.loc[((df_edit["area"] >= 9) & (df_edit["area"] < 51)), ["garage"]].mean()[0]
    garage_51_70 = df_edit.loc[((df_edit["area"] >= 51) & (df_edit["area"] < 71)), ["garage"]].mean()[0]
    garage_71_108 = df_edit.loc[((df_edit["area"] >= 71) & (df_edit["area"] < 109)), ["garage"]].mean()[0]
    garage_109_500 = df_edit.loc[((df_edit["area"] >= 109)), ["garage"]].mean()[0]

    df_edit.loc[((df_edit["area"] >= 0) & (df_edit["area"] < 51) & (df_edit["garage"] == 0))] = round(garage_9_50)
    df_edit.loc[((df_edit["area"] >= 51) & (df_edit["area"] < 71) & (df_edit["garage"] == 0))] = round(garage_51_70)
    df_edit.loc[((df_edit["area"] >= 71) & (df_edit["area"] < 109)& (df_edit["garage"] == 0))] = round(garage_71_108)
    df_edit.loc[((df_edit["area"] >= 109) & (df_edit["garage"] == 0))] = round(garage_109_500)

    ## AMENITIES

    ## BATHROOMS

    return df_edit

## RUN ==============================================================================
df = pd.read_csv("../../bronze/data/houses_full_load.csv")

## ROOMS, GARAGE, AMENITIES, VALUE, CONDOMINIUM, BATHROOMS
df_edit = data_clean(df)
df_edit = data_missing_values(df_edit)

# %%
df_edit.info()


# %%


# %%
df_edit["garage"].unique()

# %%
round(df_edit.loc[((df_edit["area"] >= 51) & (df_edit["area"] < 71)), ["garage"]].mean()[0])


# %%
