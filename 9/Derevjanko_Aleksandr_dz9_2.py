class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_of_asphalt(self):
        weight = self._length * self._width * 0.025 * 5
        return f'{int(weight)} т'


road_1 = Road(20, 5000)
print(road_1.weight_of_asphalt())
