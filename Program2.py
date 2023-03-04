import folium

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

map = folium.Map(location=[36.7783, -119.4179],zoom_start=6, min_zoom=5)

for aux in data:
    folium.CircleMarker(radius=1, location=[aux[1], aux[0]]).add_to(map)

map
    
    

