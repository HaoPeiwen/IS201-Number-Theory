m = input('输入m(奇素数)：')
m = int(m)
quadratic_residue = []
non_quadratic_residue = []
for i in range(1,m):
	x = (i**2) % m
	if x not in quadratic_residue:
		quadratic_residue.append(x)
for i in range(1, m):
	if i not in quadratic_residue:
		non_quadratic_residue.append(i)
quadratic_residue.sort()
non_quadratic_residue.sort()
print(m,'的平方剩余为：',quadratic_residue,sep='')
print(m,'的非平方剩余为：',non_quadratic_residue,sep='')
input('press ENTER to exit.')
