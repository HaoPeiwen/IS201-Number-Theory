import random


def fastExpMod(b, n, m):
	result = 1
	n = int(n)
	while n != 0:
		if (n & 1) == 1:  # ni = 1, then mul
			result = (result * b) % m
		n >>= 1  # n的二进制向右移位
		b = (b * b) % m
	return result


def SinglePrimeTest(n):
	t = n - 1  # Initial t = n - 1, s = 0, then 2^s * t == n - 1.
	s = 0
	while t % 2 == 0:  # Find s, t, satisfied 2^s * t = n - 1.
		s += 1
		t /= 2
	b = random.randint(2, n - 2)
	if fastExpMod(b, t, n) == 1:  # If a^q mod n = 1, n maybe is a prime number
		return "inconclusive"
	for r in range(0, s):  # If there exists j satisfy a ^ ((2 ^ j) * q) mod n == n-1, n maybe is a prime number
		if fastExpMod(b, (2 ** r) * t, n) == n - 1:
			return "inconclusive"
	return "composite"  # Or, a is not a prime number


def main():
	k = int(input('安全参数: '))
	n = int(input('检验奇整数n: '))
	found = True
	for i in range(k):
		if SinglePrimeTest(n) == "composite":
			found = False
			break
	if found:
		print(n, 'is large probability a prime number.')
	else:
		print(n, 'is a sum number.')
	input('press <enter> to exit.')


if __name__ == '__main__':
	main()
