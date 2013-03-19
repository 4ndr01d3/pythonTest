import sys

def parseSequence(sequence,numberperline,indentation=0):
	seq=""
	index=0
	while index<len(sequence):
		seq += " "*indentation +sequence[index:index+numberperline] + "\n"
		index +=numberperline
	return seq
	
def parseFasta(path):
	fastadir={}
	fasta = open(path,"r")
	seq=""
	
	fastalines=fasta.readlines()
	fasta.close()
	if fastalines[0][0]!=">":
		print "ERROR: The file doesn't start with '>', therefore is not in Fasta format"
		return False
	
	fastadir["id"]=fastalines[0][1:].strip()
	
	seq=""
	for i in range(1,len(fastalines)):
		seq += fastalines[i].strip()
	
	fastadir["sequence"]=seq 
	return fastadir

def countNucleotides(sequence):
	lower=sequence.lower()
	a=lower.count("a")
	g=lower.count("g")
	c=lower.count("c")
	t=lower.count("t")
	return (a,g,c,t,len(sequence)-a-g-c-t)
	
def createFastaFile(path,id,sequence):
	file = open(path,"w")
	file.write(">"+id+"\n")
	file.write(parseSequence(sequence,80))
	file.close()
	
	
	
	
	
	
if len(sys.argv)!=2:
	print "ERROR: You must specify a fasta file path."
else:
	path = sys.argv[1]
	fasta=parseFasta(path)
	if fasta==False:
		sys.exit()
	header = "the sequence of the file "+fasta["id"]+ " is:"
	print header
	print parseSequence(fasta["sequence"],50,len(header))
	numbers= countNucleotides(fasta["sequence"])
	print "%5s|%5s|%5s|%5s|%5s"%("A","G","C","T","*")
	print "%5s|%5s|%5s|%5s|%5s"%numbers
	
	header = "The sequence changing T fo U is:"
	print header
	newSeq=fasta["sequence"].replace("t","u").replace("T","U")
	print parseSequence(newSeq,50,len(header))

	path2=raw_input("where do you want to name your files? ")
	createFastaFile(path2+"_T2U.txt",fasta["id"]+"_T2U",newSeq)
	
	rna=""
	for ch in newSeq:
		rna = ch +rna
	
	rna = rna.upper().replace("U","a").replace("A","u").replace("G","c").replace("C","g").upper()
	createFastaFile(path2+"_RNA.txt",fasta["id"]+"_RNA",rna)
	
