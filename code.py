import sqlite3
import pandas as pd
connection = sqlite3.connect("ghibli_movies.db")
cursor = connection.cursor()
cursor.execute("create table ghibli_movies (movie_name text,lead_role1 text,lead_role2 text,director text,release_year integer)")
release_list = [
    ("spirited away","haku","chihiro","hayao miyazaki",2001),
    ("my neighbor tortoro","totoro","satsuki","hayao miyazaki",1988),
    ("howl's moving castle","howl","sophie","hayao miyazaki",2004),
    ("ponyo","ponyo","sosuke","hayao miyazaki",2008)
    ]
cursor.executemany("insert into ghibli_movies values (?,?,?,?,?)",release_list)

#printing database rows
for row in cursor.execute("select * from ghibli_movies "):
    print(row)
print("*****************************************************")

#print specific rows
cursor.execute("select * from ghibli_movies where movie_name = :c", {"c":"ponyo"})
ghibli_search = cursor.fetchall()
print(ghibli_search)
print("*****************************************************")

#tollywood table 
cursor.execute("create table tollywood_movies (movie_name text,lead_actor text,lead_actress text,director text,release_year integer)")
Tmovie_list = [
    ("Shyam Shingha Roy","Nani","saipalavi","Rahul Sankrityan",2021),
    ("Bahubali","Prabhas","Anushka Shetty","S.S.Rajamouli",2015),
    ("Mahanathi","keerthy suresh","dulquer","Nag Ashwin",2018),
    ("Manam","Samantha","Naga Chaitanya","vikram kumar",2014)
    ]

cursor.executemany("insert into tollywood_movies values (?,?,?,?,?)",Tmovie_list)
cursor.execute("select * from tollywood_movies where movie_name = :c", {"c":"Manam"})
Tmovie_search = cursor.fetchall()
print(Tmovie_search)
print("*****************************************************")

#kollywood movies
cursor.execute("create table kollywood_movies (movie_name text,lead_actor text,lead_actress text,director text,release_year integer)")
Kmovie_list = [
    ("Indru Netru Naalai","Vishnu","Miya George","R.Ravi Kumar",2015),
    ("Jai Bhim","Surya","Lijomol Jose","TJ Gnanavel",2021),
    ("Doctor","Sivakarthikeyan","Priyanka Mohan","Nelson Dilipkumar",2021),
    ("Nanban","Vijay","Ileana D'Cruz","S.Sankar",2012)
    ]

cursor.executemany("insert into Kollywood_movies values (?,?,?,?,?)",Kmovie_list)
cursor.execute("select * from Kollywood_movies where movie_name = :c", {"c":"Doctor"})
Kmovie_search = cursor.fetchall()
print(Kmovie_search)
print("*****************************************************")



print(pd.read_sql_query("SELECT * FROM ghibli_movies ", connection))
print("----------------------------------------------------------------------------------")
print(pd.read_sql_query("SELECT * FROM tollywood_movies ", connection))
print("----------------------------------------------------------------------------------")
print(pd.read_sql_query("SELECT * FROM Kollywood_movies ", connection))

connection.commit()
connection.close()

