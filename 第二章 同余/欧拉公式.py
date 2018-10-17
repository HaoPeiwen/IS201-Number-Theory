def coprime(a,b):
    q = int(a/b)
    r = a - q*b
    while r != 0:
        a = b
        b = r
        q = int(a/b)
        r = a - q * b
    if b == 1:
        return True
    else:
        return False

def main():
    n = int(input('输入n求得φ(n): '))
    counter = 0
    for i in range(1,n):
        if coprime(i,n):
            counter += 1
    print('φ(n) = '+str(counter))
    input("Press <enter> to exit.")

main()
