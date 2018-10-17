d = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
a = []
import operator
z = {}
z = sorted(d.items(), key = operator.itemgetter(1))
for i in range(len(z)):
        a.append (z[i][0])
print (a)


