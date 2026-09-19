'''A biotech lab enter a dna sequence count the accurance of each nucleotide a ,t, g, c .count how many times a,g,t,c occurred it may be in any order but using count.'''

# Prompt the user to enter their DNA sequence
dna_input = input("Enter the DNA sequence: ")

# Convert to lowercase to handle any case input
sequence = dna_input.upper()

# Count each nucleotide directly using the count method
A_count = sequence.count('A')
T_count = sequence.count('T')
G_count = sequence.count('G')
C_count = sequence.count('C')

# Print the results clearly
print(f"\n Nucleotide Counts:")
print("A: ",A_count)
print("T: ",T_count)
print("G: ",G_count)
print("C: ",C_count)
print("Total Length: ",len(sequence))
