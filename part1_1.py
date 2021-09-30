class Rectangle:
    def __init__(self, length=1, width=1):
        if 0 < length < 20:
            self.__length = length
        else:
            self.__length = 1
        if 0 < width < 20:
            self.__width = width
        else:
            self.__width = 1

    def __str__(self):
        return 'length = ' + str(self.__length) + '\n' + 'width = ' + str(self.__width)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length1):
        if 0 < length1 < 20:
            self.__length = length1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width1):
        if 0 < width1 < 20:
            self.__width = width1

    def area(self):
        return self.__width * self.__length

    def perimeter(self):
        return (self.__width + self.__length) * 2

a = Rectangle()
b = Rectangle(10, 5)
print('A:\n' + str(a))
print('B:\n' + str(b))
print('A perim: ' + str(a.perimeter()))
print('B perim: ' + str(b.perimeter()))
print('A area: ' + str(a.area()))
print('B area: ' + str(b.area()))
