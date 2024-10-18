"""
## Question 4: Find Distant Cutsites in FASTA Data (30 points)
File name: `find_cutsites.py`

In molecular biology, restriction enzymes cut DNA at specific sequences called restriction sites or cut sites. Finding pairs of cut sites that are a certain distance apart is important for various genetic engineering techniques. Cutsites are often represented with a vertical bar (|) in the cut site sequence, indicating where the enzyme cuts the DNA.

An example:
- Take cut site sequence "G|GATCC" for BamHI:
- In the sequence dna="AAGG|GATCCTT", the cut site starts at index 4
- The enzyme would cut between G and T, resulting in "AAGG" and "GATCCTT".
- So the cut would happen before dna[4], which we would count as it's location.

Create a Python script that finds pairs of restriction enzyme cut sites that are 80-120 kilobase pairs (kbp) apart in a given FASTA file. Your script should:

1. Accept two arguments: the FASTA file path (data/random_sequence.fasta) and a cut site sequence (e.g., "G|GATCC")
2. Read the FASTA file and save the DNA sequence to a variable omitting whitespace.
3. Find all occurrences of the cut site (specified below) in the DNA sequence.
4. Find all pairs of cut site locations that are 80,000-120,000 base pairs (80-120 kbp) apart.
5. Print the total number of cut site pairs found and the positions of the first 5 pairs.
6. Save a summary of the results in the results directory as "distant_cutsite_summary.txt".

Tips:
- When running the script, put the cut site sequence in quotes to prevent issues with the pipe character, e.g., "G|GATCC".
- Remember to remove the `|` character from the cut site sequence before searching for it in the DNA sequence.
- Consider using string methods like `.replace()` or `strip()` to remove whitespace from the FASTA sequence.
- (optional, advanced) The `re` module can be helpful for finding all occurrences of the cut site in the sequence.

### Task

Run the script on the random sequence you generated in Question 2 and with cut site sequence "G|GATCC" (BamHI)

### Example usage
`````
python find_distant_cutsites.py data/random_sequence.fasta "G|GATCC"
`````

Expected output:
`````
Analyzing cut site: GGATCC
Total cut sites found: 976
Cut site pairs 80-120 kbp apart: 1423
First 5 pairs:
1. 15231 - 101589
2. 15231 - 118956
3. 28764 - 109102
4. 28764 - 126471
5. 42198 - 122609

Results saved to bioinformatics_project/results/distant_cutsite_summary.txt
`````
"""

import sys
import re
import os

# Creating a Function to find cut site locations in the DNA sequence, removing the '|'
def find_cut_sites(sequence, cut_site):
    clean_cut_site = cut_site.replace('|', '')
    return [match.start() for match in re.finditer(clean_cut_site, sequence)]

# Function to find pairs of cut sites that are 80-120 kbp apart
def find_distant_pairs(locations, min_distance=80000, max_distance=120000):
    pairs = []
    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            distance = locations[j] - locations[i]
            if min_distance <= distance <= max_distance:
                pairs.append((locations[i], locations[j]))
    return pairs

def main():
    if len(sys.argv) != 3:
        print("Usage: python find_cutsites.py <fasta_file> <cut_site>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    cut_site = sys.argv[2]

    try:
        with open(fasta_file, 'r') as file:
            sequence = ''.join(line.strip() for line in file if not line.startswith('>'))
    except FileNotFoundError:
        print(f"File {fasta_file} not found.")
        sys.exit(1)

#Find cut sites in the sequence
    cut_site_positions = find_cut_sites(sequence, cut_site)
    print(f"Total cut sites found: {len(cut_site_positions)}")

#Find cut site pairs
    cut_site_pairs = find_distant_pairs(cut_site_positions)
    print(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}")

    print("First 5 pairs:")
    for i, (pos1, pos2) in enumerate(cut_site_pairs[:5], 1):
        print(f"{i}. {pos1} - {pos2}")

    results_file = 'C:/Users/kevin/OneDrive/Desktop/UCSF Fall 2024/Datasci 217/Intro to Python/bioinformatics_project/results/cutsite_summary.txt'
    with open(results_file, 'w') as f:
        f.write(f"Analyzing cut site: {cut_site.replace('|', '')}\n")
        f.write(f"Total cut sites found: {len(cut_site_positions)}\n")
        f.write(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}\n")
        f.write("First 5 pairs:\n")
        for i, (pos1, pos2) in enumerate(cut_site_pairs[:5], 1):
            f.write(f"{i}. {pos1} - {pos2}\n")
    
    print(f"Results saved to {results_file}")


if __name__ == "__main__":
    main()

"""
Total cut sites found: 226
Cut site pairs 80-120 kbp apart: 1872
First 5 pairs:
1. 6824 - 112539
2. 6824 - 113552
3. 6824 - 117069
4. 6824 - 120383
5. 10067 - 112539
"""