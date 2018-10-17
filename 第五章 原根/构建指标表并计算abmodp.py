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


def fain(n):  # computing fin
	counter = 0
	lis_of_fin = []
	for i in range(1, n):
		if coprime(i, n):
			counter += 1
			lis_of_fin.append(i)
	return counter, lis_of_fin


def factor_of_fain(n):  # 返回n的因数列表
	lis = []
	for i in range(1, n + 1):
		if n % i == 0:
			lis.append(i)
	return lis


def simplified_residue_system(x):  # 返回x的简化剩余系列表
	result = []
	for i in range(x):
		if coprime(i, x):
			result.append(i)
	return result


def computeg(p):  # 计算p的一个原根g
	fin, lis_of_fin = fain(p)
	facfinlis = factor_of_fain(fin)
	result = []
	for a in lis_of_fin:
		for i in facfinlis:
			if fastExpMod(a, i, p) == 1:
				if i == fin:
					result.append(a)
				break
		if len(result) == 1:
			break
	return result[0]


def main():
	p = input('输入p求其原根的指标列表：')
	p = int(p)
	g = computeg(p)
	fi_p, tmp = fain(p)  # tmp只是占位，无用
	simp = simplified_residue_system(p)  # simp为fi_m的简化剩余系列表
	ind = []
	for d in simp:
		r = fastExpMod(g, d, p)
		ind.append(r)
		print(g, '^', d, ' = ', r, sep='')
	print('以上为以g = ', g, '为底的模p = ', p, '的指标列表', sep='')
	a, b = eval(input('输入a,b求a*b mod p: '))
	(a1, b1) = (a % p, b % p)
	if a1 == 0 or b1 == 0:
		print(a, '*', b, ' mod ', p, '= 0', sep='')
	else:
		index = (ind.index(a1)+ind.index(b1)+2) % fi_p - 1
		print(a, '*', b, ' mod ', p, '=', ind[index], sep='')
	input("Press <enter> to exit.")
main()


