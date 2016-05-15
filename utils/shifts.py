import datetime as dt


today = dt.datetime.today()

t0 = dt.datetime(year=today.year, month=today.month, day=today.day, hour=1, minute=0)
t1 = dt.datetime(year=today.year, month=today.month, day=today.day, hour=8, minute=0)
t2 = dt.datetime(year=today.year, month=today.month, day=today.day, hour=17, minute=0)

shift_1 = (t0, t1)
shift_2 = (t1, t2)
shift_3 = (t2, t0)
