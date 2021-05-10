from flask import Flask, render_template, request
from Recommender import get_recommendation
from Recommender import get_description ,get_genre

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def show_index_html():
    return render_template('index.html',movies = [], description= [],Genre= [],length=0)

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        pay = request.form['movie_name']
        # if pay is not "":
        #     return "Empty input. Please Try again."
        # print(pay)
        movies = get_recommendation(pay)
        description =get_description(pay)
        Genre = get_genre(pay)

        return render_template('index.html',movies = movies , description = description,Genre=Genre ,length = 10) 

if __name__ == '__main__':
    app.run(debug=True)