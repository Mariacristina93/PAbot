from neo4jrestclient.client import GraphDatabase
from GraphPackage import GraphNode as gn
from GraphPackage import GraphRelation as gr

class Neo4jApi:
    gdb = None
    username = None
    pwd = None

    def __init__(self, gdbLink , uName, password):
        self.gdb = GraphDatabase(gdbLink, uName, password)
        self.username = uName
        self.pwd = password

    def getNode(self, labels, name):
        query = "MATCH (a:"+labels+"{name: \""+name+"\"}) RETURN a"
        return gn.GraphNode(self.gdb.query(query)[0][0])

    def getNodeByID(self, linkId):
        id = linkId.split("/")[-1]
        query = "MATCH (a) WHERE ID(a)="+id+" RETURN a"
        return gn.GraphNode(self.gdb.query(query)[0][0])

    def getRelations(self, graphNode):
        query = "MATCH (a:"+ graphNode.getLabel() +"{name: \""+graphNode.getData()["name"]+"\"})-[r]-(b) RETURN r"
        relationsList = []
        for el in self.gdb.query(query):
            relationsList.append(gr.GraphRelation(el[0]))
        return relationsList

    def getRelationsIN(self, graphNode):
        query = "MATCH (a:"+ graphNode.getLabel() +"{name: \""+graphNode.getData()["name"]+"\"})<-[r]-(b) RETURN r"
        relationsList = []
        for el in self.gdb.query(query):
            relationsList.append(gr.GraphRelation(el[0]))
        return relationsList

    def getRelationsOUT(self, graphNode):
        query = "MATCH (a:"+ graphNode.getLabel() +"{name: \""+graphNode.getData()["name"]+"\"})-[r]->(b) RETURN r"
        relationsList = []
        for el in self.gdb.query(query):
            relationsList.append(gr.GraphRelation(el[0]))
        return relationsList

    def getEndNodesByRelationType(self, relationsOutList, relationType):
        endNodes = []
        for el in relationsOutList:
            if el.getType() == relationType:
                endNodes.append(self.getNodeByID(el.getEndID()))
        return endNodes

    def getStartNodesByRelationType(self, relationsInList, relationType):
        startNodes = []
        for el in relationsInList:
            if el.getType() == relationType:
                startNodes.append(self.getNodeByID(el.getStartID()))
        return startNodes

'''myGraph = Neo4jApi("http://localhost:7474/db/data/",'neo4j','passaporto')
startNode = myGraph.getNode("Documentation", "Documentazione passaporto")
outRelations = myGraph.getRelationsIN(startNode)
result = myGraph.getStartNodesByRelationType( outRelations, "REQUIRED")
for el in result:
    el.printNode()'''
    #print("\n ----------------- \n")
#print(str(result[1]))
#myGraph.getNodeByID(result[1][0]["end"]).printNode()
