from flask import Flask
from neo4j import GraphDatabase

app = Flask(__name__)
driver = GraphDatabase.driver("bolt://127.0.0.1:")

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
