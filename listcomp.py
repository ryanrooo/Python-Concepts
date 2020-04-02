


def main():

    even = [2 , 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odd = [1 ,3, 5, 7, 9, 11, 13, 15, 17, 19]

    #perfrom a mapping and filter function on a list

    evensquared = list(map(lambda e: e**2, filter(lambda e: e > 4 and e < 16, even)))
    print (evensquared)

    #simplified list comprehension
    evensquared =  [ e ** 2 for e in even]
    print (evensquared)

    #limit the items with predicate condition
    oddsquared = [e ** 2 for e in odd if e > 3 and e < 17]
    print (oddsquared)

if __name__ == "__main__":
    main()