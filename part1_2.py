class Rational:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        while den != 0:  # Euclidean algorithm
            temp = den
            den = num % den
            num = temp
        self.__num /= num
        self.__den /= num

    def trad(self):  # traditional form printout
        print(str(int(self.__num)) + '/' + str(int(self.__den)))

    def floating(self):  # floating-point form printout
        print(float(self.__num)/self.__den)


a = Rational(49, 70)
a.trad()
a.floating()
