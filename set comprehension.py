
def main():

    ctemp = [5, 10, 12 ,14, 10, 23, 41, 30, 12, 24, 12, 18, 29 ]

    # create unique set curly braces
    ftemp1 = [(t*9/5)+32 for t in ctemp]
    ftemp2 = {(t*9/5)+32 for t in ctemp}
    print (ftemp1)
    print (ftemp2)

    #build a set form an input source
    stemp = "The quick brown fox jumped over the lazy dog"
    char = {c.upper() for c in stemp if not c.isspace()}
    print (char)




if __name__ == "__main__":
    main()