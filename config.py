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
sortedMeta=[]
sortedMeta2=[]
mycursor.execute("SELECT title,metascore from `imdb-movie-data` ORDER BY metascore desc")

myresults=mycursor.fetchall()
for i in myresults:
		sortedMeta.append(i[0])
		sortedMeta2.append(i[1])


sortedrate=[]
sortedrate2=[]
mycursor.execute("SELECT title,rating from `imdb-movie-data` ORDER BY rating desc")

myresults=mycursor.fetchall()
for i in myresults:
		sortedrate.append(i[0])
		sortedrate2.append(i[1])



sortedvote=[]
sortedvote2=[]
mycursor.execute("SELECT title,votes from `imdb-movie-data` ORDER BY votes desc")

myresults=mycursor.fetchall()
for i in myresults:
		sortedvote.append(i[0])
		sortedvote2.append(i[1])		


sortedrev=[]
sortedrev2=[]
mycursor.execute("SELECT title,`Revenue (Millions)` from `imdb-movie-data` ORDER BY `Revenue (Millions)` desc")

myresults=mycursor.fetchall()
for i in myresults:
		sortedrev.append(i[0])
		sortedrev2.append(i[1])		




