# FrozenSet - Unoredered collection of unique element,used to freeze any collection,due to unordered collection indexing and slicing not supported,immutable in nature,represented through frozenset(collection),collection are string,list,tuple,set

# Example of frozen set
s="python"
fs=frozenset(s)
print(s)
print(type(fs))
print(id(fs))

# Python inbuilt function for frozenset are max,min,sum,length,id,type

# Frozenset Method

# union
fs1=frozenset([2,4,6,8])
fs2=frozenset([5,6,7,8,4])
print(fs1.union(fs2))

# intersection
fs1=frozenset([2,4,6,8])
fs2=frozenset([5,6,7,8,4])
print(fs1.intersection(fs2))

# symmetricdifference
fs1=frozenset([2,4,6,8])
fs2=frozenset([5,6,7,8,4])
print(fs1.symmetric_difference(fs2))

# difference
fs1=frozenset([2,4,6,8])
fs2=frozenset([5,6,7,8,4])
print(fs1.difference(fs2))

# isdisjoint
fs1=frozenset([2,4,6,8])
fs2=frozenset([5,6,7,8,4])
print(fs1.isdisjoint(fs2))

# issuperset
fs1=frozenset([2,4,6,8])
fs2=frozenset([5,6,7,8,4])
print(fs1.issuperset(fs2))

# issubset
fs1=frozenset([2,4,6,8])
fs2=frozenset([5,6,7,8,4])
print(fs1.issubset(fs2))

# Comment is used describe our code
# Variable Declaration
x=y=z=10
print(x,y,z)

x,y,z=10,20,30
print(x,y,z)