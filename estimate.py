from datetime import  datetime
import timedelta

def sum(start, end):
    a = datetime.strptime(start[0], '%Y-%m-%d %H:%M:%S.%f')
    b = datetime.strptime(end[0], '%Y-%m-%d %H:%M:%S.%f')
    c = b - a
    c = c.total_seconds()
    c /= 60
    if c < 5:
        return 0
    elif c > 5:
        c = (c - 5) / 30 * 20
        return c
