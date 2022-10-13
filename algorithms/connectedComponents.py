from graph import Graph


class ConnectedComponents(Graph):
    def __init__(self, adjList, stationCoord) -> None:
        super().__init__(adjList, stationCoord)

    def recursiveDFS(self, components, v, visited, setOfNodes):
        visited[v] = True
        components.append(v)

        for neighbour in self.adjList[v]:
            node = neighbour[0]
            if visited[node] is False and node in setOfNodes:
                components = self.recursiveDFS(components, node, visited,
                                               setOfNodes)

        return components

    def runAlgo(self, setOfNodes):
        visited = {}
        for x in self.stationCoord:
            visited[x] = False

        connectedComponents = []

        for v in setOfNodes:
            if visited[v] is False:
                components = []
                components = self.recursiveDFS(components, v, visited,
                                               setOfNodes)
                connectedComponents.append(components)

        return connectedComponents
