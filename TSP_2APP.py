#Project Group 16
#12AUG17 as of 121632JUL17
#TSP
#2-app algorithm for the traveling sales person

import sys
import math
import copy

#city class for creating initial array to store city data
class City:
    def __init__(self, number, xCoord, yCoord):
        self.cityName = number
        self.x = xCoord
        self.y = yCoord
        self.key = float('inf')
        self.pred = None

#read data from provided file and store city info as arguements in city array.
def readFile(fileName):
    file = fileName + '.txt'
    with open(file) as data:
        cityArray = []
        for line in data:
            line = line.split() # to deal with blank
            if line:            # lines (take the line and grab individual elements in value)
                cityInfo = []
                for value in line:
                    cityInfo.append(value)
                city = City(int(cityInfo[0]), int(cityInfo[1]), int(cityInfo[2])) #create a new object
                cityArray.append(city)  #append the object to the city array
    return cityArray

def extractMin(array):
    city = -6
    index = -6
    minU = float('inf')
    for i in range(len(array)):
        if array[i].key < minU:
            city = array[i].cityName
            minU = array[i].key
            index = i
    return city, index

#write file
def writeFile(fileName, array):
    file = fileName + 'TEST' + '.txt' + '.tour'
    with open(file, 'w') as outPutFile:
        for val in array:
            num = str(val)
            outPutFile.write(num + "\n")

def tour(mst):
    tourArray=[]
    for i in range(len(mst)):
        tourArray.append(mst[i].cityName)
    return tourArray

#compute distance between two cities
def distance(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    return int(round(math.sqrt(dx*dx + dy*dy)))

def checkNQ(Q, cityName):
    index = -6
    exists = False
    for i in range(len(Q)):
        if Q[i].cityName == cityName:
            exists = True
            index = i
    return exists, index

#compute tour distance
def tourDistance(cityArray, tour):
        dist = 0
        for i in range(len(cityArray)-1):  #the -1 remedies out or range errors, no allowing you to calculate a distance from the last city
            dist = dist + distance(cityArray[tour[i]].x,cityArray[tour[i]].y,cityArray[tour[i+1]].x, cityArray[tour[i+1]].y)
        lfCity = distance(cityArray[tour[0]].x, cityArray[tour[0]].y, cityArray[tour[-1]].x, cityArray[tour[-1]].y)  #add in distance from first to last.
        dist += lfCity
        return dist

def MST_PRIM(cityArray, Q):
    A=[]
    cityArray[0].key = 0
    Q[0].key = 0
    while len(Q)!=0:
        u, index = extractMin(Q)
        A.append(Q[index])
        del Q[index]
        for i in range(len(cityArray)):
            d = distance(cityArray[i].x, cityArray[i].y, cityArray[u].x, cityArray[u].y)
            inQ, idx = checkNQ(Q, cityArray[i].cityName)
            if inQ and (d < Q[idx].key):
                 Q[idx].pred = u
                 Q[idx].key = d
    return A

def main():
    fileName = sys.argv[1]
    cityArray = readFile(fileName)
    Q = readFile(fileName)
    finalDistance = float('inf')
    minSpanTree = MST_PRIM(cityArray, Q)
    optTour = tour(minSpanTree)
    optTourDist = tourDistance(cityArray,optTour)
    optTour.insert(0,optTourDist)
    # print(optTourDist)
    # for i in range(len(optTour)):
    #      print(optTour[i])
    writeFile(fileName,optTour)

if __name__ == "__main__":
    main()
