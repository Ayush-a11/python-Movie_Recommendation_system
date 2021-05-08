from flask import Flask, render_template, request
from Recommender import get_recommendation
from Recommender import get_description

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def show_index_html():
    return render_template('index.html', headings = {}, data = {})

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        pay = request.form['movie_name']
        # if pay is not "":
        #     return "Empty input. Please Try again."
        # print(pay)
        movies = get_recommendation(pay)
        description =get_description(pay)
        # print(description)
        # a, b =     
        # a, b = F()
        # a = ["A", "B", "C"]
        # b = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
        return render_template('index.html',movies = movies , description = description)

if __name__ == '__main__':
    app.run(debug=True)