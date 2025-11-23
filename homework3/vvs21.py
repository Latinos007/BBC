class strGame:
    def __init__(self, s):
        self.s = str(s)

    def lvl1(self, metod):
        if metod == 'lower':
            print(self.s.lower())
        elif metod == 'upper':
            print(self.s.upper())
        else:
            print(self.s.capitalize())

    def lvl2(self, i1, i2, i3):
        if i1: print('первое вхождение слова круто:', self.s.find('круто'))
        if i2: print(self.s.replace('круто', 'cool', 1))  # з
        if i3: print('кол-во букв "о": ', self.s.lower().count('о'))

    def lvl3(self, spltsign, joinsgn):
        print(joinsgn.join(self.s.split(spltsign)))

    def lvl4(self, metod, clersign=''):
        if clersign != '':
            self.s = self.s.strip(clersign)
            print(self.s)
        if metod == 'isdigit' and self.s.isdigit(): print('эта строка является числом')
        if metod == 'isalpha' and self.s.isalpha(): print('эта строка является словом')
    def lvl5(self):
        garb = '_№!@#$;%^:&?*_-+=`~[]{}<>().'
        s = self.s
        new_s = ''
        for i in range(len(s)):
            if s[i] not in garb:
                new_s += s[i]
            else: new_s += ' '
        print(new_s.strip().capitalize()+'.')

level, user_str = int(input('введите желаемый уровень: ')), str(input('введите строку: '))
game = strGame(user_str)

if level == 1:
    metod = str(input('введите необходимый метод(upper, lower, capitalize): '))
    game.lvl1(metod)
elif level == 2:
    print(
        'введите, какие из функций "первое вхождение, замена слова круто, подсчёт"о"" вы хотите использовать(например "1 1 0")')
    i1, i2, i3 = [bool(x) for x in str(input()).split()]
    game.lvl2(i1, i2, i3)
elif level == 3:
    spltsign, joinsgn = str(input('символ для split: ')), str(input('символ для join: '))
    game.lvl3(spltsign, joinsgn)
elif level == 4:
    metod = str(input('выберите метод: '))
    clearsign = ''
    if metod == 'strip':
        clearsign = str(input('ввведите знак, который хотите убрать по краям: '))
    game.lvl4(metod, clearsign)
elif level == 5:
    game.lvl5()