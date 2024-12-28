def parse_fasta(file_path):
    sequences = {}
    with open(file_path, "r") as file:
        current_sequence_name = None
        current_sequence = []
        for line in file:
            line = line.strip()
            if line.startswith(">"):  # Sequence name
                if current_sequence_name:
                    sequences[current_sequence_name] = "".join(current_sequence)
                current_sequence_name = line[1:]  # Remove ">"
                current_sequence = []
            else:  # Sequence data
                current_sequence.append(line)
        if current_sequence_name:
            sequences[current_sequence_name] = "".join(current_sequence)
    return sequences

# Parse a FASTA file
file_path = "fasta/example.fasta"  
parsed_sequences = parse_fasta(file_path)
print("Parsed Sequences:", parsed_sequences)
