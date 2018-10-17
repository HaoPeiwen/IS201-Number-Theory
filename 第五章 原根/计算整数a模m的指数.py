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


def main():
	a, m = eval(input('分别输入a,m：'))
	for i in range(1,m):
		if fastExpMod(a, i, m)==1:
			print(a,'模',m,'的指数为',i,sep='')
			break
	input("Press <enter> to exit.")
main()

