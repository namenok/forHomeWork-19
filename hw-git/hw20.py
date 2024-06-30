#практична
#1
class Wheels:
    def __init__(self, size, diameter, season):
        self.size = size
        self.diameter = diameter
        self.season = season

    def season_speed(self):
        if self.season == 'winter':
            return f'швидкість - 5'
        elif self.season == 'summer':
            return f'максимальна швидкість'
        else:
            return None

class Motor:
    def __init__(self, fuel_type, capacity):
        self.fuel_type = fuel_type
        self.capacity =capacity

    def energy_conversion(self):
        return f'перетворення енергії пального в механічну роботу.'

class Doors:
    def __init__(self, color, amount, opening_type):
        self.color = color
        self.amount = amount
        self.opening_type = opening_type

    def opening(self):
        if self.opening_type == 'up':
            return f'двері відчиняються вгору'
        elif self.opening_type == 'sideways':
            return f'двері відчиняються вбік'

class Auto(Wheels, Motor, Doors):
    pass

# 2
class HomePet:
    def __init__(self, name, type, size, color):
        self.name = name
        self.type = type
        self.size = size
        self.color = color




class Dog(HomePet):
    def sounds(self):
        return f'гавкає'

    def __init__(self, name, type, size, color):
        super().__init__(name, type, size, color)

    def show_n(self):
        return self.name

    def show_t(self):
        return self.type

class Kat(HomePet):
    def sounds(self):
        return f'мяукає'

    def __init__(self, name, type, size, color):
        super().__init__(name, type, size, color)

    def show_n(self):
        return self.name

    def show_t(self):
        return self.type

class Papagei(HomePet):
    def sounds(self):
        return f'цвірінькає'

    def __init__(self, name, type, size, color):
        super().__init__(name, type, size, color)

    def show_n(self):
        return self.name

    def show_t(self):
        return self.type

class Hamster(HomePet):
    def sounds(self):
        return f'пікає'

    def __init__(self, name, type, size, color):
        super().__init__(name, type, size, color)

    def show_n(self):
        return self.name

    def show_t(self):
        return self.type


# -----------------------HOME WORK------------------
#1

class Figure:
   def __init__(self, side_len, width, pi, radius, kated, len_basis_trap_1,len_basis_trap_2, heigh_basis_trap):
       self.side_len = side_len
       self.width = width
       self.pi = pi
       self.radius = radius
       self.kated = kated
       self.len_basis_trap_1 = len_basis_trap_1
       self.len_basis_trap_2 = len_basis_trap_2
       self.heigh_basis_trap =heigh_basis_trap




class Pramokutnik(Figure):
    def __init__(self, side_len, width):
        super().__init__(side_len, width)

    def pl(self):
        return self.side_len**2 * self.width**2


class Circle(Figure):
    def __init__(self, pi, radius):
        super().__init__(pi, radius)

    def pl(self):
        return self.pi * self.radius**2


class Pramokutnytrukutnik(Figure):
    def __init__(self, kated):
        super().__init__(kated)


    def pl(self):
        return (self.kated**2)/2


class Trapezia(Figure):
    def __init__(self, len_basis_trap_1,len_basis_trap_2,  heigh__basis_trap):
        super().__init__(len_basis_trap_1,len_basis_trap_2,  heigh__basis_trap)

    def pl(self):
        return (self.len_basis_trap_1 + self.len_basis_trap_2)* self.heigh__basis_trap**2



# 2 видозмінюю додаючи магічні методи
class Figure:
   def __init__(self, side_len, width, pi, radius, kated, len_basis_trap_1,len_basis_trap_2, heigh_basis_trap):
       self.side_len = side_len
       self.width = width
       self.pi = pi
       self.radius = radius
       self.kated = kated
       self.len_basis_trap_1 = len_basis_trap_1
       self.len_basis_trap_2 = len_basis_trap_2
       self.heigh_basis_trap = heigh_basis_trap




class Pramokutnik(Figure):
    def __init__(self, side_len, width):
        super().__init__(side_len, width)

    def __int__(self):
        return self.side_len**2 * self.width**2

    def __str__(self):
        return f'довжина сторони прямокутника = {self.side_len}, ширина =  {self.width}'


class Circle(Figure):
    def __init__(self, pi, radius):
        super().__init__(pi, radius)

    def __int__(self):
        return self.pi * self.radius**2

    def __str__(self):
        return f'число пі ={self.pi}, радіус кола = {self.radius}'


class Pramokutnytrukutnik(Figure):
    def __init__(self, kated):
        super().__init__(kated)

    def __int__(self):
        return (self.kated**2)/2

    def __str__(self):
        return f'катед прямокутного трикутника = {self.kated}'


class Trapezia(Figure):
    def __init__(self, len_basis_trap_1,len_basis_trap_2,  heigh_basis_trap):
        super().__init__(len_basis_trap_1,len_basis_trap_2,  heigh_basis_trap)

    def __int__(self):
        return (self.len_basis_trap_1 + self.len_basis_trap_2)* self.heigh_basis_trap**2

    def __str__(self):
        return f'довжимна основи трапеціі перша = {self.len_basis_trap_1},друга =  {self.len_basis_trap_2}, висота =  {self.heigh_basis_trap}'


# 3
class Shape:
    def __init__(self, len_of_side, upper_left_corner, len_of_rectangle, width_of_rectangle, coordinate_of_circle,
                 rad_circle, parallel_side_to_the_coordinate_axis, lis):
        self.len_of_side = len_of_side
        self.upper_left_corner = upper_left_corner
        self.len_of_rectangle = len_of_rectangle
        self.width_of_rectangle = width_of_rectangle
        self.coordinate_of_circle = coordinate_of_circle
        self.rad_circle = rad_circle
        self.parallel_side_to_the_coordinate_axis = parallel_side_to_the_coordinate_axis
        self.lis = lis

    def show(self):
        #вивести на екран інфу про фігуру, але я зробила це окремо в кожному дочірньому, не знаю як це відобразити тут
        pass

    def save(self, lis):
        with open('le20.txt', 'w') as file:
            file.write(str(lis))

    def load(self):
        with open('le20.txt', 'r') as file:
            print(file.read())


class Square(Shape):
    def __init__(self, len_of_side, upper_left_corner):
        super().__init__(len_of_side, upper_left_corner)

    def __str__(self):
        return f' інфа квадрат: {self.len_of_side}, {self.upper_left_corner}'


class Rectangle(Shape):
    def __init__(self, upper_left_corner, len_of_rectangle, width_of_rectangle):
        super().__init__(upper_left_corner, len_of_rectangle, width_of_rectangle)

    def __str__(self):
        return f' інфа прямокутник: {self.upper_left_corner}, {self.len_of_rectangle}, {self.width_of_rectangle}'


class Circle(Shape):
    def __init__(self, coordinate_of_circle, rad_circle):
        super().__init__(coordinate_of_circle, rad_circle)

    def __str__(self):
        return f' інфа коло: {self.coordinate_of_circle}, {self.rad_circle}'


class Ellipse(Rectangle):
    def __init__(self, parallel_side_to_the_coordinate_axis, upper_left_corner, len_of_rectangle, width_of_rectangle):
        Square.__init__(parallel_side_to_the_coordinate_axis)
        Rectangle.__init__(upper_left_corner, len_of_rectangle, width_of_rectangle)

    def __str__(self):
        return (f' інфа еліпса: {self.parallel_side_to_the_coordinate_axis},прямокутника з ним : '
                f'{self.upper_left_corner}, {self.len_of_rectangle}, {self.width_of_rectangle}')


sq = Square(5, 90)
rec = Rectangle(90, 7, 4)
ci = Circle(1, 10)
ell = Ellipse(12, 90, 7, 4)

li = [sq, rec, ci, ell]
Shape.save()
Shape.load()