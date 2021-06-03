from py2neo import Node, NodeMatcher

from janes_voyages import graph


class Location:
    def __init__(self, name:str="", latitude:float=0.0, longitude:float=0.0, location_type:str=""):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.location_type = location_type

    def find(self) -> Node:
        nodes = NodeMatcher(graph)
        node = nodes.match('Location', name=self.name).first()
        return node

    def create(self) -> bool:
        if not self.find():
            node = Node('Location', name=self.name, latitude=self.latitude, longitude=self.longitude, location_type=self.location_type)
            graph.create(node)
            return True
        return False