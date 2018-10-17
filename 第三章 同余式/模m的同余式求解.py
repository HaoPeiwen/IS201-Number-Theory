def primejudge(n):  # 判断是否为素数
	import math
	if n >= 4:
		nmax = int(math.sqrt(n))
		nroot = int(math.sqrt(nmax))
		SetofPrime = []
		for i in range(1, nmax):
			SetofPrime.append(i + 1)
		count = 0
		p = SetofPrime[count]
		while p <= nroot:
			kmax = int(nmax / p)
			for i in range(2, kmax + 1):
				if (i * p) in SetofPrime:
					SetofPrime.remove(i * p)
			count += 1
			p = SetofPrime[count]
		ans = True
		for i in SetofPrime:
			if n % i == 0:
				ans = False
		return ans
	elif n in [2, 3]:
		return True
	else:
		return False


def getprimeset(n):  # 得到n/2以内的素数列表
	import math
	nmax = int(n / 2)
	nroot = int(math.sqrt(nmax))
	SetofPrime = []
	for i in range(1, nmax):
		SetofPrime.append(i + 1)
	count = 0
	p = SetofPrime[count]
	while p <= nroot:
		kmax = int(nmax / p)
		for i in range(2, kmax + 1):
			if (i * p) in SetofPrime:
				SetofPrime.remove(i * p)
		count += 1
		p = SetofPrime[count]
	return SetofPrime


def getvalue_fx(clist, x):  # 求f(x)在x处的算数值
	result = clist[0]
	for i in range(len(clist) - 1):
		result = result * x + clist[i + 1]
	return result


def resolve_m(n):  # 若m不是质数则分解为质数求解 (这里要求分解后质数的指数为1)
	setofprime = getprimeset(n)  # 得到n/2以内的素数列表
	primelist = []
	timeslist = []
	for i in setofprime:
		while n != 1 and n % i == 0:
			n = int(n / i)
			if i not in primelist:
				primelist.append(i)
				timeslist.append(1)
			else:
				timeslist[primelist.index(i)] += 1
		if n == 1:
			break
	return primelist, timeslist


def getinput_fx():
	strinput = input('输入多项式系数（最高次到零次），用空格隔开：')
	strinput = strinput.split(' ')
	coefficient = []
	for i in strinput:
		coefficient.append(int(i))
	return coefficient


def solve(clist, m):  # 计算同余式
	clist = simplify(clist, m)
	root = []
	for i in range(m):
		ri = getvalue_fx(clist, i)
		if ri % m == 0:
			root.append(i)
	return root


def simplify(clist, m):  # 同余式化简为r(x)
	coefficient = [1]
	for i in range(m - 2):
		coefficient.append(0)
	coefficient.append(-1)
	coefficient.append(0)
	n = len(clist) - 1
	m = len(coefficient) - 1
	while len(clist) > m:
		n0 = clist[0]
		if n0 != 0:
			for i in range(m + 1):
				clist[i] -= n0 * coefficient[i]
		while clist[0] == 0:
			clist.pop(0)
	while clist[0] == 0:
		clist.pop(0)
	return clist


def composite_solve(clist, m):
	mlist, mtimes = resolve_m(m)
	for i in range(len(mlist)):
		if mtimes[i] != 1:  # 素数高次同余式
			gaoci(clist, m, mlist[i], mtimes[i])
			mlist.remove(mlist[i])
	rdic = []  # 原式modmi的解的二维数组
	Mlis = []  # Mi中国剩余定理
	i = 0
	for mi in mlist:
		root = solve(clist, mi)
		rdic.append(root)
		Mlis.append(int(m / mi))
		Mp = compute_Mp(mi, Mlis[i], mi)
		Mlis[i] = Mlis[i] * Mp
		i += 1
	for i in range(len(mlist)):
		for j in range(len(rdic[i])):
			rdic[i][j] = (rdic[i][j] * Mlis[i]) % m
	return Chiremainder(rdic, m)


def compute_Mp(a, b, mi):
	if b == 0:
		return 1, 0, a
	x1 = 1
	y1 = 0
	x2 = 0
	y2 = 1
	while b != 0:
		q = int(a / b)
		r = a % b
		a = b
		b = r
		x = x1 - q * x2
		x1 = x2
		x2 = x
		y = y1 - q * y2
		y1 = y2
		y2 = y
	if y1 < 0:
		return mi + y1
	return y1


Sum = 0
outlist = []


def Chiremainder(rdic, m):
	n = len(rdic)
	dfs(0, rdic, n)
	for i in range(len(outlist)):
		outlist[i] = outlist[i] % m
	return outlist


def dfs(floor, rdic, n):
	global Sum
	if floor == n:
		outlist.append(Sum)
	else:
		for i in rdic[floor]:
			Sum += i
			dfs(floor+1, rdic, n)
			Sum -= i


def gaoci(clist, m, mi, a):  # 模mi的a次方
	pass


def main():
	print('输入f(x)')
	cfx = getinput_fx()
	m = input('输入m:')
	m = int(m)
	if primejudge(m):
		root = solve(cfx, m)
	else:
		root = composite_solve(cfx, m)
	root.sort()
	print('x ≡ ', end='', sep='')
	for i in range(len(root) - 1):
		print(root[i], ', ', end='', sep='')
	print(root[len(root) - 1], ' (mod', m, ')', sep='')
	input("Press <enter> to exit.")


main()
