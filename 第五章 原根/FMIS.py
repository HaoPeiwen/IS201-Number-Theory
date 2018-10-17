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


def coprime(a, b):  # 判断ab是否互素
	q = int(a / b)
	r = a - q * b
	while r != 0:
		a = b
		b = r
		q = int(a / b)
		r = a - q * b
	if b == 1:
		return True
	else:
		return False


def main():
	pass

if __name__ == '__main__': main()
