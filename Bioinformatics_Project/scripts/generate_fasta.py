import random 
import textwrap

def random_DNA_seq(length):

    characters = 'ATCG'
    sequence = ''.join(random.choice(characters)for i in range(length))
    return sequence

sequence = random_DNA_seq(1000000)

sequence_80char = '\n'.join(textwrap.wrap(sequence, width=80))

fasta_stuff = f'>Random DNA Sequence\n{sequence_80char}'

filepath = "/workspaces/05-first-exam-rishim3000/bioinformatics_project/data/random_sequence.fasta"

with open(filepath, 'w') as fasta_file:
    fasta_file.write(fasta_stuff)