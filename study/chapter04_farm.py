def fact(x, y):
    short = y if y < x else x
    long = x if x > y else y
    if short == 0:
        return long / 2

    else:
        return fact(long - short, long % short)



print(fact(840, 320))
