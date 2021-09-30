class Rectangle:
    def __init__(self, length=1, width=1):  # 1 is the default for any unset field
        if 0 < length < 20:
            self.__length = length
        else:
            self.__length = 1
        if 0 < width < 20:
            self.__width = width
        else:
            self.__width = 1

    def __str__(self):  # redefined str() for convenience
        return 'length = ' + str(self.__length) + '\n' + 'width = ' + str(self.__width)

    @property  # length getter
    def length(self):
        return self.__length

    @length.setter  # length setter
    def length(self, length1):
        if 0 < length1 < 20:
            self.__length = length1

    @property   # width getter
    def width(self):
        return self.__width

    @width.setter  # width setter
    def width(self, width1):
        if 0 < width1 < 20:
            self.__width = width1

    def area(self):  # area calculate
        return self.__width * self.__length

    def perimeter(self):  # area calculate
        return (self.__width + self.__length) * 2


a = Rectangle()
b = Rectangle(10, 5)
print('A:\n' + str(a))
print('B:\n' + str(b))
print('A perim: ' + str(a.perimeter()))
print('B perim: ' + str(b.perimeter()))
print('A area: ' + str(a.area()))
print('B area: ' + str(b.area()))
