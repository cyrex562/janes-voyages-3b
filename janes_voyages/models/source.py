from py2neo import Node, NodeMatcher, Relationship

from janes_voyages import graph
from janes_voyages.models.tag import Tag


class Source:
    def __init__(self, name:str = ''):
        self.name = name
        self.tags = set()

    def find(self) -> Node:
        nodes = NodeMatcher(graph)
        source = nodes.match('Source', name=self.name).first()
        return source

    def create(self) -> bool:
        if not self.find():
            source = Node('Source', name=self.name)
            graph.create(source)
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