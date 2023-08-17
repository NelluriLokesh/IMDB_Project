'''
Dataset: ''

Explore
Analyze
Cleaning
Manipulation
Feature Engineering
Modeling
Validation and Interpretation
Reporting and Visualization
  
step1 -- importing the tools or libraries
         1.numpy  ->to perform the mathematical operations
         2.pandas  ->data maniplucatoin
         3.matplotlib -> data visulisation
         4.seaborn -> data visulisation tool
         5.SQLite -> server less data base

hints and tips:
    1.connect your database(or create a connection) -> sqlite3.connect(database_name)
    2. use the cursor function -> database_veriable.cursor()

workflow:
    1.you need to establish a connection to your sqlite database by creating a connection object
    2.then, you have to create a cursor object using the cursor() method
    3.then, excute the query-> cursor_object.execute('query')
    4.to fetch the data, the use fecthall() method of the cursor object
    
step2 --
        1.establish the connection to database


QUESTIONS:
    first analysis::
        1.Get all the data about directors
        2.Check how many movies are pressent in the imdb table
        3.Find these 3 directors : james cameron,luc cameron,luc besson
        4.Find all the directore with names starting with steven
        5.Count the female directors
        6.Find the names of the 10th first women directors
        7.Whare the 3 most popular movies
        8.What are the 3 most bankable movie
        9.What is the most awarded average vote movie since the jan 1st, 2000
        10.Which movies were directed by Brenda chapman
        11.name the director who made the most movies
        12.name of the director who is most bankable

     second budget analysis:
Q.tell top 10 hightest budget making movies

    revenue analysis
Q.find top 10 revenue making movies

     voting analysis
1.find the most popular movies with hightest vote average
2.find all the movies for vote_average and vote_count

     director analysis
Q.name all the directors with number of 
    movies and revenue where revenue should be taken into accounts for doing the analysis

Q. give the title of 
    the movies,release_date,budget,revenue,popularity and vote_average made by steven spielberg

Q.name all the directors with number of 
    movies and revenue where NO.OF MOVIES SHOULD be taken into accounts for doing the analysis


'''

# NUMPY >to perform the mathematical operations
import numpy as np
# PANDAS ->data maniplucatoin
import pandas as pd
# MATPLOYLIB -> data visulisation
import matplotlib.pyplot as plt
# SEABORM-> data visulisation tool
import seaborn as sns
# .SQLite -> server less data base
import sqlite3

import warnings
warnings.filterwarnings('ignore')
### hints and tips

df = r"C:\Users\ABC\Desktop\data scientist\PROJECTS\PROJECTS files\imdb\movies.sqlite"
## there 2 tables in this dataset -> movies and directors
conn = sqlite3.connect(df)
cur = conn.cursor()

# establishing the connection with the data base
cur.execute('SELECT * FROM movies')

## creating the cursor object
movies = cur.fetchall()

## displying the database data
#print(movies)

## creating a dataframe
movies = pd.DataFrame(movies,columns=['id','original_title','buget','popularity','release_date',
                                    'revenue','title','vote_average','vote_count','overvi','tagline',
                                    'uid','director_id'])
## displaying the dataframe
# print(movies)

## analysis 

# 1. get all the data about directors
cur.execute('SELECT * FROM directors')
directors = cur.fetchall()
directors = pd.DataFrame(directors,columns=['name','id','gender','UID','depertment'])

## To run the above theory uncomment the below line
# print(directors)



## 2.check how many movies are present in the IMDB table
cur.execute('SELECT COUNT(title) FROM movies')
count = cur.fetchall()

## To run the above theory uncomment the below line
# print(f"The number of movies present in the IMDB database id {count[0][0]}")



## 3.Find these 3 directors : James Cameron , John Woo , Luc Besson
#cur.execute('SELECT * FROM directors WHERE name IN ("James Cameron","John Woo","Luc Besson") ')
###           or 
cur.execute("SELECT * FROM directors WHERE name ='James Cameron' OR name='John Woo' OR name='Luc Besson'")
three_directores = cur.fetchall()

## To run the above theory uncomment the below line
# print(f"These 3 Directors data are : {three_directores}")



## 4.find all the directores with name starting with 'Steven'
cur.execute("SELECT * FROM directors WHERE name LIKE 'Steven%' ")
name_like = cur.fetchall()

## To run the above theory uncomment the below line
# print(f"The directors whose name are starting eith the word Steven are{name_like}")


## 5.Count the female directors
cur.execute('SELECT COUNT(gender) FROM directors WHERE gender = 1')
gender = cur.fetchall()

## To run the above theory uncomment the below line
# print(f"The total number of female are {gender[0][0]}")



## 6.Find the names of the 10th first women directors
cur.execute("SELECT name FROM directors WHERE gender = 1")
tenth_woman = cur.fetchall()

## To run the above theory uncomment the below line
# print(f"The tenth female directos {tenth_woman[10][0]}")



##  7.Whare the 3 most popular movies
cur.execute('SELECT title FROM movies ORDER BY popularity DESC LIMIT 3 ')
popular_movies = cur.fetchall()

## To run the above theory uncomment the below line
# print(f"The 3 most popular movies are : {popular_movies[0][0]},{popular_movies[1][0]} and {popular_movies[2][0]}")



##  8.What are the 3 most bankable movie
cur.execute("SELECT title FROM movies ORDER BY budget DESC LIMIT 3")
most_bankble = cur.fetchall()

## To run the above theory uncomment the below line
# print(f"The 3 most bankable movies are : {most_bankble[0][0]},{most_bankble[1][0]} and {most_bankble[2][0]}")



## 9.What is the most awarded average rated movie since the jan 1st, 2000
cur.execute("SELECT original_title FROM movies WHERE release_date > '2000-01-02' ORDER BY vote_average desc limit 1")
most_awarded = cur.fetchall()

## To run the above theory uncomment the below line
# print(f"The most awarded movies are{most_awarded[0][0]}")



## 10.Which movies were directed by Brenda chapman
cur.execute("SELECT original_title FROM movies JOIN directors on directors.id = movies.director_id where name = 'Brenda Chapman'")
directed_by = cur.fetchall()

## To run the above theory uncomment the below line
# print(f"The Movies directed by Branda Chapman is {directed_by[0][0]}")



## 11.name the director who made the most movies
cur.execute("SELECT name FROM directors join movies on movies.director_id = directors.id group by director_id order by count(name) desc limit 1 ")
m = cur.fetchall()

## To run the above theory uncomment the below line
# print(m)



## 12.name of the director who is most bankable
cur.execute("SELECT name FROM directors join movies ON movies.director_id = directors.id GROUP BY director_id ORDER BY sum(movies.budget) DESC LIMIT 1")
bankable = cur.fetchall()

## To run the above theory uncomment the below line
# print(f"The most bankable director is {bankable[0][0]}")



##     second budget analysis:
##Q.tell top 10 hightest budget making movies
cur.execute("SELECT * FROM movies ORDER BY budget DESC limit 10")
top_budget = cur.fetchall()
top_budget = pd.DataFrame(top_budget,columns=['id','original_title','buget','popularity','release_date',
                                    'revenue','title','vote_average','vote_count','overvi','tagline',
                                    'uid','director_id'])

## To run the above theory uncomment the below line
# print(f"{top_budget}")



###     revenue analysis:
## Q.find top 10 revenue making movies
cur.execute("SELECT * FROM movies ORDER BY revenue DESC LIMIT 10")
top_revenue = cur.fetchall()
top_revenue = pd.DataFrame(top_revenue,columns=['id','original_title','buget','popularity','release_date',
                                    'revenue','title','vote_average','vote_count','overvi','tagline',
                                    'uid','director_id'])

## To run the above theory uncomment the below line
# print(top_revenue)


###    voting analysis
## 1.find the most popular movies with hightest vote average

cur.execute("SELECT * FROM movies ORDER BY vote_average DESC LIMIT 10")
most_popular = cur.fetchall()
most_popular = pd.DataFrame(most_popular,columns=['id','original_title','buget','popularity','release_date',
                                    'revenue','title','vote_average','vote_count','overvi','tagline',
                                    'uid','director_id'])

## To run the above theory uncomment the below line
# print(most_popular)


## 2.find all the movies for vote_average and vote_count
cur.execute("SELECT title FROM movies ORDER BY vote_average AND vote_count DESC limit 10 ")
average_count = cur.fetchall()
average_count = pd.DataFrame(average_count)

## To run the above theory uncomment the below line
# print(average_count)



###    director analysis
# Q.name all the directors with number of 
#           movies and revenue where revenue should be taken into accounts for doing the analysis
cur.execute("SELECT name,COUNT(movies.title),SUM(movies.revenue) FROM directors JOIN movies ON directors.id = movies.director_id GROUP BY name ORDER BY sum(movies.revenue) DESC")
directed_by = cur.fetchall()
directed_by = pd.DataFrame(directed_by,columns=['directors_names','movies','top_revenue'])

## To run the above theory uncomment the below line
# print(directed_by)  



##Q.name all the directors with number of 
#       movies and revenue where NO.OF MOVIES SHOULD be taken into accounts for doing the analysis
cur.execute("SELECT name,COUNT(movies.title), SUM(revenue) FROM directors JOIN movies ON directors.id = director_id GROUP BY name ORDER BY count(title) DESC LIMIT 10")
total_movies = cur.fetchall()
total_movies = pd.DataFrame(total_movies,columns=['names','total_movies','total_revenue'])

## To run the above theory uncomment the below line
# print(total_movies)


# give the title of 
#       the movies,release_date,budget,revenue,popularity and vote_average made by steven spielberg
cur.execute("SELECT title,release_date,budget,revenue,popularity,vote_average FROM movies JOIN directors ON directors.id = movies.director_id where directors.name='Steven Spielberg'")
Steven_movies = cur.fetchall()
Steven_movies = pd.DataFrame(Steven_movies,columns=['title','`release_date','budget',
                                                    "revenue",'popularity',"vote_average"])

## To run the above theory uncomment the below line
# print(Steven_movies)








