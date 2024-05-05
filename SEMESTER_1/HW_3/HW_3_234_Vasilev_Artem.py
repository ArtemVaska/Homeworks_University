"""
2. Добавить в игру разные типы оружия: холодное и метательное
3. Реализовать выстрел в направлении
4. Добавить использование предметов персонажами
"""


import math
from abc import ABC, abstractmethod


class Location:
    """
    Локация.
    """
    def __init__(self, name: str, width: int, height: int, length: int):
        """
        Инициализирует название локации, ширину, высоту и длину.
        """
        self.name = name
        self._width = width
        self._height = height
        self._length = length
        self._objs = []

    def addObject(self, obj):
        """
        Добавляет локацию в список локаций, если его еще там нет.
        """
        if obj not in self._objs:
            self._objs.append(obj)

    def clear(self):
        """
        Очищает список локаций.
        """
        self._objs = None

    def isInside(self, x, y, z) -> bool:
        return ((x > 0 and x < self._length)
                and (y > 0 and y < self._width)
                and (z > 0 and z < self._height))

    @property
    def width(self):
        """
        Геттер для получения ширины.
        """
        return self._width

    @property
    def length(self):
        """
        Геттер для получения длины.
        """
        return self._length

    @property
    def height(self):
        """
        Геттер для получения высоты.
        """
        return self._height

    @property
    def volume(self):
        """
        Геттер для расчета и получения объема.
        """
        return self.height * self.length * self.width


class GameObject:
    """
    Игровой объект.
    """
    def __init__(self, name: str, loc: Location, x, y, z):
        """
        Инициализирует название игрового объекта, локацию и ее координаты.
        """
        self.name = name
        self._loc = loc
        self._loc.addObject(self)
        self.x, self.y, self.z = x, y, z

    @property
    def x(self):
        """
        Геттер для получения координаты 'x'.
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Сеттер для задания координаты 'x'.
        """
        if x < 0:  # проверка, не равно ли значение новой координаты 0
            self._x = 0  # если да, то назначить новое значение координаты как 0
        elif self._loc.length < x:  # проверка, не больше ли оно значения соотв. координаты игрового поля
            self._x = self._loc.length  # если да, то назначить новое значение координаты = соотв. координате поля
        else:
            self._x = x  # при НЕсоблюдении условий изменение координаты 'x' на введенную пользователем

    @property
    def y(self):
        """
        Геттер для получения координаты 'y'.
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Сеттер для задания координаты 'y'.
        """
        if y < 0:
            self._y = 0
        elif self._loc.width < y:
            self._y = self._loc.width
        else:
            self._y = y

    @property
    def z(self):
        """
        Геттер для получения координаты 'z'.
        """
        return self._z

    @z.setter
    def z(self, z):
        """
        Сеттер для задания координаты 'z'.
        """
        if z < 0:
            self._z = 0
        elif self._loc.height < z:
            self._z = self._loc.height
        else:
            self._z = z

    def move(self, x, y, z):
        """
        Движение по игровому полю на расстояние, соотв. заданным координатам.
        """
        self.x += x
        self.y += y
        self.z += z

    def distance(self, obj):
        """
        Расчет дистанции от текущих координат объекта до заданного объекта. ???
        """
        dx = self.x - obj.x
        dy = self.y - obj.y
        dz = self.z - obj.z
        r2 = dx ** 2 + dy ** 2 + dz ** 2
        return int(math.sqrt(r2))

class LivingObject(GameObject):
    """
    Живой игровой объект.
    """
    def __init__(self, name: str, loc: Location, x, y, z, hp: int):
        """
        Инициализация живого объекта с заданным именем, локацией, координатами на игровом поле и кол-вом HP.
        """
        super().__init__(name, loc, x, y, z)  # ссылка (super) на базовый класс
        self._max_hp = hp
        self._hp = hp

    @property
    def maxHP(self):
        """
        Геттер для получения максимального HP.
        """
        return self._max_hp

    @property
    def hp(self):
        """
        Геттер для получения текущего HP.
        """
        return self._hp

    def changeHP(self, change):
        """
        Изменение текущего кол-ва HP на заданное значение (+ или -).
        """
        if not self.alive:
            return
        self._hp += change
        if self._hp < 0:
            self._hp = 0
        if self._hp > self._max_hp:
            self._hp = self._max_hp

    @property
    def alive(self) -> bool:
        """
        Возвращение информации о том, жив ли игровой объект.
        """
        return self._hp > 0

    def eat(self, obj):
        """
        Съесть заданный объект, если персонаж находятся на расстояние <= 1 от объекта.
        """
        if self.distance(obj) > 1:
            return
        self.changeHP(obj.eatMe())


class Weapon(GameObject):
    """
    Оружие
    """
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius):
        """
        Инициализация оружия с заданным именем, локацией, координатами на игровом поле, уроном и радиусом поражения.
        """
        super().__init__(name, loc, x, y, z)
        self._damage = damage
        self._radius = radius

    @property
    def damage(self):
        """
        Возвращает урон, наносимый для заданного оружия.
        """
        return self._damage

    @property
    def radius(self):
        """
        Возвращает радиус поражения для заданного оружия.
        """
        return self._radius

    def attack(self, obj: LivingObject):
        """
        Функция для атаки живого объекта.
        Наносит урон, соотв. используемому оружию при условии нахождения живого объекта в радиусе поражения оружия.
        """
        d = self.distance(obj)
        if d > self.radius:
            return
        obj.changeHP(-self.damage)


class SteelArms(Weapon):
    """
    Оружие ближнего боя.
    """
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius: int, material: str):
        """
        Инициализация холодного оружия с заданным именем, локацией,
        координатами на игровом поле, уроном, радиусом поражения и материалом,
        от которого зависит множитель нанесенного урона.
        """
        super().__init__(name, loc, x, y, z, damage, radius)
        self._material = material.lower()
        if self._material == 'wood':
            self._damage = damage * 0.8
        elif self._material == 'iron':
            self._damage = damage
        elif self._material == 'silver':
            self._damage = damage * 1.2

    def attack(self, obj: LivingObject):
        """
        Атака заданного живого объекта.
        """
        d = self.distance(obj)
        if d > self.radius:
            print('Атакуемый объект слишком далеко!')
            return
        obj.changeHP(-self.damage)
        print(f'Вы атаковали {obj.name} с помощью {self.name}!')
        print(f'У {obj.name} осталось {obj.hp} HP')


class ThrowingWeapon(Weapon):
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius):
        """
        Инициализация метательного оружия с заданным именем, локацией,
        координатами на игровом поле, уроном и радиусом поражения.
        """
        super().__init__(name, loc, x, y, z, damage, radius)

    def throw(self, obj: LivingObject):
        """
        Метнуть оружие в живой объект.
        """
        d = self.distance(obj)
        if d > self.radius:
            print('Не докинуть так далеко!')
            return
        obj.changeHP(-self.damage)
        print(f'Вы атаковали {obj.name} с помощью {self.name}!')
        print(f'У {obj.name} осталось {obj.hp} HP')
        print(f'{self.name} находится в координатах X={obj.x}, Y={obj.y}, Z={obj.z}')


class Player(LivingObject):
    def __init__(self, name: str, loc: Location, x, y, z, hp: int):
        """
        Инициализация игрока с заданным именем, местоположением и локацией на игровом поле, а также HP.
        """
        super().__init__(name, loc, x, y, z, hp)
        self.weapon = None  # пока что нет оружия

    def take_weapon(self, weapon: Weapon):
        """
        Взять оружие.
        """
        d = self.distance(weapon)
        if d > 1:
            self.move(weapon.x, weapon.y, weapon.z)
        self.weapon = weapon  # подобрали оружие
        print(f'Игрок {self.name} подобрал {self.weapon.name}')
        return

    def attack_player(self, obj: LivingObject):
        """
        Если у игрока есть оружие, то он может атаковать другого игрока.
        """
        if self.weapon is None:
            print(f'У игрока {self.name} нет оружия, чтобы атаковать!')
            return
        if isinstance(self.weapon, SteelArms):
            self.weapon.attack(obj)
            return
        if isinstance(self.weapon, ThrowingWeapon):
            self.weapon.throw(obj)
            return


class Eatable(ABC):
    """
    Съедобные объекты.
    """
    def __init__(self, hp: int):
        """
        Инициализация съедобного объекта и HP, которое он восстанавливает.
        """
        self._hp = hp
        self._eaten = False

    @property
    def eaten(self) -> bool:
        """
        Возвращает информацию о том, был ли съеден данный объект.
        """
        return self._eaten

    @abstractmethod
    def eatMe(self):
        """
        Если съедобный объект не был съеден, то ест его и изменяет HP.
        """
        if not self.eaten:
            self._eaten = True
            return self._hp
        else:
            return 0

class Food(GameObject, Eatable):
    """
    Еда = игровые съедобный объекты.
    """
    def __init__(self, name, loc, x, y, z, hp):
        """
        Инициализация объекта с заданным именем, локацией, координатами на игровом поле и HP,
        на которое будет увеличено кол-во HP объекта, съевшего его.
        """
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)

    def eatMe(self):
        """
        Функция, чтобы съесть еду (восполнение HP).
        """
        Food.eatMe(self)


class Poison(GameObject, Eatable):
    def __init__(self, name, loc, x, y, z, hp):
        """
        Инициализация ядовитого объекта с заданным именем, локацией, координатами на игровом поле и HP,
        на которое будет уменьшено кол-во HP объекта, выпившего / съевшего его.
        """
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)

    def eatMe(self):
        """
        Функция, чтобы съесть что-то съедобное (уменьшение HP).
        """
        return -Eatable.eatMe(self)


class Burnable(ABC):
    """
    Сжигаемые объекты.
    """
    def __init__(self):
        """
        Инициализация объекта, который пока что не сожжен
        """
        self._burned = False

    @property
    def burned(self):
        """
        Информация о том, сожжен ли объект.
        """
        return self._burned

    @abstractmethod
    def burnMe(self):
        """
        Сжигание объекта.
        """
        self._burned = True

class Cookable(GameObject, Eatable, Burnable):
    def __init__(self, name, loc, x, y, z, hp):
        """
        Инициализация объекта, который можно приготовить / съесть / сжечь,
        с заданным именем, локацией, координатами на игровом поле и HP,
        на которое будет увеличено / уменьшено кол-во HP объекта, съевшего его.
        """
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)
        Burnable.__init__(self)

    @classmethod
    def growMushroom(cls, loc, x, y, z):
        """
        Вырастить гриб в заданной локации и координатами, который восстанавлвиает 20 HP.
        """
        return cls('mushroom', loc, x, y, z, 20)

    def burnMe(self):
        """
        Приготовить гриб.
        """
        Burnable.burnMe(self)

    def eatMe(self):
        """
        Съесть гриб и увеличить HP, если он сожжен (приготовлен), иначе уменьшить.
        """
        hp = Eatable.eatMe(self)
        return hp if self.burned else -hp


mountains = Location('Mountains', 50, 200, 50)
sword = SteelArms('Excalibur', loc=mountains, x=25, y=195, z=25, damage=6666, radius=10, material='wood')
spear = ThrowingWeapon('Death', loc=mountains, x=20, y=180, z=20, damage=1000, radius=50)

good_man = Player('Kirito', loc=mountains, x=25, y=195, z=25, hp=2500)
bad_man = Player('Shinigami', loc=mountains, x=20, y=160, z=20, hp=10_000)

print(f'{good_man.name} {good_man.hp} HP  VS.  {bad_man.name} {bad_man.hp} HP\n')

good_man.take_weapon(sword)
print()
bad_man.take_weapon(spear)
print()

good_man.attack_player(bad_man)
print()
bad_man.attack_player(good_man)
print()
good_man.attack_player(bad_man)
