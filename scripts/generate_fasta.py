"""
## Question 2: Generate Random FASTA Data (25 points)
File name: `generate_fasta.py`

FASTA format is a text-based format for representing nucleotide or peptide sequences. FASTA files usually include a header line with the `> Sequence Name` before the sequence data, but this is not required for this assignment. Examples of FASTA files can be found on its [Wikipedia page](https://en.wikipedia.org/wiki/FASTA_format).

Create a Python script that generates a random DNA sequence and saves it in FASTA format. Your script should:

1. Generate a random DNA sequence of 1 million base pairs (using A, C, G, T).
2. Format the sequence with 80 base pairs per line.
3. Save the sequence in FASTA format in the "data" directory, with the filename "random_sequence.fasta".

Tips:
- Use Python's `random` module to generate random DNA sequences.
- Remember to open the file in write mode when saving the FASTA data.
- Use string joining for efficient concatenation of large sequences.
- Use a `for` loop to count characters when adding each line of the sequence to the file.
- (optional, advanced) The `textwrap` module can help you format the sequence into 80-character lines.

### Task

Run the script and check the output (include it in your repository).

### Example usage
```
python generate_fasta.py
```

Expected output:
```
Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta
"""


import os
import random

def generate_random_dna_sequence(length):
    return ''.join(random.choices('ACGT', k=length))

def format_fasta(sequence, line_length=80):
    return '\n'.join(sequence[i:i+line_length] for i in range(0, len(sequence), line_length))

def save_fasta(sequence, filepath):
    with open(filepath, 'w') as file:
        file.write(">random_sequence\n")
        file.write(sequence)

def main():
    sequence_length = 1_000_000
    sequence = generate_random_dna_sequence(sequence_length)
    formatted_sequence = format_fasta(sequence)
    
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(output_dir, exist_ok=True)
    output_filepath = os.path.join(output_dir, 'random_sequence.fasta')
    
    save_fasta(formatted_sequence, output_filepath)
    print(f"Random DNA sequence saved to {output_filepath}")

if __name__ == "__main__":
    main()