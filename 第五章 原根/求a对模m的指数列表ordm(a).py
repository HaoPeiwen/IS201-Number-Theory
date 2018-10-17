from FMIS import*


def fain(n):  # computing fin
	counter = 0
	lis_of_fin = []
	for i in range(1, n):
		if coprime(i, n):  # from FMIS functions
			counter += 1
			lis_of_fin.append(i)
	return counter, lis_of_fin


def factor_of_fain(n):  # 返回n的因数列表
	lis = []
	for i in range(1, n + 1):
		if n % i == 0:
			lis.append(i)
	return lis


def main():
	m = input('输入m求其ordm(a)列表：')
	m = int(m)
	fin, lis_of_fin = fain(m)
	facfinlis = factor_of_fain(fin)
	key = []
	value = []
	for a in lis_of_fin:
		for i in facfinlis:
			if fastExpMod(a, i, m) == 1:
				key.append(a)
				value.append(i)
				break
	result = dict(zip(key, value))
	print('{a:ordm(a)} 的字典为：', result)
	input("Press <enter> to exit.")
main()



