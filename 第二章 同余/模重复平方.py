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
	b, n, m = eval(input('分别输入b,n,m：'))
	x = fastExpMod(b, n, m)
	print(str(b) + '^' + str(n) + ' ≡ ' + str(x) + ' (mod ' + str(m) + ').')
	input("Press <enter> to exit.")


main()
