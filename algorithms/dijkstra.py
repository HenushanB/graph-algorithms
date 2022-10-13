from graph import Graph


class Dijkstra(Graph):
    def __init__(self, adjList, stationCoord) -> None:
        super().__init__(adjList, stationCoord)

    def runAlgo(self, root, end):
        distance = {}
        nodePath = {}
        stationNums = {}
        for x in self.adjList:
            distance[x] = float('inf')
            nodePath[x] = []
            stationNums[x] = []

        distance[root] = 0

        nodeTemp = {root: 0}

        nodePath[root].append(root)

        while nodeTemp:

            currNode = min(nodeTemp, key=lambda k: nodeTemp[k])
            del nodeTemp[currNode]
            for node_dist in self.adjList[currNode]:
                adjnode = node_dist[0]
                weight = node_dist[1]
                line = node_dist[2]
                if distance[adjnode] > distance[currNode] + weight:
                    distance[adjnode] = distance[currNode] + weight
                    nodeTemp[adjnode] = distance[adjnode]
                    # adding the nodes in the path to visualize
                    nodePath[adjnode] = nodePath[currNode] + [adjnode]
                    # tracking transfers
                    stationNums[adjnode] = stationNums[currNode][:]
                    if len(stationNums[adjnode]) == 0 or (stationNums
                                                          [adjnode][-1]
                                                          != line):
                        stationNums[adjnode].append(line)
                # minimum amount of transfers
                elif distance[adjnode] == distance[currNode] + weight:
                    temp = stationNums[currNode]

                    if len(temp) == 0 or temp[-1] != line:
                        temp.append(line)
                    if len(temp) < len(stationNums[adjnode]):
                        stationNums[adjnode] = temp
        if end is not None:
            print("Dijkstra's Algorithm:")
            print("The time it takes: " + str(distance[end]))
            print("The path it travels: " + str(nodePath[end]))
            print("The lines taken: " + str(stationNums[end]))
            print()
            return (distance[end], nodePath[end], stationNums[end])
        else:
            return (distance, nodePath, stationNums)
