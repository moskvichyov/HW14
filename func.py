import sqlite3
import json

DB_PATH = 'netflix.db'


def get_movie_title(title):

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sqlite_query = "SELECT `title`, `country`, `release_year`, listed_in as genre, `description` " \
                   "FROM netflix " \
                   f"WHERE `title` ='{title}'" \
                   "ORDER by `release_year` " \
                   "LIMIT 1"
    cur.execute(sqlite_query)
    data_raw = cur.fetchone()

    data = {
        "title": data_raw[0],
        "country": data_raw[1],
        "release_year": data_raw[2],
        "genre": data_raw[3],
        "description": data_raw[4]
    }
    con.close()
    return data


def get_movie_between_years(st, en):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sqlite_query = "SELECT title, release_year " \
                   "FROM netflix " \
                   f"WHERE release_year BETWEEN {st} AND {en} " \
                   "LIMIT 100"
    cur.execute(sqlite_query)
    data = []
    for row in cur.fetchall():
        movie = {
            "title": row[0],
            "release_year": row[1]
        }
        data.append(movie)
    return data


def get_movie_by_rating(rate1, rate2):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sqlite_query = "SELECT title, rating, description " \
                   "FROM netflix " \
                   f"WHERE rating in ('{rate1}', '{rate2}')" \
                   "LIMIT 100"

    cur.execute(sqlite_query)
    data = []
    for row in cur.fetchall():
        movie = {
            "title": row[0],
            "rating": row[1],
            "description": row[2]
        }
        data.append(movie)

    return data


def get_movie_by_genre(genre):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sqlite_query = "SELECT title, rating, description, listed_in as genre, release_year " \
                   "FROM netflix " \
                   f"WHERE genre LIKE '%{genre}%' " \
                   "ORDER by release_year " \
                   "DESC " \
                   "LIMIT 10"

    cur.execute(sqlite_query)
    data = []
    for row in cur.fetchall():
        movie = {
            "title": row[0],
            "rating": row[1],
            "description": row[2],
            "genre": row[3],
            "release_year": row[4]
        }
        data.append(movie)
    con.close()
    return data


def get_movie_by_type_genre_year(movie_type, year, genre):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sqlite_query = "SELECT `title`, `description`, `type`, `release_year`, `listed_in` as genre " \
                   "FROM netflix " \
                   f"WHERE `type` = '{movie_type}' AND `release_year` = '{year}' and `genre` LIKE '%{genre}%' " \
                   "LIMIT 100"

    cur.execute(sqlite_query)
    data = []
    for row in cur.fetchall():
        movie = {
            "title": row[0],
            "description": row[1],
            "type": row[2],
            "release_year": row[3],
            "genre": row[4]
        }
        data.append(movie)

    return data


def get_movie_by_2actors(one,two):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sqlite_query = "SELECT `cast`, `title` " \
                   "FROM netflix " \
                   f"WHERE `cast` LIKE '%{one}%' AND `cast` like '%{two}%'"

    cur.execute(sqlite_query)
    data_raw=cur.fetchone()
    actors = data_raw[0].split(', ')
    actors = set(actors)
    actors.remove(one)
    actors.remove(two)


    return actors










