import mysql.connector

mydb=mysql.connector.connect(
	 host="127.0.0.1",
	 user="root",
	 password="",
	 database="movie"
 )
 
mycursor=mydb.cursor()
mycursor.execute("SELECT title FROM `imdb-movie-data`")

myresults=mycursor.fetchall()

title=[]
genre=[]
description=[]
actor=[]
director=[]
movie_id=[]
rating=[]
votes=[]
revenue=[]
metascore=[]
#geting data for title
for i in myresults:
	title.append(i[0])

mycursor.execute("SELECT genre FROM `imdb-movie-data`")

myresults=mycursor.fetchall()
for i in myresults:
	genre.append(i[0])

mycursor.execute("SELECT description FROM `imdb-movie-data`")

myresults=mycursor.fetchall()
for i in myresults:
	description.append(i[0])

mycursor.execute("SELECT actors FROM `imdb-movie-data`")

myresults=mycursor.fetchall()
for i in myresults:
	actor.append(i[0])

mycursor.execute("SELECT director FROM `imdb-movie-data`")

myresults=mycursor.fetchall()
for i in myresults:
	director.append(i[0])
	
mycursor.execute("SELECT rank as movieId FROM `imdb-movie-data`")

myresults=mycursor.fetchall()
for i in myresults:
	movie_id.append(i[0])

mycursor.execute("SELECT Rating  FROM `imdb-movie-data`")

myresults=mycursor.fetchall()
for i in myresults:
	rating.append(i[0])

mycursor.execute("SELECT Votes FROM `imdb-movie-data`")

myresults=mycursor.fetchall()
for i in myresults:
	votes.append(i[0])

mycursor.execute("SELECT `Revenue (Millions)` FROM `imdb-movie-data`")

myresults=mycursor.fetchall()
for i in myresults:
	revenue.append(i[0])
	mycursor.execute("SELECT Metascore FROM `imdb-movie-data`")

	myresults=mycursor.fetchall()
	for i in myresults:
		metascore.append(i[0])

 