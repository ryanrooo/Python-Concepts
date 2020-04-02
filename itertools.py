import itertools

def testfun(x):
    pass

#iterates next name and repeats cycle
def main():
    seq1 = ["joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print (next(cycle1))
    print (next(cycle1))
    print (next(cycle1))
    print (next(cycle1))
    print (next(cycle1))
    print (next(cycle1))

    #iterates next number by 10 increments
    count1 = itertools.count(100, 10)
    print (next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # accumulates previous added number with next number
    vals = [10, 20, 30, 40, 90, 50, 60, 70, 80 ]
    accumulator = itertools.accumulate(vals, max)
    print (list(accumulator))

    chain = itertools.chain("ABCD", "1234")
    print (list(chain))

    print (itertools.__doc__)


if __name__ == "__main__":
    main()