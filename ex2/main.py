class IsLeapYear:
    def __init__(self):
        pass

    def is_leap_year_v1(self, year):
        if (year % 4) == 0:
            return True
        else:
            return False

    def is_leap_year_v2(self, year):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
