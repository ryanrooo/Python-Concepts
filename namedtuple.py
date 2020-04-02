import collections

def main():

    point = collections.namedtuple("point", "x y")
    p1 = point(10,20)
    p2 = point(30, 40)
    print (p1, p2)

    p1 = p1._replace(x=100)
    print (p1)

if __name__ == "__main__":
    main()