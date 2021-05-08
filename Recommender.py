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

#Loading Data
# from google.colab import files
# uploaded = files.upload()

#Storing Data
db = pd.read_csv('IMDB-Movie-Data.csv')
#adding a new column Movie-Id
db['Movie_id'] = range(0,1000)
#showing data
db.head()

# Commented out IPython magic to ensure Python compatibility.
#EDA
#importing labaries for visualization
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style('white')
# %matplotlib inline



#get a count of the number of rows/movies in the dataset
db.shape

#Listing important columns
columns=['Actors','Director','Genre','Title','Description']

#showing the import columns
db[columns].head(3)

#checking for any missing values in the important columns
db[columns].isnull().any()

#comining the values of the important column into a single string
def get_important_features(data):
	important_features = []
	for i in range(0,data.shape[0]):
		important_features.append(data['Actors'][i]+' '+data['Director'][i]+' '+data['Genre'][i]+' '+data['Title'][i]+' '+data['Description'][i])

	return important_features

#creating a column to hold the combine string
db['important_features']= get_important_features(db)

#show the data
db.head(20)

#covert the text to matrix
cm=CountVectorizer().fit_transform(db['important_features'])

#Get the cosine similarity matrix 
cs=cosine_similarity(cm)
#printing the cosine similarity matrix
# print(cs)

#get the shape of cosine similarity matrix
# cs.shape

#get the title  user like
# title= input("Enter a movie name: ")

#finding the movies id from title
def get_recommendation(title):
	movie_id= db[db.Title == title]['Movie_id'].values[0]

	#create a list enumeration for similarity score

	scores = list(enumerate(cs[movie_id]))

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
		movies_title =db[db.Movie_id == item[0]]['Title'].values[0]
		movie_names.append(movies_title)
		j+=1
		if j>10:
			break
	return movie_names

def get_description(title):
	desc= []
	movie_id= db[db.Title == title]['Movie_id'].values[0]

	#create a list enumeration for similarity score

	scores = list(enumerate(cs[movie_id]))

	#sorting the list
	sorted_scores = sorted(scores,key =lambda x:x[1], reverse= True)

	sorted_scores=sorted_scores[1:]

	#printing the sorted scores
	# print(sorted_scores)

	# printing first 10 similar movies

	j=0
	movie_names = []
	# print("The recomended movies for "+ title +" are as follows")
	for item in sorted_scores:
		movies_title =db[db.Movie_id == item[0]]['Description'].values[0]
		desc.append(movies_title)
		j+=1
		if j>10:
			break
	return desc

print(get_description('Fury'))