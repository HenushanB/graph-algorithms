from algorithms.dijkstra import Dijkstra
from graph import Graph


class TravellingSalesman(Graph):
    def __init__(self, adjList, stationCoord) -> None:
        super().__init__(adjList, stationCoord)
        self.createShortestPairsArray()

    def createShortestPairsArray(self):
        self.shortestPairs = {}
        self.shortestPaths = {}
        dijkstraObj = Dijkstra(self.adjList, self.stationCoord)
        for station in dijkstraObj.adjList.keys():
            algorithmOutput = dijkstraObj.runAlgo(station, None)
            self.shortestPairs[station] = algorithmOutput[0]
            self.shortestPaths[station] = algorithmOutput[1]

    def runAlgo(self, start, stopsList):
        stops = stopsList.copy()
        outputPath = [start]
        totalDist = 0
        current = start
        while len(stops) > 0:
            closest = None
            for stop in stops:
                if not closest or (self.shortestPairs[current][stop] <
                                   closest[1]):
                    closest = (stop, self.shortestPairs[current][stop])
            outputPath += (self.shortestPaths[current][closest[0]])[1:]
            totalDist += closest[1]
            current = closest[0]
            stops.remove(current)
        outputPath.append(start)
        outputPath += (self.shortestPaths[current][start])[1:]
        totalDist += self.shortestPairs[current][start]
        print("Most Efficient Path Starting And Ending At Station -> " +
              str(start))
        print("Stopping At Stations: " + str(stopsList))
        print()
        print("Total Distance: " + str(totalDist))
        return (totalDist, outputPath)
