from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

jsonFile = open('newsHack.json', encoding='utf8', errors='ignore')
posts = json.load(jsonFile)


@app.route('/')
@app.route('/home')
def index():
    return render_template('tajanews.html', newsHaru=posts)


if __name__ == '__main__':
    app.run(debug=True)
