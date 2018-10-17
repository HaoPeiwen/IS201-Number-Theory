import math
def getprimeset(n):
    nmax = int(n / 2)
    nroot = int(math.sqrt(nmax))
    SetofPrime = []
    for i in range(1, nmax):
        SetofPrime.append(i+1)
    count = 0
    p = SetofPrime[count]
    while p <= nroot:
        kmax = int(nmax/p)
        for i in range(2, kmax+1):
            if (i*p) in SetofPrime:
                SetofPrime.remove(i*p)
        count += 1
        p = SetofPrime[count]
    return SetofPrime

def main():
    n = int(input('输入n，以分解素因数：'))
    N = str(n)
    setofprime = getprimeset(n)  #得到n/2以内的素数列表
    primelist = []
    timeslist = []
    for i in setofprime:
        while n != 1 and n % i == 0:
            n = int(n/i)
            if i not in primelist:
                primelist.append(i)
                timeslist.append(1)
            else:
                timeslist[primelist.index(i)] += 1
        if n == 1:
            break
    length = len(primelist)
    print(N+' = ', end='')
    for i in range(length-1):
        print(str(primelist[i])+'^'+str(timeslist[i]), end=' * ')
    print(str(primelist[length-1])+'^'+str(timeslist[length-1]))
    input("Press <enter> to exit.")
main()



