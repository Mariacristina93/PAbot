class GraphNode:
    id = None
    label = None
    data = None

    def __init__(self,node):
        self.id = node['metadata']['id']
        self.label = node['metadata']['labels'][0]
        self.data = node['data']

    def getId(self):
        return self.id

    def getLabel(self):
        return self.label

    def getData(self):
        return self.data

    def printNode(self):
        print("ID: "+ str(self.id))
        print("LABEL: "+ self.label)
        for el in self.data.keys():
            print(el + ": " + self.data[el])