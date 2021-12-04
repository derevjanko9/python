class Stationery:
    def __init__(self, title):
        self.title = title
        self.draw()

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')

stationery_1 = Stationery('пишушая палка')
stationery_2 = Pen('Parker')
stationery_3 = Pencil('Kohinoor')
stationery_4 = Handle('Erich Krause')