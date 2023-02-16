import sqlite3 as sql
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def csv_to_sql(csv_content, database, table_name):
    f = pd.read_csv(csv_content)
    connection = sql.connect(database)
    f.to_sql(table_name, con=connection, if_exists='replace', index=False)