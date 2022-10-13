from databuilder.graphBuilder import GraphBuilder
import csv


class Stations(GraphBuilder):

    def __init__(self, filename) -> None:
        super().__init__()
        self.fileName = filename
        self.stationCoord = {}
        self.myData = []

    def parseCSVData(self,):
        with open(self.fileName, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self.myData.append(row)
            csv_file.close()
        self.myData = self.myData[1:]

    def buildList(self):
        for row in self.myData:
            station = int(row[0])
            x = float(row[1])
            y = float(row[2])
            self.stationCoord[station] = [x, y]

    def returnList(self):
        return self.stationCoord
