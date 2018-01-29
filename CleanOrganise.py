import requests, json

class CleanOrganise:
    dataFromFile = []
    organisedData = []


    def __init__(self,d):
        self.dataFromFile = d

    def inObj (self,queryValue):
        pos = 0
        if (len(self.organisedData) == 0):
            return False,pos
        for data in self.organisedData:
            if data[0] == queryValue:
                return True,pos
            pos += 1
        return False,pos

    def addInObj (self,newValue):
        self.organisedData.append([newValue,1])

    def updateCount (self,pos):
        self.organisedData[pos][1] += 1

    def groupStationID (self,groupValue):
        boolVal,pos = self.inObj(groupValue)
        if not boolVal:
            self.addInObj(groupValue)
        else:
            self.updateCount(pos)


    def cleanData(self,dataValue):
        self.organisedData = []
        for item in self.dataFromFile:
            self.groupStationID(item[dataValue])
        print(self.organisedData)
