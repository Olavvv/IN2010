ndatasets = int(input())

def readDatasets(nDatasets):
    datasetInt = []
    datasetStr = []

    for i in range(nDatasets):
        datasetStr = input().split(" ")
        datasetN = int(datasetStr[0])
        datasetStr.remove(datasetStr[0])
        for data in datasetStr:
            datasetInt.append(int(data))
        
        sortDataset(datasetInt, datasetN)

    
    
def sortDataset(dataset, datasetN):
    sorted = []
    counter = 0
    sorted.append(dataset[0])

    k = 0
    for data in dataset:
        for i in range(0, k):
            if (sorted[i] > data):
                pushBack(sorted, i)
        sorted.append(data)







    print(f"{sorted} {counter}")

def pushBack(list, index):
    counter = 0
    returnList = [None]*len(list)
    for i in range(index,len(list) - 1):

readDatasets(ndatasets)

                
                
                