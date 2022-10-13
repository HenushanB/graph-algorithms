from databuilder.stations import Stations
from databuilder.connections import Connections
from algorithms.dijkstra import Dijkstra
from algorithms.aStarSearch import AStarSearch

myConnecData = Connections('_dataset/london.connections.csv')
myConnecData.parseCSVData()
myConnecData.buildList()

myStationSet = Stations('_dataset/london.stations.csv')
myStationSet.parseCSVData()
myStationSet.buildList()

dijk = Dijkstra(myConnecData.returnList(), myStationSet.returnList())
astar = AStarSearch(myConnecData.returnList(), myStationSet.returnList())

# Dijktra test cases


def testcase1():
    assert dijk.runAlgo(11, 193) == (6, [11, 83, 193], [3])
    assert astar.runAlgo(11, 193) == [11, 163, 82, 193]


def testcase2():
    assert dijk.runAlgo(11, 11) == (0, [11], [])
    assert astar.runAlgo(11, 11) == [11]


def testcase3():
    assert dijk.runAlgo(1, 302) == (45, [1, 265, 110, 17, 74, 99, 236,
                                         229, 273, 107, 192, 277, 89,
                                         40, 139, 264, 8, 124, 77, 93,
                                         288, 302], [10, 4, 3, 11, 9])
    assert astar.runAlgo(1, 302) == [1, 265, 110, 17, 74, 99, 236, 146,
                                     133, 107, 192, 277, 89, 40, 139,
                                     264, 8, 124, 77, 93, 288, 302]


def testcase4():
    assert dijk.runAlgo(1, 2) == (31, [1, 265, 110, 17, 74, 99, 236, 229,
                                       273, 248, 285, 279, 13, 156, 2],
                                  [10, 4, 3, 7, 12, 2, 3])
    assert astar.runAlgo(1, 2) == [1, 265, 110, 17, 74, 99, 236, 229, 273,
                                   248, 285, 279, 13, 156, 2]


def testcase5():
    assert dijk.runAlgo(1, 210) == (20, [1, 73, 182, 194, 5, 252, 251,
                                         235, 210], [4, 10])
    assert astar.runAlgo(1, 210) == [1, 73, 182, 194, 5, 252, 251, 235, 210]


def testcase6():
    assert dijk.runAlgo(157, 25) == (9, [157, 233, 279, 87, 255, 25],
                                     [7, 1, 3])
    assert astar.runAlgo(157, 25) == [157, 13, 156, 2, 263, 166, 44, 161, 25]


def testcase7():
    assert dijk.numNodes() == 302
    assert astar.numNodes() == 302


def testcase8():
    assert dijk.numEdges() == 349
    assert astar.numEdges() == 349


def testcase9():
    assert dijk.averageDeg() == 2
    assert astar.averageDeg() == 2


def testcase10():
    assert dijk.getNodeDegree(11) == 7
    assert astar.getNodeDegree(11) == 7
