def lowerBase(base):
	if base=="A" or base=="a":
		print "a",
	elif base=="C" or base=="c":
		print "c",
	elif base=="G" or base=="g":
		print "g",
	else:
		print "t",
		
counter = 0
seq = raw_input("sequence? ")
while counter < len(seq):
	lowerBase(seq[counter])
	counter +=1