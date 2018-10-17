import math
nmax = int(input('输入整数n获取0~n以内的素数：'))
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
print(str(nmax)+'以内的素数为：')
for i in range(len(SetofPrime)-1):
    print(SetofPrime[i],end=',')
print(SetofPrime[len(SetofPrime)-1])
input("Press <enter> to exit.")




