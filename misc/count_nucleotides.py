# Input DNA sequence
dna_sequence = "ATGCGTACGTAGCTAGCTAGCTAGCTA"

# Count nucleotides
def count_nucleotides(sequence):
    return {nucleotide: sequence.count(nucleotide) for nucleotide in "ATGC"}

# Execute function
nucleotide_counts = count_nucleotides(dna_sequence)

# Display results
print("DNA Sequence:", dna_sequence)
print("Nucleotide Counts:", nucleotide_counts)
