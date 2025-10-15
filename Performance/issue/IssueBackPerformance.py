
def IssueBackPoint(total,good,bad):
    total = int(total)
    good = int(good)
    bad = int(bad)
    point = 10*total + 0.5*good -8*bad
    return point
