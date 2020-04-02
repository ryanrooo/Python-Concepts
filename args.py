

def addition(*args):
    results = 0
    for arg in args:
        results += arg
    return results



def main():
    print (addition(5, 10, 15, 20))

    mynum = [ 5, 10, 15, 20]
    print(addition(*mynum))









if __name__ == "__main__":
    main()