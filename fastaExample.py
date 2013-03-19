import sys

if len(sys.argv)!=2:
	print "ERROR: You must specify a fasta file path."
else:
	path = sys.argv[1]

	fasta = open(path,"r")
	seq=""
	firstChar=True
	for line in fasta:
		for n in line:
			if firstChar:
				if n!=">":
					print "ERROR: The file doesn't start with '>', therefore is not in Fasta format"
					sys.exit()
			firstChar=False		
			seq +=n
		
	print seq