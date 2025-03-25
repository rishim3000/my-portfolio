import sys
import os

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        sequence = ''.join(line.strip() for line in file if not line.startswith('>'))
    return sequence

def find_cut_sites(sequence, cut_site):

    cut_positions = []
    cut_site = cut_site.replace('|', '')  # Remove the pipe symbol from the cut site
    pos = sequence.find(cut_site)
    while pos != -1:
        cut_positions.append(pos)
        pos = sequence.find(cut_site, pos + 1)
    return cut_positions

def find_distant_pairs(cut_positions, min_distance=80000, max_distance=120000):
    "80-120 kbp apart."
    cut_site_pairs = []
    for i in range(len(cut_positions)):
        for j in range(i + 1, len(cut_positions)):
            distance = cut_positions[j] - cut_positions[i]
            if min_distance <= distance <= max_distance:
                cut_site_pairs.append((cut_positions[i], cut_positions[j]))
    return cut_site_pairs

def save_summary(pairs, output_path, total_sites, cut_site):
    with open(output_path, 'w') as file:
        file.write(f"Analyzing cut site: {cut_site}\n")
        file.write(f"Total cut sites found: {total_sites}\n")
        file.write(f"Cut site pairs 80-120 kbp apart: {len(pairs)}\n")
        file.write("First 5 pairs:\n")
        for idx, pair in enumerate(pairs[:5], 1):
            file.write(f"{idx}. {pair[0]} - {pair[1]}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python find_cutsites.py <fasta_file> <cut_site>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    cut_site = sys.argv[2]
    
    if not os.path.exists(fasta_file):
        print(f"Error: File '{fasta_file}' not found.")
        sys.exit(1)

    # Read the DNA sequence from the FASTA file
    dna_sequence = read_fasta(fasta_file)

    # Find all cut site positions
    cut_positions = find_cut_sites(dna_sequence, cut_site)

    # Find pairs of cut sites that are 80-120 kbp apart
    cut_site_pairs = find_distant_pairs(cut_positions)

    # Print the results
    print(f"Analyzing cut site: {cut_site.replace('|', '')}")
    print(f"Total cut sites found: {len(cut_positions)}")
    print(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}")
    print("First 5 pairs:")
    for idx, pair in enumerate(cut_site_pairs[:5], 1):
        print(f"{idx}. {pair[0]} - {pair[1]}")

    # Save the summary
    results_dir = "/workspaces/05-first-exam-rishim3000/bioinformatics_project/results"
    os.makedirs(results_dir, exist_ok=True)
    summary_file = os.path.join(results_dir, "cutsite_summary.txt")
    save_summary(cut_site_pairs, summary_file, len(cut_positions), cut_site.replace('|', ''))

    print(f"Results saved to {summary_file}")

if __name__ == "__main__":
    main()
