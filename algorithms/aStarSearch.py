from graph import Graph
import math


class AStarSearch(Graph):
    def __init__(self, adjList, stationCoord) -> None:
        super().__init__(adjList, stationCoord)

    def convertLatLongToDist(self, lat1, lat2, long1, long2):
        return math.sqrt((abs(lat1-lat2))**2 + (abs(long1-long2))**2)

    def setUpAStarHeuristic(self, stop):
        self.h = {}
        for data, coord in self.stationCoord.items():
            self.h[data] = self.convertLatLongToDist(coord[0],
                                                     self.stationCoord
                                                     [stop][0],
                                                     coord[1],
                                                     self.stationCoord
                                                     [stop][1])

    def runAlgo(self, start, stop):
        open = set([start])
        # nodes that have been visited and their neighbors have been visited
        closed = set([])

        # set up heuristic data
        self.setUpAStarHeuristic(stop)

        # distances to all other nodes : default is infinity
        distance = {}
        distance[start] = 0

        # adj contains an adjacency mapping of all nodes
        adj = {}
        adj[start] = start

        while len(open) > 0:
            n = None

            # it will find a node with the lowest value of f() -
            for node in open:
                if n is None or (distance[node] + self.h[node] <
                                 distance[n] + self.h[n]):
                    n = node

            if n is None:
                # path doesn't exist
                return None

            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []

                while adj[n] != n:
                    reconst_path.append(n)
                    n = adj[n]

                reconst_path.append(start)

                reconst_path.reverse()

                print("A* Algorithm:")
                print('Path found: {}'.format(reconst_path))
                print()
                return reconst_path

            # for all the neighbors of the current node do
            for node, weight, line in self.adjList[n]:
                # if the current node is not presentin both open and closed
                # add it to open and note n as it's adj
                weight = self.convertLatLongToDist(self.stationCoord[n][0],
                                                   self.stationCoord[node][0],
                                                   self.stationCoord[n][1],
                                                   self.stationCoord[node][1])
                if node not in open and node not in closed:
                    open.add(node)
                    adj[node] = n
                    distance[node] = distance[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update adj data and distance data
                # and if the node was in the closed, move it to open
                else:
                    if distance[node] > distance[n] + weight:
                        distance[node] = distance[n] + weight
                        adj[node] = n

                        if node in closed:
                            closed.remove(node)
                            open.add(node)

            # remove n from the open, and add it to closed
            # because all of his neighbors were inspected
            open.remove(n)
            closed.add(n)

        print('Path does not exist!')
        return None
