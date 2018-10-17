a,b = eval(input('分别输入a，b为被除数和除数：'))
q = int(a/b)
r = a - q*b
print(str(a)+' = '+str(q)+' * '+str(b)+' + '+str(r))
input("Press <enter> to exit.")