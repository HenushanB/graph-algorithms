from databuilder.graphBuilder import GraphBuilder
import csv


class Connections(GraphBuilder):
    def __init__(self, filename) -> None:
        super().__init__()
        self.adjList = {}
        self.myData = []
        self.fileName = filename

    def parseCSVData(self,):
        with open(self.fileName, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self.myData.append(row)
            csv_file.close()
        self.myData = self.myData[1:]

    def buildList(self):
        for row in self.myData:
            node1 = int(row[0])
            node2 = int(row[1])
            lineNum = int(row[2])
            weight = int(row[3])
            if node1 in self.adjList:
                count = 0
                for x in self.adjList[node1]:
                    if x[0] == node2:
                        count = 1
                        break
                if count == 0:
                    self.adjList[node1].append([node2, weight, lineNum])
            else:
                self.adjList[node1] = [[node2, weight, lineNum]]
            if node2 in self.adjList:
                count = 0
                for x in self.adjList[node2]:
                    if x[0] == node1:
                        count = 1
                        break
                if count == 0:
                    self.adjList[node2].append([node1, weight, lineNum])
            else:
                self.adjList[node2] = [[node1, weight, lineNum]]

    def returnList(self):
        return self.adjList
