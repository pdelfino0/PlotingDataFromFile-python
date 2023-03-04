import matplotlib.pylab as plt

def loadData (fileName):
    aux = []
    with open(fileName) as csv:
        csv.readline()
        for line in csv:
            for x in range(0,9):
                new = [float(value) for value in line.split(',')]
                aux.append(new)
    return aux

data = loadData("sampledata/california_housing_test.csv")
longitude = [aux[0] for aux in data]
latitude = [aux[1] for aux in data]

#plt.plot(longitude, latitude, 'bo')
plt.scatter(longitude, latitude,s=1)
plt.show()


