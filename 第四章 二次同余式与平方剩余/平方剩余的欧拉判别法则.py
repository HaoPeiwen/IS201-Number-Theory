def fastExpMod(b, n, m):
	result = 1
	n = int(n)
	while n != 0:
		if (n & 1) == 1:
			# ni = 1, then mul
			result = (result * b) % m
		n >>= 1
		# n的二进制向右移位
		b = (b * b) % m
	return result


def main():
	a, p = eval(input('分别输入a, p：'))
	n = (p - 1) / 2
	x = fastExpMod(a, n, p)
	if x == 1:
		print(a, '是模', p, '的平方剩余', sep='')
	else:
		print(a, '是模', p, '的非平方剩余', sep='')
	input("Press <enter> to exit.")


main()
