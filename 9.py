import datetime
from humans.classes_lesson import Human as h, Squadron as s, Regimen as r
# t_current = datetime.datetime.now()
# diff = t_current - datetime.timedelta(hours=1)
# print(diff.time())

h1 = h('John')
h2 = h('Donn')
s1 = s()
r1 = r()
h1.set_db(1995, 5, 5)
h1.set_age()
h2.set_age()
s1.add([h1, h2])
r1.add([s1])
r1.info()
















