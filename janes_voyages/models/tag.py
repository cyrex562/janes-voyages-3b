from py2neo import Node, NodeMatcher

from janes_voyages import graph


class Tag:
    def __init__(self, value: str):
        self.value = value

    def find(self) -> Node:
        nodes = NodeMatcher(graph)
        tag = nodes.match('Tag', value=self.value).first()
        return tag

    def create(self) -> bool:
        if not self.find():
            tag = Node('Tag', value=self.value)
            graph.create(tag)
            return True
        return False