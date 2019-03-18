import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return '''Home'''

g_id_counter = 1
def make_id(g_id_counter):
    g_id_counter += 1
    return g_id_counter

@app.route('/v1/post', methods=['GET', 'POST'])
def post():
    conn = sqlite3.connect('posts.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    if flask.request.method == 'POST':
        text_id = make_id(g_id_counter)
        text = request.form['text']
        parent = request.form['parent']
        print("text", text)
        print("id", text_id)
        print("p", parent)
        print("---------")
        cur.execute('INSERT INTO posts (id, text, parent) VALUES (?, ?, ?);',
                    (text_id, text, parent))
        conn.commit()
        return '''PUT''' #TODO: should be proper response

    if flask.request.method == 'GET':
        all_posts = cur.execute('SELECT * FROM posts;').fetchall()
        return jsonify(all_posts)

    return '''Invalid'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()
