n = 10


for i in range(1, n):
    print(i*'*')
    
for i in range(n, 0, -1):
    print(i*'*')
    
for i in range (n, 0, -1):
    print((n-i) * ' ' + i * '*')