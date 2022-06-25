# %%
import pandas as pd
import sqlalchemy as sqla

# %%
# CREATE A DB CONNECTION
engine = sqla.create_engine("sqlite:///../houses.db")

# SAVE TO LOCAL FOLDER
def save_local(table, db_con):
    # READ THE ENTIRE TABLE TO A DATAFRAME
    df = pd.read_sql(table, db_con)
    dest_name = f"../full_load/{table}_full_load.csv"

    # SAVE TO CSV
    df.to_csv(dest_name)

save_local("houses", engine)