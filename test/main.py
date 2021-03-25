from flask import Flask, render_template
from configparser import ConfigParser

app = Flask(__name__)

@app.route("/")
def index():

    config = ConfigParser()
    config.read('Config.ini',encoding='utf-8')

    data_json = {"title":config.get("html","title")}
    return render_template('index.html',data_json = data_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=9000,debug=True)