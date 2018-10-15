class GraphRelation:
    id = None
    type = None
    data = None
    startID = None
    endID = None

    def __init__(self, relation):
        self.id = relation["metadata"]["id"]
        self.type = relation["metadata"]["type"]
        self.data = relation["data"]
        self.startID = relation["start"].split("/")[-1]
        self.endID = relation["end"].split("/")[-1]

    def getID(self):
        return self.id

    def getType(self):
        return self.type

    def getData(self):
        return self.data

    def getStartID(self):
        return self.startID

    def getEndID(self):
        return self.endID

    def printRelation(self):
        print("ID: " + str(self.id))
        print("TYPE: " + self.type)
        if len(self.data) > 0:
            for el in self.data.keys():
                print(el + ": " + self.data[el])
        print("START_ID: " + str(self.startID))
        print("END_ID: " + str(self.endID))