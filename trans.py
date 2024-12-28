'''TRANSCRIBE'''

# Input DNA sequence
dna_sequence = "ATGCGTACGTAGCTAGCTAGCTAGCTA"

# Transcribe DNA to RNA
def transcribe_dna_to_rna(sequence):
    return sequence.replace("T", "U")

# Transcribe the sequence
rna_sequence = transcribe_dna_to_rna(dna_sequence)

# Display result
print("RNA Sequence:", rna_sequence)

'''TRANSLATE'''

# Codon table
codon_table = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUA": "Leucine",
    "UAA": "Stop"
}

# Translate RNA to Protein
def translate_rna_to_protein(rna_sequence):
    protein = []
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        amino_acid = codon_table.get(codon, "Unknown")
        if amino_acid == "Stop":
            break
        protein.append(amino_acid)
    return protein


# Execute translation
protein_sequence = translate_rna_to_protein(rna_sequence)

# Display result
print("Protein Sequence:", protein_sequence)