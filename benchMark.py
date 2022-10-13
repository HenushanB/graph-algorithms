import matplotlib.pyplot as plt
import csv
import math
import time


class Benchmark():
    def __init__(self) -> None:
        self.CSV_DISTANCES_FILE = '_benchMarkFiles/distBetweenStations.csv'
        self.BENCH_MARK_OUPUT_FILE = '_benchMarkFiles/benchMarkOutput.csv'
        self.DATA_POINT_MULTIPLIER = 20
        self.dataMapping = {}

    def parseCSVData(self, fileName):
        myData = []
        with open(fileName, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                myData.append(row)
            csv_file.close()

        return myData[1:]

    def deg2rad(self, deg):
        return deg * (math.pi/180)

    def getDistanceFromLatLongMeter(self, lat1, lon1, lat2, lon2):
        R = 637  # Radius of the earth in km
        dLat = self.deg2rad(lat2 - lat1)
        dLon = self.deg2rad(lon2 - lon1)
        a = (math.sin(dLat / 2) * math.sin(dLat / 2) +
             math.cos(self.deg2rad(lat1)) * math.cos(self.deg2rad(lat2)) *
             math.sin(dLon / 2) * math.sin(dLon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = R * c  # Distance in km
        return d * 1000  # Distance in m

    def getDistancesBetweenNodes(self, nodes):
        outputFile = open(self.CSV_DISTANCES_FILE, 'w', newline='')
        writer = csv.writer(outputFile)
        shortestDist = None
        longestDist = None
        keys = list(nodes.keys())
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                node = keys[i]
                destination = keys[j]
                dist = self.getDistanceFromLatLongMeter(nodes[node][0],
                                                        nodes[node][1],
                                                        nodes[destination][0],
                                                        nodes[destination][1])
                if shortestDist is None or dist < shortestDist:
                    shortestDist = dist
                if longestDist is None or dist > longestDist:
                    longestDist = dist
                writer.writerow([node, destination, dist])
        outputFile.close()
        print(shortestDist)
        print(longestDist)

    def buildBenchMarkHashMap(self):
        distancesData = self.parseCSVData(self.CSV_DISTANCES_FILE)
        for row in distancesData:
            newIndex = int(math.ceil(float(row[2])/self.DATA_POINT_MULTIPLIER))
            if newIndex in self.dataMapping:
                self.dataMapping[newIndex].append(row)
            else:
                self.dataMapping[newIndex] = [row]

    def performBenchMark(self, dijObk, aStarObj):
        outputFile = open(self.BENCH_MARK_OUPUT_FILE, 'w', newline='')
        writer = csv.writer(outputFile)
        MIN_DATAPOINTS = 20
        for key, distRange in self.dataMapping.items():
            nextLineOuput = [(key*self.DATA_POINT_MULTIPLIER)]
            loopCounter = 0
            while loopCounter < MIN_DATAPOINTS:
                for dataPoint in distRange:
                    startTime = time.time()
                    dijObk.runAlgo(int(dataPoint[0]), int(dataPoint[1]))
                    stopTime = time.time()
                    nextLineOuput.append((stopTime - startTime)*1000)
                    startTime = time.time()
                    aStarObj.runAlgo(int(dataPoint[0]), int(dataPoint[1]))
                    stopTime = time.time()
                    nextLineOuput.append((stopTime-startTime)*1000)
                    loopCounter += 1
            writer.writerow(nextLineOuput)
        outputFile.close()

    def split_integer(self, num, divisor):
        current = divisor
        returnList = [0]
        while current <= num:
            returnList.append(current)
            current += divisor
        return returnList

    def createBenchMarkGraphs(self):
        benchMarkData = self.parseCSVData(self.BENCH_MARK_OUPUT_FILE)
        for i in range(len(benchMarkData)):
            benchMarkData[i][0] = int(benchMarkData[i][0])
        benchMarkData.sort()
        x = []
        dijkstraY = []
        aStarY = []
        maxX = None
        for row in benchMarkData:
            dataPoints = 0
            dijkstraSum = 0
            aStarSum = 0
            firstValue = True
            algoToggle = True
            for value in row:
                if not firstValue:
                    if algoToggle:
                        dijkstraSum += float(value)
                        dataPoints += 1
                    else:
                        aStarSum += float(value)
                    algoToggle = not algoToggle
                else:
                    firstValue = False
            x.append(row[0])
            if maxX is None or row[0] > maxX:
                maxX = row[0]
            dijkstraY.append(dijkstraSum/dataPoints)
            aStarY.append(aStarSum/dataPoints)
        plt.xticks(self.split_integer(maxX, 1000))
        plt.plot(x, dijkstraY, label="Dijkstra")
        plt.plot(x, aStarY, label="A*")
        plt.xlabel('Approximate Distance Between Stations (Meters)')
        plt.ylabel('Algorithm Running Time (Milliseconds)')
        runTime = "Running Time Comparison : "
        algos = "Dijkstra Algorithm vs A* Algorithm"
        plt.title(runTime + algos)
        plt.legend()
        plt.show()
