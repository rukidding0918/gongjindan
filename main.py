from flask import render_template
import flask


app = flask.Flask(__name__)

if __name__ == "__main__":
    with app.app_context():
        html = render_template('base.html')
        with open("index.html", "w") as f:
            f.write(html)