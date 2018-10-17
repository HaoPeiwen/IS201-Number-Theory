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
	p = input('输入p(8k+5型素奇数)：')
	p = int(p)
	arf = (p-1)/4
	x = fastExpMod(2, arf, p)
	y = 1
	m = (x*x+y*y)/p
	while m != 1:
		u = x % m
		v = y % m
		x1 = (u*x+v*y)/m
		y1 = (u*y-v*x)/m
		x = x1
		y = y1
		m = (x * x + y * y) / p
	x = int(abs(x))
	y = int(abs(y))
	print('存在正整数x=',x,', y=',y,'使得 x^2+y^2=',p,' 成立',sep='')

main()