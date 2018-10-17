from FMIS import*


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


def main():
	m = input('输入m求其原根列表：')
	m = int(m)
	fin, lis_of_fin = fain(m)
	facfinlis = factor_of_fain(fin)
	result = []
	for a in lis_of_fin:
		for i in facfinlis:
			if fastExpMod(a, i, m)==1:
				if i== fin:
					result.append(a)
				break
	print(result)
	input("Press <enter> to exit.")
main()



