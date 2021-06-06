from flask import Flask, render_template, request
from Recommender import get_recommendation
from Recommender import get_description ,get_genre
from Recommender import top_pick

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def show_index_html():
    top_rated=[]
    top_rated,num=top_pick('Rating')
    return render_template('index.html',movies = [], description= [],Genre= [],length=0, top_rated=top_rated,num=num)

@app.route('/he',methods = ['POST'])
def show_index_htm():
    choice = request.form['filter']
    top_rated,num=top_pick(choice)
    return render_template('index.html',movies = [], description= [],Genre= [],length=0, top_rated=top_rated,num=num)

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        movie_name = request.form['movie_name']
        movies = get_recommendation(movie_name)
        description =get_description(movie_name)
        Genre = get_genre(movie_name)

        return render_template('index.html',movies = movies , description = description,Genre=Genre ,length = 10,top_rated=[]) 
        
if __name__ == '__main__':
    app.run(debug=True)