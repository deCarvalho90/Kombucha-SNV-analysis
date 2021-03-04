# Script to find gene equivalent pairs based on the first line of fasta sequence
# Output: list of gene names and their equivalents from genomes space and Earth
import sys
from pyfasta import Fasta

g311 = sys.argv[1] # space ffn file (space)
g314 = sys.argv[2] # Earth ffn file (Earth)
f311 = Fasta(g311)
f314 = Fasta(g314)

snvs = [] # list of number of snvs between pairs of corresponding genes
percent = [] # List of % of SNV in pairs of genes

for g1 in f311:
	seq1 = f311[g1]
	st1 = seq1[:60]
	for g2 in f314:
		seq2 = f314[g2]
		st2 = seq2[:60]
		if st1 == st2:
			if len(seq1) == len(seq2):
			count += 1
			print(g1+';'+g2+';'+str(len(seq1))+';'+str(len(seq2)))
