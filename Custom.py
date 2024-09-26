class Rectangle:

    def __init__(self,length,width):
        self.length=length
        self.width=width


    def __iter__(self):
        # will return an iterator pointing to a tuple
        return iter((self.length,self.width))


    def getDimensions(self):

        print("length:",self.length)
        print("width:",self.width)



instance=Rectangle(2, 3)
instance2=Rectangle(20,40)
instance2.getDimensions()

## for iteration over an instance of the rectangle class

for dimenisons in instance2:
    print(dimenisons,end=" ")

