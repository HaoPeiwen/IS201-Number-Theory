import random

# 模重复平方法
def fastExpMod(b, n, m):
    result = 1
    n = int(n)
    while n != 0:
        if (n & 1) == 1:
            # ni = 1, then mul
            result = (result * b) % m
        n >>= 1
        # n的二进制向右移位
        b = (b*b) % m
    return result

# 素性检验
def primeTest(n):
    q = n - 1  # Initial q = n-1
    k = 0
    # Find k, q, satisfied 2^k * q = n - 1
    while q % 2 == 0:
        k += 1
        q /= 2
    a = random.randint(2, n-2)
    # If a^q mod n= 1, n maybe is a prime number
    if fastExpMod(a, q, n) == 1:
        return "inconclusive"
    # If there exists j satisfy a ^ ((2 ^ j) * q) mod n == n-1, n maybe is a prime number
    for j in range(0, k):
        if fastExpMod(a, (2**j)*q, n) == n - 1:
            return "inconclusive"
    # a is not a prime number
    return "composite"


def findPrime(halfkeyLength):
    while True:
        n = random.randint(0, 1 << halfkeyLength)
        if n % 2 != 0:
            found = True
            # If n satisfy primeTest 10 times, then n should be a prime number
            for i in range(0, 10):
                if primeTest(n) == "composite":
                    found = False
                    break
            if found:
                return n


def extendedGCD(a, b):
    if b == 0:
        return 1, 0, a
    x1 = 1
    y1 = 0
    x2 = 0
    y2 = 1
    while b != 0:
        q = int(a / b)
        r = a % b
        a = b
        b = r
        x = x1 - q*x2
        x1 = x2
        x2 = x
        y = y1 - q*y2
        y1 = y2
        y2 = y
    return x1, y1, a


def selectE(fn, halfkeyLength):
    while True:
        e = random.randint(0, 1 << halfkeyLength)
        x, y, r = extendedGCD(e, fn)
        if r == 1:
            return e


def computeD(fn, e):
    (x, y, r) = extendedGCD(fn, e)
    if y < 0:
        return fn + y
    return y


def keyGeneration(keyLength):
    halfkeylength = int(keyLength/2)
    p = findPrime(halfkeylength)
    q = findPrime(halfkeylength)
    n = p * q
    fn = (p-1) * (q-1)
    e = selectE(fn, halfkeylength)
    d = computeD(fn, e)
    return n, e, d


def encryption(M, e, n):
    return fastExpMod(M, e, n)


def decryption(C, d, n):
    return fastExpMod(C, d, n)


def main():
    n, e, d = keyGeneration(64)
    f = open("X.txt")
    x = f.read()
    para_num = int(len(x)/9)+1  # 由于64位密钥长度仅支持9位字符串的加密，所以进行分组
    paragraph = []
    XASCII = ''
    Cstring = ''
    jiemi = ''
    for xi in range(para_num):
        paragraph.append(x[xi*9:xi*9+9])
        X = 0
        for i in paragraph[xi]:
            X *= 100
            X += (ord(i) - 23)
        XASCII += str(X)
        C = encryption(X, e, n)
        Cstring += str(C)
        M = decryption(C, d, n)
        Mstring = str(M)
        for i in range(int(len(Mstring)/2)):
            jiemi += chr(int(Mstring[2*i:2*i+2])+23)
    if jiemi == x:
        print('明文为：', x)
        f.close()
        print('明文转化为ASCII： ', XASCII)
        print('通过随机生成p,q,e进行加密后：', Cstring)
        print('解密后: ', jiemi)
        input('Press ENTER to exit.')
    else:
        main()

main()

