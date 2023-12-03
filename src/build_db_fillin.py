import pathlib
import sqlite3
import pandas as pd


path = pathlib.Path().cwd() # use pathlib to get current working directory


def create_db(db_name, filename, table_name):
    file_path = "../CSVData/"+filename # create a path to the data file

    con = sqlite3.connect("../database/"+db_name)  # create a connection to the database
    cursor = con.cursor() # create a cursor

    studentsData =  pd.read_csv(file_path) # read in the data 
    studentsData.to_sql(table_name, con, index = False, if_exists = 'replace') #insert the data
    
    # execute a select statement as f-string and print results to verify insertion
    results = cursor.execute(f"SELECT * FROM {table_name}").fetchall()
    print(results)
    
    # commit the changes to the database
    con.commit()
                      
    # close the connection                  
    con.close()                  


if __name__=="__main__":
    db_name = "ImmigrantsDB.db"
    filename = "immigrantsData.csv"
    table_name = "immigrants"
    create_db(db_name, filename, table_name)
