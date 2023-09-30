from math import sqrt, trunc
class Vector:

    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, (int, float)):
            self.x = x
        else:
            raise TypeError("Невірний тип аргумента 'x'")
        if isinstance(y, (int, float)):
            self.y = y
        else:
            raise TypeError("Невірний тип аргумента 'y'")
        if isinstance(z, (int, float)):
            self.z = z
        else:
            raise TypeError("Невірний тип аргумента 'z'")

    def __str__(self):
        return f'Vector{self.x, self.y, self.z}'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Vector(new_x, new_y, new_z)

    def __iadd__(self, other):
        new_x = self.x + other
        new_y = self.y + other
        new_z = self.z + other
        return Vector(new_x, new_y, new_z)

    def __isub__(self, other):
        new_x = self.x - other
        new_y = self.y - other
        new_z = self.z - other
        return Vector(new_x, new_y, new_z)

    def __mul__(self, other):
        if isinstance(other, (Vector)):
            prod_d_c = (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
            return f'scalar product = {prod_d_c}'
        if isinstance(other, (int, float)):
            return Vector((self.x * other), (self.y * other), (self.z * other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __int__(self):
        return trunc(sqrt(abs(self.x ** 2) + abs(self.y ** 2) + abs(self.z ** 2)))

    def __len__(self):
        return self.__int__()

    def __neg__(self):
        self.x = - self.x
        self.y = - self.y
        self.z = - self.z
        return Vector(self.x, self.y, self.z)

    def __getitem__(self, index):
        self.koord = [self.x, self.y, self.z]
        return self.koord[index]

    def __setitem__(self, index, value):
        self.koord = [self.x, self.y, self.z]
        self.koord[index] = value
        return value

    def __contains__(self, item):
        self.koord = [self.x, self.y, self.z]
        if item in self.koord:
            return True
        return False

    def __bool__(self):
        if len(self) != 0:
            return True
        return False

    def __call__(self):
        print(f'{self} become functor')


a = Vector(1, 2, 3)
b = Vector(5, 6, 7)
print(f'a = {a}')
print(f'b = {b}')
print(a == b)
c = a + b
print(f'c = {c}')
d = b - a
print(f'd = {d}')
print()
d += 3
print(f'd = {d}')
c -= 5
print(f'c = {c}')
print(c * d)
print()
c = c * 5
print(f'c = {c}', type(c))
d = 5 * d
print(f'd = {d}', type(d))

print(f'len(c) = {len(c)}')
print()
print(f'c.__neg__ = {c.__neg__()}')
print(c[0])
print(c.__setitem__(1, 12))
print(-5 in c)
print(c.__bool__())
c()

