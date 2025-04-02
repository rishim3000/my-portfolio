# Bioinformatics Project

This project structure includes the following directories:
- **data**: For input data files
- **scripts**: Python scripts for analysis
- **results**: Output results

## Part 1: Generate Random Sequence Data
- Generate a random DNA sequence of 1 million base pairs (using A, C, G, T).
- Format the sequence with 80 base pairs per line.
- Save the sequence in FASTA format in the "data" directory, with the filename "random_sequence.fasta".

## Part 2: DNA Sequence Operations
- Accept a DNA sequence as a command-line argument
- Implement the following functions:
  - complement(sequence): Returns the complement of a DNA sequence (A -> T, C -> G, G -> C, T -> A).
  - reverse(sequence): Returns the reverse of a sequence (e.g. "CCTCAGC" -> "CAGCCTC").
  - reverse_complement(sequence): Returns the reverse complement of a DNA sequence.

## Part 3: Find Distant Cutsites in Sequence Data

- Accept two arguments : the FASTA file path (data/random_sequence.fasta) and a cut site sequence (e.g., "G|GATCC")
- Read the FASTA file and save the DNA sequence to a variable omitting whitespace.
- Find all occurrences of the cut site (specified below) in the DNA sequence.
- Find all pairs of cut site locations that are 80,000-120,000 base pairs (80-120 kbp) apart.
- Print the total number of cut site pairs found and the positions of the first 5 pairs.
- Save a summary of the results in the results directory as "cutsite_summary.txt".
