a, b = eval(input('分别输入m，a判断其是否互素：'))
A = str(a)
B = str(b)
q = int(a/b)
r = a - q*b
while r != 0:
    a = b
    b = r
    q = int(a/b)
    r = a - q * b
if b == 1:
    print(A+','+B+'互素。')
else:
    print(A+','+B+'不是互素。')
input("Press <enter> to exit.")