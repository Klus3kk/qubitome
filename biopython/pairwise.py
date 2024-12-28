from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# Example sequences
seq1 = "ATGCGTACGTAGCTAGCTAGC"
seq2 = "ATGCGTACGTAGCCGCTAGCA"

# Perform global alignment
alignments = pairwise2.align.globalxx(seq1, seq2)

# Display the best alignment
for alignment in alignments[:1]:  # Show top alignment
    print(format_alignment(*alignment))
