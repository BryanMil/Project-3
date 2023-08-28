import sqlite3
import pandas as pd

# use pandas to create dataframe based on csv data
df_Final_Obesity = pd.read_csv(r'Final_Obesity_Covid.csv')
df_Final_Confirmed = pd.read_csv(r'Final_Confirmed.csv')
df_Final_Deaths = pd.read_csv(r'Final_Deaths.csv')

# create a sqlite database and a connection to it
cnxn = sqlite3.connect('Final_Obesity.db')
crsr = cnxn.cursor()

# create Final Obesity table with a primary key
create_statement_Final_Obesity = """CREATE TABLE covid (
St text PRIMARY KEY,
'population' real,
'Covid_Deaths' real,
'Per_Deaths' real,
'Per_Obesity' real,
'TTL_Obease' real
);"""
crsr.execute(create_statement_Final_Obesity)

create_statement_Final_Confirmed = """CREATE TABLE confirmed (
St text PRIMARY KEY,
'Col_1_2020' real,
'Col_6_2020' real,
'Col_1_2021' real,
'Col_6_2021' real,
'Col_1_2022' real,
'Col_6_2022' real,
'Col_1_2023' real
);"""
crsr.execute(create_statement_Final_Confirmed)

create_statement_Final_Deaths = """CREATE TABLE deaths (
St text PRIMARY KEY,
'Col_1_2020' real,
'Col_6_2020' real,
'Col_1_2021' real,
'Col_6_2021' real,
'Col_1_2022' real,
'Col_6_2022' real,
'Col_1_2023' real
);"""
crsr.execute(create_statement_Final_Deaths)





# insert your dataframes into that database

df_Final_Obesity.to_sql('covid', cnxn, index=False, if_exists="append")
df_Final_Confirmed.to_sql('confirmed', cnxn, index=False, if_exists="append")
df_Final_Deaths.to_sql('deaths', cnxn, index=False, if_exists="append")
cnxn.close()