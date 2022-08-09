from flask import Flask, render_template
from api import MovieFetcher

app = Flask(__name__)

#create the pages of site


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/movie_result')
def movie_result():
    movie = MovieFetcher()
    movie.fetch_movie()
    movie_json = movie.as_json()
    return render_template('movie_result.html', movie=movie_json)


if __name__== '__main__':
    app.run() #adding #debug=False still get internal server error