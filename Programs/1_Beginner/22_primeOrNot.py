from math import sqrt

n = 18
p_fl = 0

if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            p_fl = 1
            break
    if (p_fl == 0):
        print("True")
    else:
        print("False")
else:
    print("False")
