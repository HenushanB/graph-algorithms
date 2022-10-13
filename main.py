from algorithms.connectedComponents import ConnectedComponents
from algorithms.travellingSalesman import TravellingSalesman
from databuilder.stations import Stations
from databuilder.connections import Connections
from algorithms.dijkstra import Dijkstra
from algorithms.aStarSearch import AStarSearch


def main():
    # parsing data from connections.csv and creating adjList
    myConnecData = Connections('_dataset/london.connections.csv')
    myConnecData.parseCSVData()
    myConnecData.buildList()

    # parsing data from stations.csv
    myStationSet = Stations('_dataset/london.stations.csv')
    myStationSet.parseCSVData()
    myStationSet.buildList()

    # finding the shortest path
    dijk = Dijkstra(myConnecData.returnList(), myStationSet.returnList())
    astar = AStarSearch(myConnecData.returnList(), myStationSet.returnList())
    connecComp = ConnectedComponents(myConnecData.returnList(),
                                     myStationSet.returnList())
    traveller = TravellingSalesman(myConnecData.returnList(),
                                   myStationSet.returnList())

    dijk.runAlgo(157, 25)
    astar.runAlgo(157, 25)
    zone1 = myStationSet.returnList()
    zone1 = set(zone1)
    print(connecComp.runAlgo(zone1))
    print()
    print(traveller.runAlgo(11, [25, 32, 200, 193, 17, 9]))
    print(dijk.numEdges())
    print(dijk.getNodeDegree(11))


if __name__ == "__main__":
    main()
