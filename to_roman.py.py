roman_numeral = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

def to_roman(num):
    if not (0 < n < 4000):
        raise OutOfRangeError
    if not isinstance(n, int):
        raise NotIntegerError

    def to_roman(n):
        result = ''
        # print('n: {0}'.format(n))
        for numeral, integer in roman_numeral:
            while n >= integer:
                result += numeral
                n -= integer
        return result