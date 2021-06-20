import time


class TrafficLight:
    def __init__(self, color=None):
        self.__color = color

    def running(self):
        self.__color = 'red'
        print(f'{self.__color}')
        time.sleep(7)
        self.__color = 'yellow'
        print(f'{self.__color}')
        time.sleep(2)
        self.__color = 'green'
        print(f'{self.__color}')
        time.sleep(7)


traffic_lights = TrafficLight()
traffic_lights.running()
