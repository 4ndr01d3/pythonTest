def reverse(s):
	t=""
	for i in range(len(s)):
		t = t + s [len(s)-i-1]
		
	return t

for i in range(100):	
	print reverse ("animal"+str(i))