

class employee():
    def __init__(self, fname, lname, level, yrservice):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.yrservice = yrservice

    def __ge__(self, other):
        if (self.level== other.level):
            return self.yrservice >= other.yrservice
        return self.level >= other.level

    def __gt__(self, other):
        if (self.level== other.level):
            return self.yrservice > other.yrservice
        return self.level > other.level

    def __lt__(self, other):
        if (self.level== other.level):
            return self.yrservice < other.yrservice
        return self.level < other.level

    def __le__(self, other):
        if (self.level == other.level):
            return self.yrservice <= other.yrservice
        return self.level <= other.level

    def __eq__(self, other):
        pass



def main():

    dept = []
    dept.append(employee("tim", "sims", 5, 9))
    dept.append(employee("john", "doe", 4, 12))
    dept.append(employee("jane", "smith", 6, 6))
    dept.append(employee("rebecca", "robinson", 5, 13))
    dept.append(employee("tyler", "durden", 5, 12))
    print (dept[0] > dept[2])
    print (dept[4] < dept[3])
    emps = sorted(dept)
    for emp in emps:
        print (emp.lname)



if __name__ == "__main__":
    main()
