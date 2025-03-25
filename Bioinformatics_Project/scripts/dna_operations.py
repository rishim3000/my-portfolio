import argparse


def complement(sequence):
    sequence = sequence.upper()
    complement_dict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}

    result = ''.join(complement_dict[base] for base in sequence)
    return result

def reversed(sequence):
     result = sequence[::-1]
     return result

def reverse_complement(sequence):
    complemented_sequence = complement(sequence)
    result = complemented_sequence[::-1]
    return result


def main():
    parser = argparse.ArgumentParser(description="Get the complement of a DNA sequence.")
    
    parser.add_argument("sequence", type=str, help="The input DNA sequence.")
    
    args = parser.parse_args()
    
    # All operations
    complemented_sequence = complement(args.sequence)
    reverse_sequence = reversed(args.sequence)
    reversed_complement = reverse_complement(args.sequence)

    print("Original sequence: ", args.sequence)
    print("Complement: ", complemented_sequence)
    print("Original Reversed: ", reverse_sequence)
    print("Complement Reversed: ", reversed_complement)

if __name__ == "__main__":
    main()                          

