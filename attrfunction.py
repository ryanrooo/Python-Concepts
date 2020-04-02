

class color():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}"
        else:
            raise AttributeError

    def __setattr__(self, attr, value):
        if attr == "rgbcolor":
            self.red = value[0]
            self.green = value[1]
            self.blue = value[2]
        super().__setattr__(attr,value)

    # use dir to list the available properties
    def __dir__(self):
        return ("red", "green", "blue", "rgbcolor")


def main():

    #create instance of color
    cls1 = color()

    #print the value of the coputed attributes
    print(cls1.rgbcolor)
    print (cls1.hexcolor)

    #set the value of a computed attribute
    cls1.rgbcolor = (1,2,3)
    print (cls1.rgbcolor)

    #acces regular values
    print (cls1.red)

    #use dir to list the available properties
    print (dir(cls1))


if __name__ == "__main__":
    main()


