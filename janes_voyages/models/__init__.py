from py2neo import Graph
import os

url = os.environ.get('DB_URL', 'http://localhost:7474')
username = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')

graph = Graph(url + '/db/data/', username=username, password=password)

import captain
import location
import note
import ship
import source
import tag
import voyage
import waypoint


















