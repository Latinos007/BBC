import random
from random import randint as rnd
from random import shuffle
import os
random.seed(42)

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
    print('Что вы хотите сделать?')
    actions = []
    if 'зелье регенерации' in player.inv: actions.append('выпить зелье регенерации')
    if 'световая бомба' in player.inv: actions.append('использовать световую бомбу')
    if len(player.inv): actions += ['сортировать инвентарь', 'выкинуть предмет']
    print(*[f'{x+1}. {actions[x]}' for x in range(len(actions))], sep = '\n')


def event(location):
    global win
    if location == 'c':
        loot = random.choice(['шлем', 'доспехи', 'меч','зелье регенерации', 'световая бомба'])
        print(f'Вы наткнулись на сундук! Внутри вы увидели {loot}', 'хотите положить вещь в инвентарь?', sep='\n')
        if str(input()) in ['Да', 'да', 'y', 'Yes', 'yes']:
            player.inv.append(loot)
            maze.grid[x][y] = '_'
    elif location == 't':
        print('Вы попали в ловушку!', '-5 hp', sep='\n')
        player.hp -= 5
    elif location == 'm':
        player.hp -= 30
        print('На вас напал монстр!', '-30 hp', sep='\n')
        maze.grid[x][y] = '_'
    elif location == 'K':
        print('На полу лежит ключ, хотите подобрать его?')
        if str(input()) in ['Да', 'да', 'y', 'Yes', 'yes']:
            player.inv.append('ключ')
            maze.grid[x][y] = '_'
    elif location == 'P':
        if portal_wasnt_found:
            print('Вы нашли запертую дверь, за которой слышны звуки портала.', end=' ')
        if 'ключ' in player.inv:
            print('Ключ в вашем инвентаре подощёл, вы заходите в портал')
            win = True
        else:
            print('Не получается открыть дверь к порталу.')


class Player:
    def __init__(self):
        self.hp = 100
        self.df = 0
        self.dmg = 10
        self.inv = []

        self.posx = 0
        self.posy = 0


class Maze:
    def __init__(self, n):
        self.n = n
        self.grid = [['_' for x in range(n)] for y in range(n)]
        self.opened = [['*' for x in range(n)] for y in range(n)]
        self.opened[0][0] = ''

    #сгенерировать карту лабиринта
    def maze_gen(self):
        n = self.n
        places = ['t'] * rnd(2, n * n // 4) + ['c'] * rnd(2, n * n // 5) + ['m'] * rnd(1, n * n // 8) + ['K'] + [
            'P']  # traps, chests, monsters
        places = [''] * (n * n - len(places) - 1) + places
        shuffle(places)
        places = [''] + places
        self.grid = [[places[x + n * y] if places[x + n * y] != '' else '_' for x in range(n)] for y in range(n)]

    #распечатать карту лабиринта
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

maze = Maze(4)
player = Player()

# флаги
portal_wasnt_found = True
win = False

maze.maze_gen()
maze.mprint(0, 0)

# правила
os.system('cls')
print('Добро пожаловать в лабиринт!')
print('чтобы перемешаться используйте wasd')

# игра
while True:
    userinp = str(input('направление: '))
    if userinp in 'wasd': walk(userinp)
    else: action()
    os.system('cls')

    #обновление видимости карты лабиринта и позиции пользователя
    x, y = player.posx, player.posy
    location = maze.grid[x][y]
    maze.explore(x, y)
    maze.mprint(x, y)

    #воспроизводство события, если текущая клетка не пустая
    if location != '_':
        event(location)
        if win: break

    #проверки здоровья игрока
    if player.hp <= 0:
        break

    #вывод информации о персонаже
    print('-' * 50)
    print(f'инвентарь: {player.inv}\nhp: {player.hp}')
    print('-' * 50)

os.system('cls')

print('---ИГРА ОКОНЧЕНА---')
print('Победа!') if win else print('Вы проиграли.')
# доделать систему защиты, систему боя, систему хп, выбор действий в портале
