# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
		https://colab.research.google.com/drive/1LWVvujoU2GF-SNTVCyCAIGM03F5ApN8j
"""

# Movie-Recomendation system

#import libaries

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from config import *
import difflib

#Loading Data
# from google.colab import files
# uploaded = files.upload()
#Storing Data
#db = pd.read_csv('IMDB-Movie-Data.csv')
#adding a new column Movie-Id
#db['Movie_id'] = range(0,1000)
#db['Genre']=db['Genre'].str.replace(',',' ',regex=True)
#showing data
#db.head()

#get a count of the number of rows/movies in the dataset
#db.shape

#Listing important columns
columns=['Actors','Director','Genre','Title','Description']
#showing the import columns
# db[columns].head(3)

#checking for any missing values in the important columns
#db[columns].isnull().any()

#coming the values of the important column into a single string
def get_important_features(actor,director,description,genre,title):
	important_features = []
	for i in range(0,len(actor)):
		important_features.append(actor[i]+' '+director[i]+' '+genre[i]+' '+title[i]+' '+description[i])

	return important_features

#creating a column to hold the combine string
important_features= get_important_features(actor,director,description,genre,title)

# print ("yeah----------------------------------------",important_features)
#show the data
#db.head(20)

#covert the text to matrix
cm=CountVectorizer().fit_transform(important_features)

#Get the cosine similarity matrix 
cs=cosine_similarity(cm)
#printing the cosine similarity matrix
# print(cs)

#get the shape of cosine similarity matrix
# cs.shape

#get the title  user like
# title= input("Enter a movie name: ")

#finding the movies id from title
def get_recommendation(Title):
	try:
		Movie_id= title.index(Title)
	except:
		return ['no result found please check for spelling']
	#create a list enumeration for similarity score
	print("------------",title[Movie_id])
	scores = list(enumerate(cs[Movie_id]))

	#sorting the list
	sorted_scores = sorted(scores,key =lambda x:x[1], reverse= True)

	sorted_scores=sorted_scores[1:]

	#printing the sorted scores
	# print(sorted_scores)

	# printing first 10 similar movies

	j=0
	movie_names = []
	# print("The recommended movies for "+ title +" are as follows")
	for item in sorted_scores:
		movies_title =title[item[0]]
		movie_names.append(movies_title)
		j+=1
		if j>10:
			break
	return movie_names
#for UI
def get_description(Title):
	desc= []
	try:
		Movie_id= title.index(Title)
	except:
		return ['SORRY! No `result found please check for spelling or movie might not exist in database`']

	#create a list enumeration for similarity score

	scores = list(enumerate(cs[Movie_id]))

	#sorting the list
	sorted_scores = sorted(scores,key =lambda x:x[1], reverse= True)

	sorted_scores=sorted_scores[1:]

	#printing the sorted scores
	# print(sorted_scores)

	# printing first 10 similar movies

	j=0
	movie_names = []
	# print("The recommended movies for "+ title +" are as follows")
	for item in sorted_scores:
		movies_title =description[item[0]]
		desc.append(movies_title)
		j+=1
		if j>10:
			break
	return desc
	
def top_pick(choice):
		picks= []
		final = []
		z=[]
		if(choice=='Metascore'):
			picks=metascore
			z = [x for _,x in sorted(zip(metascore,title),reverse= True)]
			picks.sort(reverse= True)
			# print(picks)
		if(choice=='Votes'):
			picks = votes
			z = [x for _,x in sorted(zip(votes,title),reverse= True)]
			picks.sort(reverse=True)
		if(choice=='Rating'):
			picks = rating
			z = [x for _,x in sorted(zip(rating,title),reverse= True)]
			picks.sort(reverse=True)
		if(choice=='Revenue (Millions)'):
			picks = revenue
			z = [x for _,x in sorted(zip(revenue,title),reverse= True)]
			picks.sort(reverse=True)
		for i in range(9):
			final.append(z[i])
		
		return final,picks
def get_genre(Title):
	
	try:
		Movie_id= title.index(Title)
	except:
		return []

	#create a list enumeration for similarity score

	scores = list(enumerate(cs[Movie_id]))

	#sorting the list
	sorted_scores = sorted(scores,key =lambda x:x[1], reverse= True)

	sorted_scores=sorted_scores[1:]

	#printing the sorted scores
	# print(sorted_scores)

	# printing first 10 similar movies

	j=0
	Genre = []
	# print("The recommended movies for "+ title +" are as follows")
	for item in sorted_scores:
		movies_title =genre[item[0]]
		Genre.append(movies_title)
		j+=1
		if j>10:
			break
	return Genre

