class Person:

    def __init__(self, name , age):

        self.name = name
        self.age = age

    def __del__(self):
        print("Obj deleted")

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        print("Str called")
        return f"X: {self.x}, Y: {self.y}"

    def __repr__(self):
        print("Repr callees")
        return f"X: {self.x}, Y: {self.y}"

    def __call__(self):
        print("called")

    def __str__(self):
        print("Print called")
        return f"Value of X: {self.x} and value of Y: {self.y}"


v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1+v2
print(v3)
print(v3.x, v3.y)
print("Repr: ")
v3.__repr__()
print(v3)
v3()

ghq = str(v3)
print(ghq)