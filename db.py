from py2neo import Graph, Node, Relationship
graph = Graph('http://neo4j:simello@localhost:7474/db/data/')
alice = Node("Person", name="Alice")
bob = Node("Person", name="Bob")
alice_knows_bob = Relationship(alice, "KNOWS", bob)
graph.create(alice_knows_bob)
totti = Node("Person", name="Totti")
alice_fan_of_totti = Relationship(alice, "FAN OF", totti)
graph.create(alice_fan_of_totti)
bob_knows_alice = Relationship(bob, "KNOWS", alice)
graph.create(bob_knows_alice)