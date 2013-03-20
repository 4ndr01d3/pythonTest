import sys
import os.path

def parseSequence(sequence,numberperline,indentation=0):
	seq=""
	index=0
	while index<len(sequence):
		seq += " "*indentation +sequence[index:index+numberperline] + "\n"
		index +=numberperline
	return seq
	
def parseFasta(path):
	fastadir={}
	fileisNotOK=True
	if os.path.exists(path) and os.path.isfile(path):
		fasta = open(path,"r")
		seq=""

		fastalines=fasta.readlines()
		fasta.close()
		if fastalines[0][0]!=">":
			raise ValueError("ERROR: The file doesn't start with '>', therefore is not in Fasta format")
		else:
			fileisNotOK=False
	else:
		raise ValueError("ERROR: The file doesn't exist or is not a file")

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
	
	
	
	
codon_table = {
    'A': ('GCT', 'GCC', 'GCA', 'GCG'),
    'C': ('TGT', 'TGC'),
    'D': ('GAT', 'GAC'),
    'E': ('GAA', 'GAG'),
    'F': ('TTT', 'TTC'),
    'G': ('GGT', 'GGC', 'GGA', 'GGG'),
    'I': ('ATT', 'ATC', 'ATA'),
    'H': ('CAT', 'CAC'),
    'K': ('AAA', 'AAG'),
    'L': ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'),
    'M': ('ATG',),
    'N': ('AAT', 'AAC'),
    'P': ('CCT', 'CCC', 'CCA', 'CCG'),
    'Q': ('CAA', 'CAG'),
    'R': ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
    'S': ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'),
    'T': ('ACT', 'ACC', 'ACA', 'ACG'),
    'V': ('GTT', 'GTC', 'GTA', 'GTG'),
    'W': ('TGG',),
    'Y': ('TAT', 'TAC'),
    '*': ('TAA', 'TAG', 'TGA'),
}
codonTable={}
for aa in codon_table:
	for codon in codon_table[aa]:
		codonTable[codon]=aa

def translate(seq):
	aaseq=""
	for i in range(0,len(seq),3):
		codon = seq[i:i+3]
		if len(codon)==3:
			aaseq += codonTable[codon.upper()]	
	return aaseq
	
if len(sys.argv)!=2:
	print "ERROR: You must specify a fasta file path."
else:
	path = sys.argv[1]
	try:
		fasta=parseFasta(path)
	except ValueError:
		print "error in file"
		sys.exit()
	
	header = "the sequence of the file "+fasta["id"]+ " is:"
	print header
	print parseSequence(fasta["sequence"],50,len(header))
	aa= translate(fasta["sequence"])
	header = "The protein sequence is"
	print header
	print parseSequence(aa,50,len(header))
