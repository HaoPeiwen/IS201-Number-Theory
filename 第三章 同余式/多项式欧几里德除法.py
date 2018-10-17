def getinput():
    strinput = input('输入多项式系数（最高次到零次），用空格隔开：')
    strinput = strinput.split(' ')
    coefficient = []
    for i in strinput:
        coefficient.append(int(i))
    return coefficient

def getstring(clist):
    n = len(clist) - 1
    string = ''
    for i in range(n-1):
        if clist[i] != 0:
            string += str(clist[i])+'x^'+str(n-i)+' + '
    if clist[n] != 0:
        if clist[i] != 0:
            string += str(clist[n-1])+'x + '
        string += str(clist[n])
    else:
        if clist[i] != 0:
            string += str(clist[n-1])+'x'
    return string

def main():
    print('输入被除式f(x)')
    cfx = getinput()
    n = len(cfx) - 1
    print('输入除式g(x),首项系数为1')
    cgx = getinput()
    m = len(cgx) - 1
    while len(cfx) > m:
        n0 = cfx[0]
        if n0 != 0:
            for i in range(m+1):
                cfx[i] -= n0*cgx[i]
        while cfx[0] == 0:
            cfx.pop(0)
    while cfx[0] == 0:
        cfx.pop(0)
    print('r(x) = ', getstring(cfx))
    input("Press <enter> to exit.")

main()



