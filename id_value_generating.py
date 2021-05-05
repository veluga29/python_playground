import sys

a = 1000
b = 1000
print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(id(a))
print(id(b))

c = (2, 3, 5)
d = (2, 3, 5)
print(sys.getrefcount(c))
print(sys.getrefcount(d))
print(id(c))
print(id(d))

e = 'Go, go, corgi'
f = 'Go, go, corgi'
print(sys.getrefcount(e))
print(sys.getrefcount(f))
print(id(e))
print(id(f))


print()

x = []
y = []
print(id(x))
print(id(y))
print(sys.getrefcount(x))
print(sys.getrefcount(y))

v = {'Species': 'Welsh Corgi', 'legs': 4}
w = {'Species': 'Welsh Corgi', 'legs': 4}
print(id(v))
print(id(w))
print(sys.getrefcount(v))
print(sys.getrefcount(w))
