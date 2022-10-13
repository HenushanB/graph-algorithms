class Graph():
    def __init__(self, adjList, stationCoord) -> None:
        self.adjList = adjList
        self.stationCoord = stationCoord
        self.nodeDegree = {}  # key: node, value: degree of node
        self.degreeDistribution = {}
        self.buildNodeDegree()
        self.buildDistribution()

    def buildDistribution(self):
        for x in self.nodeDegree:
            if self.nodeDegree[x] not in self.degreeDistribution:
                self.degreeDistribution[self.nodeDegree[x]] = 0.5
            else:
                self.degreeDistribution[self.nodeDegree[x]] += 0.5

    def buildNodeDegree(self):
        for x in self.adjList:
            self.nodeDegree[x] = len(self.adjList[x])

    def numNodes(self):
        return len(self.stationCoord)

    def getNodeDegree(self, node):
        return self.nodeDegree[node]

    def averageDeg(self):
        avg = 0
        for x in self.nodeDegree:
            avg += self.nodeDegree[x]

        return int(avg/len(self.nodeDegree))

    def numEdges(self):
        total = 0
        for x in self.adjList:
            total += len(self.adjList[x])

        return total // 2

    def returnDistribution(self):
        return self.degreeDistribution
