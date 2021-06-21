import os
import random as r

import flask as f
from pymongo import MongoClient

import config
from .. import api
from . import quotes


bp = f.Blueprint("RnM", __name__,
                 template_folder=os.path.join(os.path.dirname(__file__), "templates"))
random = r.Random()


def mongo_conn():
    with MongoClient(config.mongo['connection_url']) as client:
        db = client[config.mongo['db_name']]
        yield (client, db)


@bp.route("/")
def index():
    for (_, db) in mongo_conn():
        filters = {"$where": "this.episode.length >= 3", "status": {"$in": ["Dead", "Alive"]}}
        males = list(db.characters.find(dict(gender='Male', **filters)))
        females = list(db.characters.find(dict(gender='Female', **filters)))

    try:
        male = random.choice(males)
        female = random.choice(females)

        male['eps'] = api.get_episodes_for_character(male)
        female['eps'] = api.get_episodes_for_character(female)

    except IndexError:
        male, female = None, None

    return f.render_template("index.html", quote=quotes.get_quote(), male=male, female=female)


@bp.route("/db")
def db():
    for (_, db) in mongo_conn():
        template_data = {"num_chars": db.characters.count_documents({})}

    return f.render_template('db.html', **template_data)


@bp.route("/db/feed")
def feed_db():
    @f.stream_with_context
    def stream(all_characters):
        for (_, db) in mongo_conn():
            res = db.characters.delete_many({})

            if res.deleted_count > 0:
                yield f"Deletados: {res.deleted_count}<br>"

            for (i, c) in enumerate(all_characters, 1):
                res = db.characters.insert_one(c)
                yield f"Objeto {res.inserted_id} inserido. ({i}) "

        yield f"""<br><script>location.replace('{f.url_for('RnM.index')}')</script>"""

    return f.Response(stream(api.get_all_characters()))
