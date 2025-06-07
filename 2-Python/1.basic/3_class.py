

class foo:
    a, b, c, d = 0, "ace", [1, 2, 3], (1, 2, 3)


newObj = foo()
print(newObj.a)
print(newObj.b)
print(newObj.c[2])
print(newObj.d)


class Point:
    pass  # when you don't want to write any code yet


class Human:
    def __init__(self, s, i):
        self.name = s
        self.age = i

    def getAge(self, i):
        self.age += i


a = Human("shin", 10)
print(a.name)
print(a.age)
a.getAge(50)
print(a.age)


# use self in parameter
newH = Human("Marie", 10)
Human.getAge(newH, 5)
print(newH.age)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, x, y):
        self.x += x
        self.y += y

    def halfway(self, target):
        tempX = (self.x + target.x) / 2
        tempY = (self.y + target.y) / 2
        return Point(tempX, tempY)

    def midpoint(p1, p2):
        return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)


p = Point(3, 4)
q = Point(5, 12)
r = p.halfway(q)
print(r.x, r.y)


r = Point.midpoint(p, q)
print(r.x, r.y)


#next chapter: 
# https://www.youtube.com/watch?v=fIEVYNvoahk&list=PLQS78DCab0Ipbh3THERLgoqsmx_XWg_66&index=15