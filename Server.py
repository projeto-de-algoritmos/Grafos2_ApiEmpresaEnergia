from flask import Flask
import Grafo
import Dijkstra

app = Flask(__name__)
g = Grafo()

@app.route("/")
def hello_world():
    return "<p>Home page</p>"
