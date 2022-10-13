from abc import ABC, abstractmethod


class GraphBuilder(ABC):
    @abstractmethod
    def parseCSVData(self):
        pass

    @abstractmethod
    def buildList(self):
        pass

    @abstractmethod
    def returnList(self):
        pass
