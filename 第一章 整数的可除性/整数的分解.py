def factors(a, b):
    q = int(a / b)
    r = a - q * b
    while r != 0:
        a = b
        b = r
        q = int(a / b)
        r = a - q * b
    return b

def main():
    n = int(input('输入正合数n: '))
    a, b = eval(input('分别输入a，b(要求a>b)验证其是否满足整数分解定理：'))
    if a>b and (a*a-b*b)%n == 0 and (a-b)%n != 0 and (a+b)%n != 0:
        ansa = factors(n, a-b)
        ansb = factors(n, a+b)
        print('(n,a-b) = '+ str(ansa)+',  (n,a+b) = '+str(ansb))
    else:
        print('输入错误')
    input("Press <enter> to exit.")
main()