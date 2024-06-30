#практична 1
class Human:
    weight = 70
    height = 170
    move = 'feet'
    education = ' '

    def see(self):
        print('I can see')

    def comunicate(self):
        print('I can talk to you')


class Builder(Human):
    education = 'construction'

    def build(self):
        print('I can build a house')

    def b_ability(self):
        print('stack bricks')


class Sailor(Human):
    education = 'maritime'

    def sail(self):
        print('I can steer a ship into the sea')

    def swim(self):
        print('I can swim ')


class Pilot(Human):
    education = 'transport'

    def aviate(self):
        print('I can aviate!')

    def oper(self):
        print('I can take the plane to a great height')


tom = Builder()
bob = Sailor()
tim = Pilot()


# практична 2
class Animal:
    def __init__(self, name, weigth_an, body_len_in_sm):
        self.name = name
        self.weigth_an = weigth_an
        self.body_len_in_sm = body_len_in_sm

    paws_amount = 4

    def jump(self):
        print('it can jump')


class Tiger(Animal):
    def roar(self):  #ричить
        print('the tiger roars')

    def __init__(self, name, weigth_an, body_len_in_sm):
        super(Animal, self).__init__(name, weigth_an, body_len_in_sm)

    def test(self):  #гетер
        return self.name, self.weigth_an, self.body_len_in_sm


class Croсodile(Animal):
    def swim(self):
        print('it can swim')

    def __init__(self, name, weigth_an, body_len_in_sm):
        super(Animal, self).__init__(name, weigth_an, body_len_in_sm)

    def test(self):
        return self.name, self.weigth_an, self.body_len_in_sm


class Kangaroo(Animal):
    def fight(self):
        print('the kangaroo fights hard')

    def __init__(self, name, weigth_an, body_len_in_sm):
        super(Animal, self).__init__(name, weigth_an, body_len_in_sm)

    def test(self):
        return self.name, self.weigth_an, self.body_len_in_sm


animal1 = Tiger('tiger', 70, 1000)
animal2 = Croсodile('crocodile', 100, 2000)
animal3 = Kangaroo('kangaroo', 80, 1800)



# ------------------ДОМАШНЯ РОБОТА-------------------------
# 1
class Device:
    def __init__(self, name, power, color, ability):
        self.name = name
        self.power = power
        self.color = color
        self.ability = ability

    def work_fixed_time(self):
        print('девайс працює по таймінгу')



class CoffeeMachine(Device):
    def __init__(self, name, power, color, ability):
        super().__init__(name, power, color, ability)

    def press_coffe(self):
        print('пресую кофе')

    def test(self):
        return self.name


class Blender(Device):
    def __init__(self, name, power, color, ability):
        super().__init__(name, power, color, ability)

    def blend(self):
        print('збиваю будь-які продукти')

    def test(self):
        return self.name

class MeatGrinder(Device):
    def __init__(self, name, power, color, ability):
        super().__init__(name, power, color, ability)

    def grind(self):
        print('перемелю будь-які прожилки та кістки')

    def test(self):
        return self.name

cof_mash = CoffeeMachine('X-name', 50, 'black', 'make coffee')
blen = Blender('bosh', 45, 'pink', 'blenderit')
gri = MeatGrinder('Bdumts' , 60, 'white', 'grind meat')


#завдання таке саме як і практичні в перше дз, вирішила його не писати

# 3
class Money:
    def __init__(self, tsila_chastyna, kopyika, valuta):
        self.tsila_chastyna = tsila_chastyna
        self.kopyika = kopyika
        self.valuta = valuta

    def output_groshi(self, tsila_chastyna, kopyika, valuta):
        print(self.tsila_chastyna, self.kopyika, self.valuta)


hrivna = Money(50, 25, 'гривня')
dollar = Money(10, 15, 'доларів')
euro = Money(230, 55, 'евро')


class Product(Money):
    def __init__(self, product_name, decre_amount, tsila_chastyna, kopyika, valuta):
        super().__init__(tsila_chastyna, kopyika, valuta)
        self.product_name = product_name
        self.decre_amount = decre_amount

    def __isub__(self, decre_amount):
        return self.tsila_chastyna - self.decre_amount

    def decrease_price(self):
        print(
            f'зменшуєм суму {self.product_name} на {self.decre_amount} одиниць: \n {self.tsila_chastyna -self.decre_amount}.{self.kopyika}  {self.valuta}')


prod1 = Product('apple', 5, 15, 10, 'гривень' )

print(prod1.decrease_price())


# --------------------ПЕРЕВАНТАЖЕННЯ ЧАСТИНА 5 ----------------------------
# казали що можна вибрати одну задачу з трьох
# 1
class Circle:
    def __init__(self, r, len):
        self.r = r
        self.len = len

    def __eq__(self, other):
        return self.r == other

    def __gt__(self, other):
        return self.len > other

    def __lt__(self, other):
        return self.len < other

    def __le__(self, other):
        return self.len <= other

    def __ge__(self, other):
        return self.len >= other

    def __add__(self, other):
        return self.r + other

    def __sub__(self, other):
        return self.r - other

    def __iadd__(self, other):
        self.r = self + other
        return self.r

    def __isub__(self, other):
        self.r = self - other
        return self.r


k1 = Circle(57, 25)
k2 = Circle(68, 33)

print(k1.__eq__(k2))
print(k1.__gt__(k2))
print(k1.__lt__(k2))
print(k1.__le__(k2))
print(k1.__ge__(k2))
n = 2   #змінюю пропорції кола шляхом роботи з цим числом
print(k1.__add__(n))
print(k1.__sub__(n))
print(k1.__iadd__(n))
print(k1.__isub__(n))
