from py2neo import Node, NodeMatcher, Relationship

from janes_voyages import graph
from janes_voyages.models.tag import Tag


class Ship:
    def __init__(self, ship_type='', name='', flag=''):
        self.ship_type = ship_type
        self.name = name
        self.flag = flag
        self.tags = set()

    def find(self) -> Node:
        nodes = NodeMatcher(graph)
        ship = nodes.match('Ship', name=self.name).first()
        return ship

    def create(self) -> bool:
        if not self.find():
            ship = Node('Ship', id=self.id, ship_type=self.ship_type, name=self.name, flag=self.flag)
            graph.create(ship)
            return True
        return False

    def add_tag(self, tag: Tag):
        tag_node = tag.find()
        self_node = self.find()
        rel = Relationship(tag_node, "TAGS", self_node)
        self.tags.add(tag)

    def remove_tag(self, tag: Tag):
        tag_node = tag.find()
        self_node = self.find()
        rel = Relationship(tag_node, "TAGS", self_node)
        if graph.exists(rel):
            graph.delete(rel)
            return True
        return False