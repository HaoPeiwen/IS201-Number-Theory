a, b = eval(input('分别输入a，b求其最大公因数：'))
A = str(a)
B = str(b)
q = int(a/b)
r = a - q*b
while r != 0:
    a = b
    b = r
    q = int(a/b)
    r = a - q * b
print('('+A+','+B+')'+'的最大公因数是'+str(b))
input("Press <enter> to exit.")