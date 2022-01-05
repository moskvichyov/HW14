import sqlite3
from flask import Flask, request, render_template, jsonify
from func import *

app = Flask(__name__)

@app.route('/movie/<title>')
def page_by_title(title):
    movie = get_movie_title(title)
    return jsonify(movie)

@app.route('/movie/<int:st>/<int:en>')
def page_by_year(st, en):
    movie = get_movie_between_years(st, en)
    return jsonify(movie)

@app.route('/rating/<rate1>/<rate2>')
def page_by_rate_g(rate1,rate2):
    movie = get_movie_by_rating(rate1,rate2)
    return jsonify(movie)

@app.route('/genre/<genre>')
def page_by_genre(genre):
    movie = get_movie_by_genre(genre)
    return jsonify(movie)

@app.route('/type/<movie_type>/<year>/<genre>')
def page_by_type(movie_type, year, genre):
    movie = get_movie_by_type_genre_year(movie_type, year, genre)
    return movie

if __name__ == '__main__':
    app.run(debug=True)

