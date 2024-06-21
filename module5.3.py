class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType


    def __eq__(self, other):
        return isinstance(other, Building) and self.buildingType == other.buildingType \
               and self.numberOfFloors == other.numberOfFloors



h1 = Building (18, 'ЖК Солнечный')
h2 = Building (18, 'ЖК Солнечный')
print(h1 == h2)