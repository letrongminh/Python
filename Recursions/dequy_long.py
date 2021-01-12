def de_quy_long_nhau(m, n):
	if m==0:
		return n+1
	elif n==0:
		return de_quy_long_nhau(m-1, 1)
	else:
		return de_quy_long_nhau(m-1, de_quy_long_nhau(m, n-1))
		pass
test = de_quy_long_nhau(2,1)
print(test)
