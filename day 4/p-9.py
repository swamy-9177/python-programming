a={1,2,3,4}
b={2,3,5,6}
print(a.union(b))
print(a|b)
print(a.intersection(b))
print(a&b)
a.intersection_update(b)
print(a)
print(a.difference(b))
print(a-b)

print(a^b)
print(a.symmetric_difference(b))
print(a.isdisjoint(b))
print(a.issubset(b))
print(a.superset(b))