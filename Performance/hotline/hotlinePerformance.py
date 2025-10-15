def HotlinePoint(total,good,bad):
    total = int(total)
    good = int(good)
    bad = int(bad)
    point = 2.5*total + 0.5*good -bad
    return point
