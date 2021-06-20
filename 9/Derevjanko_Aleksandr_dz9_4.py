class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print(f'машина повернула {direction}')

    def show_speed(self):
        print(f'скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed < 60:
            print(f'скорость автомобиля {self.speed}')
        else:
            print(f'скорость автомобиля {self.speed}\nпревышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed < 40:
            print(f'скорость автомобиля {self.speed}')
        else:
            print(f'скорость автомобиля {self.speed}\nпревышение скорости')


class PoliceCar(Car):
    pass


car_1 = Car(120, 'white', 'Mazda RX-8', False)
car_2 = TownCar(120, 'white', 'Mazda RX-8', False)
car_3 = WorkCar(120, 'white', 'Mazda RX-8', False)
car_4 = PoliceCar(120, 'white', 'Mazda RX-8', True)
print(car_1.name)
car_1.go()
car_1.turn('направо')
car_1.show_speed()
car_1.stop()
print(car_2.name)
car_2.go()
car_2.turn('направо')
car_2.show_speed()
car_2.stop()
print(car_3.name)
car_3.go()
car_3.turn('направо')
car_3.show_speed()
car_3.stop()
print(car_4.name)
car_4.go()
car_4.turn('направо')
car_4.show_speed()
car_4.stop()
