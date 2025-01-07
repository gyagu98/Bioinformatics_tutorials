DNA Sequence GC Content Analysis
This quick project compares the GC content of multiple DNA sequences using a Python script. These DNA sequences are embedded within the python script.


How to Run
To compare the GC content between different sequences, edit the python script to include your DNA sequences of interest and then run:

python3 dna_analysis_2.py

An example output
Sequence 1: ATGCGCGTATCGGCTAGCTAGCTAGGCTAA GC Content: 53.33% Sequence 2: GCGTATCGCGGCTAGCATCGGCTATCGGGC GC Content: 66.67% Sequence 3: ATATATATATATATATATATATATATATAT GC Content: 0.00%

Requirements
Python 3.x

# dna_analysis.py
def gc_content(sequence):
    """Calculate GC content of a DNA sequence."""
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    gc_count = g_count + c_count
    gc_content_percentage = (gc_count / len(sequence)) * 100
    return gc_content_percentage

# Example DNA sequence
sequence = "ATGCGCGTATCGGCTAGCTAGCTAGGCTAA"
print(f"GC Content: {gc_content(sequence):.2f}%")