import random
from random import randint as rnd, randint
from random import shuffle
import os

'''
0.двумерный лабиринт
1.можно собирать предметы (append, extend)
2.выбрасывать предметы (remove, pop)
3.сортировать инвентарь (sort, reverse, lambda f)
4.поиск ключевых элементов (index, in, not in)
5.копировать и модифицировать списки(copy, slicing)
6.list compr.
'''


def walk(direction):
    if direction == 'w':
        if player.posy - 1 >= 0:
            player.posy -= 1
    elif direction == 's':
        if player.posy + 1 < maze.n:
            player.posy += 1
    elif direction == 'a':
        if player.posx - 1 >= 0:
            player.posx -= 1
    elif direction == 'd':
        if player.posx + 1 < maze.n:
            player.posx += 1


def action():
    actions = []
    if 'зелье регенерации' in player.inv: actions.append('выпить зелье регенерации')
    if 'световая бомба' in player.inv: actions.append('использовать световую бомбу')
    if len(player.inv): actions += ['сортировать инвентарь', 'выкинуть предмет']
    if actions:
        print('Что вы хотите сделать?')
        print(*[f'{i + 1}. {actions[i]}' for i in range(len(actions))], sep='\n')
    else:
        return
    choosen = actions[int(input()) - 1]
    if choosen == 'выпить зелье регенерации':
        print('+30 hp')
        if player.hp < 70:
            player.hp += 30
        else:
            player.hp = 100
        player.inv.remove('зелье регенерации')
    elif choosen == 'использовать световую бомбу':
        for y in range(max(0, player.posy - 1), min(maze.n, player.posy + 2)):
            for x in range(max(0, player.posx - 1), min(maze.n, player.posx + 2)):
                maze.opened[x][y] = ''
        player.inv.remove('световая бомба')
    elif choosen == 'сортировать инвентарь':
        player.inv.sort()
    elif choosen == 'выкинуть предмет':
        garbind = int(input('введите номер предмета в инвентаре(1, 2, ...): '))
        if 0 <= (garbind - 1) < len(player.inv):
            player.inv.pop(garbind - 1)
        else:
            print('такого предмета нет')


def event(location):
    global win
    if location == 'c':
        loot = random.choice(
            ['доспехи', 'меч', 'зелье регенерации', 'световая бомба', 'зелье регенерации', 'световая бомба'])
        print(f'Вы наткнулись на сундук! Внутри вы увидели {loot}', 'хотите положить вещь в инвентарь?(y/n)', sep='\n')
        if str(input()) in ['Да', 'да', 'y', 'Yes', 'yes', 'da']:
            player.inv.append(loot)
            maze.grid[x][y] = '_'
    elif location == 't':
        player.take_dmg(5)
        print('Вы попали в ловушку!')
    elif location == 'm':
        player.take_dmg(30)
        print('На вас напал монстр!')
        if 'меч' in player.inv: maze.grid[x][y] = '_'
    elif location == 'K':
        print('На полу лежит ключ, хотите подобрать его?(y/n)')
        if str(input()) in ['Да', 'да', 'y', 'Yes', 'yes']:
            player.inv.append('ключ')
            maze.grid[x][y] = '_'
    elif location == 'P':
        if portal_wasnt_found:
            print('Вы нашли запертую дверь, за которой слышны звуки портала.')

        if 'ключ' in player.inv:
            print('Что вы хотите сделать?', '1. Телепортироваться в случайную точку', '2. Выйти из лабиринта', sep='\n')
            if str(input()) == '1':
                player.posx, player.posy = randint(0, maze.n - 1), randint(0, maze.n - 1)
                os.system('cls')
                maze.explore(player.posx, player.posy)
                maze.mprint(player.posx, player.posy)
                if location != '_':
                    event(location)
            else:
                win = True
        else:
            print('Не получается открыть дверь к порталу.')


class Player:
    def __init__(self):
        self.hp = 100
        self.df = 0
        self.inv = []

        self.posx = 0
        self.posy = 0

    def setdf(self, armour):
        self.df = 0
        if 'шлем' in self.inv:
            self.df += 10
        elif 'нагрудник' in self.inv:
            self.df += 40

    def take_dmg(self, hurt):
        self.hp = int(self.hp - hurt * ((100 - self.df) / 100))


class Maze:
    def __init__(self, n):
        self.n = n
        self.grid = [['_' for x in range(n)] for y in range(n)]
        self.opened = [['*' for x in range(n)] for y in range(n)]
        self.opened[0][0] = ''

    # сгенерировать карту лабиринта
    def maze_gen(self):
        n = self.n
        places = ['t'] * (n - 1) + ['c'] * n + ['m'] * (n - 2) + ['P'] + ['K']  # traps, chests, monsters
        places = [''] * (n * n - len(places) - 1) + places
        shuffle(places)
        places = [''] + places
        self.grid = [[places[x + n * y] if places[x + n * y] != '' else '_' for x in range(n)] for y in range(n)]

    # распечатать карту лабиринта
    def mprint(self, playerposx, playerposy):
        for y in range(self.n):
            for x in range(self.n):
                if x == playerposx and y == playerposy:
                    print(self.grid[playerposx][playerposy] + '@', end=' ')
                else:
                    print('*', end=' ') if self.opened[x][y] == '*' else print(self.grid[x][y], end=' ')
            print()

    def explore(self, x, y):
        self.opened[x][y] = ''


player = Player()
# флаги
portal_wasnt_found = True
win = False
os.system('cls')
# правила
print('Добро пожаловать в лабиринт!')
print('Чтобы перемещаться используйте введите w/a/s/d, чтобы действовать введите любую букву.')
print('Эффекты предметов:\nМеч убивает монстров, броня даёт защиту.')
print('Вы выглядите так: @')

maze = Maze(int(input('Введите желаемый размер лабиринта(1 число): ')))
os.system('cls')
maze.maze_gen()
maze.mprint(0, 0)
print('-' * 50)
print(f'инвентарь: {player.inv}\nhp: {player.hp}\narmour: {player.df}')
print('-' * 50)
# игра
while True:
    userinp = str(input('ввод: '))
    if userinp in 'wasd':
        walk(userinp)
    else:
        action()
    os.system('cls')

    # обновление видимости карты лабиринта и позиции пользователя
    x, y = player.posx, player.posy
    location = maze.grid[x][y]
    maze.explore(x, y)
    maze.mprint(x, y)

    # воспроизводство события, если текущая клетка не пустая
    if location != '_':
        event(location)
        if win: break

    # проверки здоровья игрока
    if player.hp <= 0:
        break

    # вывод информации о персонаже
    print('-' * 50)
    print(f'инвентарь: {player.inv}\nhp: {player.hp}\narmour: {player.df}')
    print('-' * 50)

os.system('cls')

print('---ИГРА ОКОНЧЕНА---')
print('Победа!') if win else print('Вы проиграли.')
