from collections import Counter
import csv
import statistics

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

n = []
for i in range(len(fileData)):
  num = fileData[i][1]
  n.append(float(num))

def getMean():
    h=statistics.mean(n)
    print("mean:", h)
getMean()

def getMedian():
    v= statistics.median(n)
    print("median: ", v)
getMedian()

def getMode():
    g = statistics.multimode(n)
    print("mode", g)
getMode()
