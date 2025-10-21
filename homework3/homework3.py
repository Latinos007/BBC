from random import randint as rnd
from random import shuffle

'''
0.двумерный лабиринт
1.можно собирать предметы (append, extend)
2.выбрасывать предметы (remove, pop)
3.сортировать инвентарь (sort, reverse, lambda f)
4.поиск ключевых элементов (index, in, not in)
5.копировать и модифицировать списки(copy, slicing)
6.list compr.
'''
rooms = ['*', 'chest', 'monster', 'key', 'portal', 'trap']
specs = {'hp': 100,
         'defence': 0}
inventory = []


class Player:
    def __init__(self):
        self.hp = 100
        self.df = 0
        self.inv = []



class Maze:
    def __init__(self, n):
        self.n = n
        self.grid = [[x for x in range(n)] for y in range(n)]
        self.opened = [['*' for x in range(n)] for y in range(n)]
        self.plpos = [0,0]

    def maze_gen(self):
        n = self.n
        places = ['t'] * rnd(2, n * n // 4) + ['c'] * rnd(2, n * n // 5) + ['m'] * rnd(1,n * n // 8) + ['K'] + ['P'] # traps, chests, monsters
        places = [''] * (n * n - len(places)-1) + places
        shuffle(places)
        places = [''] + places
        self.grid = [[places[x + n*y] if places[x + n*y]!='' else '_' for x in range(n)] for y in range(n)]

    def mprint(self):
        for x in range(self.n):
            for y in range(self.n):
                print('*', end=' ') if self.opened[x][y] == '*' else print(self.grid[x][y], end=' ')
            print()


MAZE = Maze(7)
player = Player()
MAZE.maze_gen()


MAZE.opened[0][0] = ''
MAZE.mprint()
while True:
    walk = str(input())
    if walk == 'r':
        pass