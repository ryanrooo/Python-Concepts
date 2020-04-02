class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0}, y:{1}>".format(self.x, self.y)

    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return  point(self.x - other.x, self.y - other.y)

    def __iadd_(self, other):
        self.x += other.x
        self.y += other.y
        return self







def main():


    p1 = point(10,20)
    p2 = point(30,30)
    print(p1, p2)

    #add two points
    p3 = p1 + p2
    print (p3)

    #sub two points
    p4 = p1 - p2
    print (p4)

    #add in place
    p1 += p2
    print (p1)


if __name__ == "__main__":
    main()
