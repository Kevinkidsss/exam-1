"""
## Question 3: DNA Sequence Operations (30 points)
File name: `dna_operations.py`

Create a Python script that performs various operations on DNA sequences. Your script should:

1. Accept a DNA sequence as a command-line argument.
2. Implement the following functions:
   - `complement(sequence)`: Returns the complement of a DNA sequence (A -> T, C -> G, G -> C, T -> A).
   - `reverse(sequence)`: Returns the reverse of a sequence (e.g. "CCTCAGC" -> "CAGCCTC").
   - `reverse_complement(sequence)`: Returns the reverse complement of a DNA sequence (e.g. "CCTCAGC" -> "GAGCTTG"); i.e. the reverse of the complement (apply `complement` then `reverse`, or vice versa).
3. For the input sequence, print:
   - The original sequence
   - Its complement
   - Its reverse
   - Its reverse complement

Tips:
- Create a dictionary mapping each base to its complement for easy lookup; e.g., `complement['A'] = 'T'`.
- String slicing with a step of -1 can be used to reverse a string efficiently.
- Remember to handle both uppercase and lowercase input.
- Use `sys.argv` or `argparse` to access command-line arguments in your script.
- (optional, advanced) Use `str.maketrans()` and `str.translate()` for efficient base substitution.

### Task

Run the script on the sequence "CCTCAGC"

### Example usage
`````
python dna_operations.py GAATTC
`````

Expected output:
`````
Original sequence: GAATTC
Complement: CTTAAG
Reverse: CTTAAG
Reverse complement: GAATTC
`````
"""

import sys

def complement(sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement_dict[base] for base in sequence.upper())

def reverse(sequence):
    return sequence[::-1]

def reverse_complement(sequence):
    return reverse(complement(sequence))

def main():
    if len(sys.argv) < 2:
        print("Provide a DNA sequence")
        sys.exit(1)

    sequence = sys.argv[1]

    print(f"Original sequence: {sequence}")

    print(f"Complement: {complement(sequence)}")

    print(f"Reverse: {reverse(sequence)}")

    print(f"Reverse complement: {reverse_complement(sequence)}")

if __name__ == "__main__":
    main()

#Original sequence: CCTCAGC
#Complement: GGAGTCG
#Reverse: CGACTCC
#Reverse complement: GCTGAGG