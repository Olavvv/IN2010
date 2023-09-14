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
    sorted = dataset
    counter = 0
    for i in range(len(sorted) - 1):
        k = i
        for j in range(i+1, len(sorted)):
            if sorted[j] < sorted[k]:
                k = j
        if i != k:
            counter += i
            sorted[i], sorted[k] = sorted[k], sorted[i]
    print(f"{sorted} {counter}")

readDatasets(ndatasets)

                
                
                