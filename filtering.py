

#Return Odd numbers

def filterfun(x):
    if x % 2 == 0:
        return False
    return True

def filterfun2(x):
    if x.isupper():
        return False
    return True

def squarefun(x):
    return x ** 2

def tograde(x):
    if x >= 90:
        return "A"
    elif x >= 80 and x <= 90:
        return  "B"
    elif x >= 70 and x <= 80:
        return  "C"
    elif x >= 65 and x <= 70:
        return  "D"
    else:
        return "F"

def main():

    #data
    number = [1, 8, 4, 5, 13, 26, 381, 410, 58, 47 ]
    char = "AbCdEfGHijK"
    grades = [81,89,94,78,61,66,99,74]

    # Use Filter to remove even number from list
    odd = list(filter(filterfun, number))
    print (odd)

    # Filter on non numerical to produce lowercase values only
    lowers = list(filter(filterfun2, char))
    print (lowers)

    # Map to create a new sequence of values
    square = list(map(squarefun,number))
    print (square)

    # Use sorted and map to change numbers to grades

    grades = sorted(grades)
    letters = list(map(tograde, grades))
    print (grades)
    print (letters)



if __name__ == "__main__":
    main()