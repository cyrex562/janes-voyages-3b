import uuid
from typing import Optional, Set

from py2neo import Node, NodeMatcher, Relationship

from janes_voyages import graph
from janes_voyages.models.note import Note
from janes_voyages.models.tag import Tag
from janes_voyages.models.captain import Captain
from janes_voyages.models.ship import Ship
from janes_voyages.models.source import Source
from janes_voyages.models.waypoint import Waypoint


class Voyage:
    def __init__(self,
                 ship: Ship = None,
                 captain: Captain = None,
                 waypoints: Optional[Set[Waypoint]] = None,
                 sources: Optional[Set[Source]] = None,
                 tags: Optional[Set[Tag]] = None,
                 notes: Optional[Set[Note]] = None):
        self.id = uuid.uuid4().get_hex()
        self.ship = ship
        self.captain = captain
        self.sources = sources
        self.tags = tags
        self.notes = notes
        self.waypoints = waypoints

    def find(self) -> Node:
        nodes = NodeMatcher(graph)
        voyage = nodes.match('Voyage', id=self.id).first()
        return voyage

    def create(self) -> bool:
        if not self.find():
            voyage = Node('Voyage', id=self.id)
            graph.create(voyage)
            return True
        else:
            return False

    def set_ship(self, ship: Ship):
        # TODO remove existing ship
        voyage_node = self.find()
        ship_node = ship.find()
        rel = Relationship(ship_node, "SHIP", voyage_node)
        graph.create(rel)
        self.ship = ship

    def set_captain(self, captain: Captain):
        # TODO remove existing relationship
        voyage_node = self.find()
        captain_node = captain.find()
        self.captain = captain
        rel = Relationship(captain_node, "CAPTAIN_OF", voyage_node)
        graph.create(rel)

    def add_source(self, source: Source):
        voyage_node = self.find()
        source_node = source.find()
        self.sources.add(source)
        rel = Relationship(source_node, "SOURCE", voyage_node)
        graph.create(rel)

    def remove_source(self, source: Source):
        source_node = self.find()
        voyage_node = self.find()
        rel = Relationship(source_node, "SOURCE", voyage_node)
        graph.delete(rel)

    def add_tag(self, tag: Tag):
        tag_node = tag.find()
        self_node = self.find()
        rel = Relationship(tag_node, "TAGS", self_node)
        graph.create(rel)
        self.tags.add(tag)

    def remove_tag(self, tag: Tag):
        tag_node = tag.find()
        self_node = self.find()
        rel = Relationship(tag_node, "TAGS", self_node)
        if graph.exists(rel):
            graph.delete(rel)
            return True
        return False

    def add_waypoint(self, waypoint: Waypoint):
        waypoint_node = waypoint.find()
        self_node = self.find()
        rel = Relationship(waypoint, "WAYPOINT", self_node)
        graph.create(rel)
        self.waypoints.add(waypoint)


