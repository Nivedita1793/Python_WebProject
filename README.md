# Python_WebProject

This is a python project to create website which display immigrants' data. It has three major steps. 

**1.Data Collection:** I have collected data from [Kaggle Datasets](https://www.kaggle.com/datasets) This dataset presents immigrants data from United States (U.S.). The data sample presented here includes all children in the Census Numerical Identification Database (Numident) of Social Security Number holders who are born in the U.S. between 1984-92. To ensure our estimates preserve anonymity and satisfy differential privacy requirements, data sample infuse a small amount of noise to each cell. In practice, this adds or subtracts a couple of people from each demographic-by-origin-by-destination migration count cell. As a result, some cells contain negative values.


**2.Database:** After collectig data, we stored it in a SQLite database. **"ImmigrantsDB.db"** is the name of database and it has only one table named by **immigrants**. Creation of database and table along with data insertion is done using the `sqlite3` package. Both SQLite and `sqlite3` come with Python. `Pandas` can be used as an intermediary.


**3.Website:**
Here we have two different source code file 

**1. app1**

**2. build_db_fillin**

Above codefiles includes code to create database and to store CSV file in to database and fetching data to display on website. 
