import fastaExample4
import sys

if len(sys.argv)!=2:
	print "ERROR: You must specify a fasta file path."
else:
	path = sys.argv[1]
	fasta=fastaExample4.getAllFastARecords(path)
	print fasta
