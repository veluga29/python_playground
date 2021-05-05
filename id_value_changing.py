import sys

print(sys.getrefcount(1000))  # 3
x = 1000
print('x = ', x, ', x ID:', id(x))  # x =  1000 , x ID: 2816230422768
y = 1000
print('y = ', y, ', y ID:', id(y))  # y =  1000 , y ID: 2816230422768
print(sys.getrefcount(1000))  # 5
x += 1
x -= 1
print('------after operation------')
print('x = ', x, ', x ID:', id(x))  # x =  1000 , x ID: 2816233474000
print('y = ', y, ', y ID:', id(y))  # y =  1000 , y ID: 2816230422768
print(sys.getrefcount(1000))  # 4
