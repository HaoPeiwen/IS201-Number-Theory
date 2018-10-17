print('此程序用贝祖等式求两不全为零整数的最大公因数')
a, b = eval(input('分别输入a，b：'))
A = str(a)
B = str(b)
r = [a, b]
s = [1, 0]
t = [0, 1]
j = 2
ans = True
if r[1] == 0:
    ss = str(s[0])
    tt = str(t[0])
    gys = s[0]*a+t[0]*b
    ans = False
else:
    q0 = int(r[0]/r[1])
    r0 = (-q0)*r[1] + r[0]
    r.append(r0)
while (r[j] != 0) and ans:
    s0 = (-q0)*s[j-1] + s[j-2]
    s.append(s0)
    t0 = (-q0)*t[j-1] + t[j-2]
    t.append(t0)
    q0 = int(r[j-1]/r[j])
    r0 = (-q0)*r[j] + r[j-1]
    r.append(r0)
    j += 1
if not ans:
    if s[0]<0:
        ss = '('+ss+')'
    if t[0]<0:
        tt = '('+tt+')'
    print('存在s = '+ss+' , t = '+tt+'使得')
    print(ss+'*'+A+' + '+tt+'*'+B+' = '+str(gys))
else:
    S = s[len(s)-1]
    ss = str(S)
    T = t[len(t)-1]
    tt = str(T)
    gys = S*a+T*b
    if S<0:
        ss = '(' + str(S) + ')'
    if T< 0:
        tt = '(' + str(T) + ')'
    print('存在s = '+str(S)+' , t = '+str(T)+'使得')
    print(ss + '*' + A + ' + ' + tt + '*' + B + ' = ' + str(gys))
input("Press <enter> to exit.")