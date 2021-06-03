import uuid
from datetime import datetime
from typing import Set

from py2neo import Node, NodeMatcher, Relationship

from janes_voyages import graph
from janes_voyages.models.tag import Tag
from janes_voyages.models.location import Location


class Waypoint:
    def __init__(self,
                 start_date: datetime,
                 end_date: datetime = None,
                 location: Location = None,
                 waypoint_type: str = "",
                 tags: Set[Tag] = None):
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.waypoint_type = waypoint_type
        self.tags = tags
        self.id = uuid.uuid4().get_hex()

    def find(self) -> Node:
        nodes = NodeMatcher(graph)
        node = nodes.match('Waypoint', id=self.id)
        return node

    def create(self) -> bool:
        if not self.find():
            node = Node('Waypoint',
                        start_date=str(self.start_date),
                        end_date=str(self.end_date),
                        waypoint_type=self.waypoint_type,
                        id=self.id)
            graph.create(node)
            return True
        return False

    def set_start_date(self, start_date: datetime):
        self.start_date = start_date
        node = self.find()
        if node is not None:
            node['start_date'] = str(start_date)
            graph.merge(node)

    def set_end_date(self, end_date: datetime):
        self.end_date = end_date
        node = self.find()
        if node is not None:
            node['end_date'] = str(end_date)
            graph.merge(node)

    def set_location(self, location: Location):
        self.location = location
        node = self.find()
        location_node = location.find()
        rel = Relationship(location_node, "LOCATION", node)
        