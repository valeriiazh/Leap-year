def my_leap_year(y):

    if (y % 400 == 0) or (y % 4 == 0 and not y % 100 == 0):
        print("{0} is a leap year".format(y))
    else:
        print("{0} is not a leap year".format(y))


year = int(input("Enter a year: "))
my_leap_year(year)
