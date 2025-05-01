# union
s1={1,2,3,4,5}
s2={5,6,7,8,4}
print(s1.union(s2))

# intersection
s1={1,2,3,4,5}
s2={5,6,7,8,4}
print(s1.intersection(s2))

# difference
s1={1,2,3,4,5}
s2={5,6,7,8,4}
print(s1.difference(s2))

# symmetric difference
s1={1,2,3,4,5}
s2={5,6,7,8,4}
print(s1.symmetric_difference(s2))


# intersectionupdate
s1={1,2,3,4,5}
s2={5,6,7,8,4}
s1.intersection_update(s2)
print(s1)
print(s2)

# symmetric difference update
s1={1,2,3,4,5}
s2={5,6,7,8,4}
s1.symmetric_difference_update(s2)
print(s1)
print(s2)

# isdisjoint - s1 and s2 element are different
s1={1,2,3,4,5}
s2={5,6,7,8,4}
print(s1.isdisjoint(s2))

# subset - s1 and s2 element are same
s1={1,2,3,4,5}
s2={5,6,4,8}
print(s1.issubset(s2))

# superset - s1 and s2 element are same
s1={1,2,3,4,5}
s2={5,6,7,8,4}
print(s1.issuperset(s2))


s3={1,2,3,4}
s4={1,2,3,4}
print(s3.issuperset(s4))
print(s3.issuperset(s4))