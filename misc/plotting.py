import matplotlib.pyplot as plt

# Example nucleotide counts
nucleotide_counts = {"A": 7, "T": 7, "G": 7, "C": 6}

# Plot nucleotide frequencies
plt.bar(nucleotide_counts.keys(), nucleotide_counts.values())
plt.title("Nucleotide Frequency")
plt.xlabel("Nucleotides")
plt.ylabel("Frequency")
plt.show()
