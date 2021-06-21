from flask import Flask

from rick_n_morty.web.blueprint import bp


app = Flask(__name__)
app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(debug=True)
