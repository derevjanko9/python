import random


class LotoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [[], [], []]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        need_spaces = 4
        need_numbers = 5
        self._numbers = random.sample(range(1, self._MAX_NUMBER), self._MAX_NUMBER_IN_CARD)
        for line in self._card:
            for _ in range(need_spaces):
                line.append(' ')
            for _ in range(need_numbers):
                line.append(self._numbers.pop())

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)


class LotoGame:
    def __init__(self, player, machine):
        self.player = player
        self.computer = machine
        self.cask = [number for number in range(1, (self.player._MAX_NUMBER + 1))]

    def start(self):
        print(f'{self.player}_______________')
        for line in self.player._card:
            print(" ".join([str(item) for item in line]))
        print(f'{self.computer}_______________')
        for line in self.computer._card:
            print(" ".join([str(item) for item in line]))
        while True:
            cask_1 = self.cask.pop(random.randint(0, (len(self.cask) - 1)))
            for index, line in enumerate(self.computer._card):
                for i in range(len(line)):
                    if isinstance(line[i], int):
                        if line[i] == cask_1:
                            self.computer._card[index][i] = '-'
            person = input(f'Есть число {cask_1} в Вашей карточке: y/n')
            count_1 = self.player._card[0].count(cask_1)
            count_2 = self.player._card[1].count(cask_1)
            count_3 = self.player._card[2].count(cask_1)
            if person == 'y' and count_1 + count_2 + count_3 == 0:
                print('Вы проиграли')
                break
            elif person == 'y' and count_1 + count_2 + count_3 == 1:
                for index, line in enumerate(self.player._card):
                    for i in range(len(line)):
                        if isinstance(line[i], int):
                            if line[i] == cask_1:
                                self.player._card[index][i] = '-'
            elif person == 'n' and count_1 + count_2 + count_3 == 1:
                print('Вы проиграли')
                break
            if self.player._card[0].count('-') + self.player._card[1].count('-') + self.player._card[2].count('-') \
                    == 15:
                print('Игрок победил')
                break
            if self.computer._card[0].count('-') + self.computer._card[1].count('-') + \
                    self.computer._card[2].count('-') == 15:
                print('Компьютер победил')
                break
            print('Игрок_______________')
            for line in self.player._card:
                print(" ".join([str(item) for item in line]))
            print('Компьютер_______________')
            for line in self.computer._card:
                print(" ".join([str(item) for item in line]))


human = LotoCard('Ivan')
computer = LotoCard('R2D2')

game = LotoGame(human, computer)
game.start()
