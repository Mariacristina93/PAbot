from GraphPackage import Neo4jApi as n4j

myGraph = n4j.Neo4jApi("http://localhost:7474/db/data/",'neo4j','passaporto')
startNode = myGraph.getNode("Documentation", "Documentazione passaporto")
outRelations = myGraph.getRelationsIN(startNode)
result = myGraph.getStartNodesByRelationType( outRelations, "REQUIRED")
for el in result:
    el.printNode()
    print("\n ----------------- \n")
#print(str(result[1]))
#myGraph.getNodeByID(result[1][0]["end"]).printNode()
