import math
n = int(input('输入n以判断其是否为素数：'))
if n>=4:
    nmax = int(math.sqrt(n))
    nroot = int(math.sqrt(nmax))
    SetofPrime = []
    for i in range(1,nmax):
        SetofPrime.append(i+1)
    count = 0
    p = SetofPrime[count]
    while p<=nroot:
        kmax = int(nmax/p)
        for i in range(2,kmax+1):
            if (i*p) in SetofPrime:
                 SetofPrime.remove(i*p)
        count += 1
        p = SetofPrime[count]
    ans = True
    for i in SetofPrime:
        if n%i == 0:
            ans = False
    if ans:
        print(str(n)+'是素数')
    else:
        print(str(n) + '不是素数')
elif n in [2,3]:
    print(str(n) + '是素数')
else:
    print('请重新输入')
input("Press <enter> to exit.")