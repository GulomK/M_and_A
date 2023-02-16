import pandas as pd
import sqlite3 as sql
import numpy as np
import my_ds_babel

def my_m_and_a(content_database_1, content_database_2, content_database_3):
    df = pd.read_csv(content_database_1) 
        
    # Cleaning the column Gender in the content_database_1
    gender = {"1" : "Female", "0" : "Male", "F" : "Female", "M" : "Male"}
    df["Gender"] = df["Gender"].replace(gender)

    # Cleaning the column FirstName in the content_database_1
    df["FirstName"] = df["FirstName"].str.replace("\W", "", regex=True)
    df["FirstName"] = df["FirstName"].str.title()

    # Cleaning the column LastName in the content_database_1
    df["LastName"] = df["LastName"].str.replace("\W", "", regex=True)
    df["LastName"] = df["LastName"].str.title()

    # Cleaning the column UserName in the content_database_1
    df["UserName"] = df["UserName"].str.lower()
        
    # Cleaning the column Email in the content_database_1
    df["Email"] = df["Email"].str.lower()

    # Cleaning the column City in the content_database_1
    df["City"] = df["City"].str.replace("_", "-")
    df["City"] = df["City"].str.replace(" ", "-")
    df["City"] = df["City"].str.title()

    # Cleaning the column Country in the content_database_1
    df.Country = "USA"
    
    #############################################################################

    df_2 = pd.read_csv(content_database_2, sep=';', header=None, names = ["Age", "City", "Gender", "Name", "Email"])

    # Cleaning the column Age in the content_database_2
    df_2["Age"] = df_2["Age"].str.replace("\D", "", regex=True)

    # Cleaning the column City in the content_database_2
    df_2["City"] = df_2["City"].str.replace("_", "-")
    df_2["City"] = df_2["City"].str.replace(" ", "-")
    df_2["City"] = df_2["City"].str.title()

    # Cleaning the column Gender in the content_database_2
    gender = {"1" : "Female", "0" : "Male", "F" : "Female", "M" : "Male"}
    df_2["Gender"] = df_2["Gender"].replace(gender)

    # Cleaning the column Name in the content_database_2
    df_2["Name"] = df_2["Name"].str.replace("\W", " ", regex=True)
    df_2["Name"] = df_2["Name"].str.title()
    df_2["First_name"] = df_2["Name"].str.split(expand=True)[0]
    df_2["Last_name"] = df_2["Name"].str.split(expand=True)[1]
    df_2.drop("Name", axis=1, inplace=True)

    # Cleaning the column Email in the content_database_2
    df_2["Email"] = df_2["Email"].str.lower()

    #############################################################################

    df_3 = pd.read_csv(content_database_3, sep='\t', skiprows=1, names = ["Gender", "Name", "Email", "Age", "City", "Country"])

    # Cleaning the column Gender in the content_database_2
    gender = {"string_Female" : "Female", "string_Male" : "Male", "boolean_1" : "Female", "boolean_0" : "Male", "character_M" : "Male"}
    df_3["Gender"] = df_3["Gender"].replace(gender)

    # Cleaning the column Name in the content_database_3
    df_3["Name"] = df_3["Name"].str.replace("string_", "")
    df_3["Name"] = df_3["Name"].str.replace("\W", " ", regex=True)
    df_3["Name"] = df_3["Name"].str.title()
    df_3["First_name"] = df_3["Name"].str.split(expand=True)[0]
    df_3["Last_name"] = df_3["Name"].str.split(expand=True)[1]
    df_3.drop("Name", axis=1, inplace=True)

    # Cleaning the column Email in the content_database_3
    df_3["Email"] = df_3["Email"].str.replace("string_", "")
    df_3["Email"] = df_3["Email"].str.lower()

    # Cleaning the column Age in the content_database_2
    df_3["Age"] = df_3["Age"].str.replace("\D", "", regex=True)

    # Cleaning the column City in the content_database_2
    df_3["City"] = df_3["City"].str.replace("string_", "")
    df_3["City"] = df_3["City"].str.replace("_", "-")
    df_3["City"] = df_3["City"].str.replace(" ", "-")
    df_3["City"] = df_3["City"].str.title()

    # Cleaning the column Country in the content_database_1
    df_3.Country = "USA"

    #############################################################################

    main_table = pd.concat([df, df_2, df_3], ignore_index=True)
    main_table = main_table.reindex(columns = ['Gender', 'FirstName', 'LastName', 'Email', 'Age', 'City', 'Country'])
    main_table.Age  = main_table.Age.astype('str')
    main_table.FirstName  = main_table.FirstName.astype('str')
    main_table.LastName  = main_table.LastName.astype('str')
    return main_table

# merged_csv = my_m_and_a("only_wood_customer_us_1.csv", "only_wood_customer_us_2.csv", "only_wood_customer_us_3.csv")
# my_ds_babel.csv_to_sql(merged_csv, 'plastic_free_boutique.sql', 'customers')
