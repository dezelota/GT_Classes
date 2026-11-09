"""
L8 Exercise - Genomics I: Parsing a genome with pyfaidx

Group Members: [Desiree Bogen, Ashley Bolen, Nathan Solomon]

Overview:
Today you will use pyfaidx to explore the Lake Malawi cichlid genome (Maylandia zebra,
assembly GT3a). The motif-finding functions you write in Q6 and Q7 will be reused in Project 2.

Before you start:
  1. Download GCF_041146795.1_Mzebra_GT3a_genomic.fna.gz and uncompress it:
         gunzip GCF_041146795.1_Mzebra_GT3a_genomic.fna.gz
  2. Make sure pyfaidx is installed in your conda environment:
         pip install pyfaidx
  3. Run this script from the terminal like this:
         python "L12 - Genomics1.py" GCF_041146795.1_Mzebra_GT3a_genomic.fna
     The first run takes a minute while pyfaidx builds the index file (.fai). Later runs are fast.

Two things to know about this genome file:
  * COORDINATES: Biologists (and genome browsers, GFF and VCF files) count bases starting at 1.
    Python slicing counts from 0. pyfaidx slicing works like Python, e.g. genome[chrom][0:10]
    returns bases 1-10. get_spliced_seq() is the exception: it takes 1-based coordinates.
  * SOFT-MASKING: Repetitive DNA is written in lowercase letters (acgt) and the rest is
    uppercase (ACGT). Both are real DNA sequence.

Collaboration / Submission:
You are welcome to work with your team on this assignment. Please submit one script per team.
Print each answer under its "Q# Output(s):" line so the TA can find it.
Due: TBD
"""

"""
L8 Exercise - Genomics I: Parsing a genome with pyfaidx

Group Members: []

Overview:
Today you will use pyfaidx to explore the Lake Malawi cichlid genome (Maylandia zebra,
assembly GT3a). The motif-finding functions you write in Q6 and Q7 will be reused in Project 2.

Before you start:
  1. Download GCF_041146795.1_Mzebra_GT3a_genomic.fna.gz and uncompress it:
         gunzip GCF_041146795.1_Mzebra_GT3a_genomic.fna.gz
  2. Make sure pyfaidx is installed in your conda environment:
         pip install pyfaidx
  3. Run this script from the terminal like this:
         python "L12 - Genomics1.py" GCF_041146795.1_Mzebra_GT3a_genomic.fna
     The first run takes a minute while pyfaidx builds the index file (.fai). Later runs are fast.

Two things to know about this genome file:
  * COORDINATES: Biologists (and genome browsers, GFF and VCF files) count bases starting at 1.
    Python slicing counts from 0. pyfaidx slicing works like Python, e.g. genome[chrom][0:10]
    returns bases 1-10. get_spliced_seq() is the exception: it takes 1-based coordinates.
  * SOFT-MASKING: Repetitive DNA is written in lowercase letters (acgt) and the rest is
    uppercase (ACGT). Both are real DNA sequence.

Collaboration / Submission:
You are welcome to work with your team on this assignment. Please submit one script per team.
Print each answer under its "Q# Output(s):" line so the TA can find it.
Due: TBD
"""

import argparse
import re
import pyfaidx

# ------------------------------------------------------------------------------------------
# Q1 (1 pt). Use argparse to take in one positional argument, GenomeFile (the fasta file).
#            Then use pyfaidx.Fasta() to read the genome into a variable called genome.
# ------------------------------------------------------------------------------------------
print('Q1 Output(s):')
parser = argparse.ArgumentParser(description='Read in fasta file')
parser.add_argument('GenomeFile', type=str, help='Path to the genome FASTA file')
args = parser.parse_args()

genome = pyfaidx.Fasta(args.GenomeFile)  # replace None with your pyfaidx.Fasta object

# ------------------------------------------------------------------------------------------
# Q2 (1 pt). The genome contains assembled chromosomes (names start with "NC_") and many
#            small unplaced scaffolds (names start with "NW_").
#   a. Print the total number of sequences in the file.
#   b. Use a list comprehension to make a list called chromosomes that holds only the names
#      that start with "NC_". Print how many there are, and print the list.
#   c. Store the first chromosome's name in a variable called chrom1. You will use it below.
# ------------------------------------------------------------------------------------------
print('\nQ2 Output(s):')
print("Total Number of Sequences:", len(genome))
chromosomes = [name for name in genome.keys() if name.startswith("NC_")] # replace with your list comprehension
print("Number of chromosomes:", len(chromosomes))
print(chromosomes)
chrom1 = chromosomes[0]     # replace None with the first chromosome name

# ------------------------------------------------------------------------------------------
# Q3 (1.5 pts). Coordinates.
#   a. Get bases 1,001 to 1,100 of chrom1. These are 1-based biologist coordinates, so convert
#      them to a Python slice. Print the sequence and its length. The length should be 100.
#   b. pyfaidx Sequence objects have .start and .end attributes. Print them. Are they
#      1-based or 0-based? Answer in a comment.
#   c. Print the reverse complement of the same region. Use only pyfaidx attributes, not your
#      own function. Hint: try dir() on the region.
# ------------------------------------------------------------------------------------------
print('\nQ3 Output(s):')

seq1 = genome[chrom1][1000:1100]
print("sequence:", seq1, "\nlength of sequence:", len(seq1))
print(seq1.start, seq1.end)
print(seq1.reverse.complement)

# b. Are .start and .end 1-based or 0-based? 
# 1-based. The slice [1000:1100] gives .start = 1001 and .end = 1100.

# ------------------------------------------------------------------------------------------
# Q4 (1.5 pts). Splicing a gene.
#   A gene's exons are listed below in 1-based coordinates, the way they appear in the
#   genome's annotation (.gff) file. Use genome.get_spliced_seq() to join the exons into one
#   sequence. Print the length of the spliced sequence and its first 30 bases.
#   Check: the total length should equal the sum of the exon lengths. Calculate that sum with
#   a list comprehension and print it too.
# ------------------------------------------------------------------------------------------
print('\nQ4 Output(s):')
exons = [[5001, 5310], [6201, 6400], [7101, 7255]]
spliced = genome.get_spliced_seq(chrom1, exons)
print("length of spliced sequence:", len(spliced), spliced[0:30])

exon_lengths = [end - start + 1 for start, end in exons]
print("sum of exon lengths:", sum(exon_lengths))

# ------------------------------------------------------------------------------------------
# Q5 (1.5 pts). GC content.
#   For each chromosome in your chromosomes list, print the chromosome name, its length in bp,
#   its GC content (use pyfaidx's .gc attribute, round to 3 decimals), and the fraction of the
#   chromosome that is soft-masked (lowercase a, c, g or t; round to 3 decimals).
#   Hint: genome[name][:].seq gives you the whole chromosome as a string.
# ------------------------------------------------------------------------------------------
print('\nQ5 Output(s):')
for name in chromosomes:
    region = genome[name][:]
    length = len(region)
    gc_content = round(region.gc, 3)
    n_masked = sum(1 for base in region.seq if base in "acgt")
    frac_masked = round(n_masked / length, 3)
    print(name, length, gc_content, frac_masked)

# ------------------------------------------------------------------------------------------
# Q6 (1.5 pts). Finding restriction sites with a while loop.
#   EcoRI cuts DNA at the site GAATTC.
#   a. Finish the find_motifs() function. It should return a list of every 0-based position
#      where motif starts in dna. Use the string .find() method inside a while loop.
#   b. Run it on chrom1 as written in the file. Print the number of sites and the first 5.
#   c. Run it again on the uppercase version of chrom1 (.upper()). Print the number of sites
#      and the first 5.
#   d. In a comment: why are the numbers different, and which one is correct?
# ------------------------------------------------------------------------------------------
print('\nQ6 Output(s):')


def find_motifs(dna, motif):
    positions = []
    start = 0
    pos = dna.find(motif, start)
    while pos != -1:
        positions.append(pos)
        start = pos + 1
        pos = dna.find(motif, start)
    return positions


# 6a. Uncomment the line below to test your function before using it on the genome
assert find_motifs('GGTTAAAGATCGGCGAGCCAATGGATCGACGATCA', 'GATC') == [7, 23, 30]

chrom1_seq = genome[chrom1][:].seq

sites = find_motifs(chrom1_seq, 'GAATTC')
print("Number of sites (as written):", len(sites))
print("First 5:", sites[:5])

sites_upper = find_motifs(chrom1_seq.upper(), 'GAATTC')
print("Number of sites (uppercase):", len(sites_upper))
print("First 5:", sites_upper[:5])

# d. Why are the numbers different? Which one is correct?
# .find() is case-sensitive, so the search on the sequence as written misses every
# GAATTC that sits in soft-masked (lowercase) sequence. Lowercase bases are still real
# DNA, so the uppercase count is the correct one.

# ------------------------------------------------------------------------------------------
# Q7 (2 pts). Finding sites with ambiguous bases using regex.
#   Some enzymes recognize sites with any base in the middle. BcgI (used for 2b-RAD in
#   Project 2) recognizes CGANNNNNNTGC, where N means any of A, C, G or T.
#   a. Finish find_motifs_regex(). Replace each N in the motif with the regex character class
#      [ACGT], then use re.finditer() to return a list of the 0-based start positions.
#   b. Run it on the UPPERCASE chrom1 sequence. Print the number of sites and the first 5.
#   c. BcgI's site is not a palindrome. On the other DNA strand it reads GCANNNNNNTCG (its
#      reverse complement). Search for that motif too. Print the number of sites, then print
#      the total number of BcgI sites on both strands.
# ------------------------------------------------------------------------------------------
print('\nQ7 Output(s):')


def find_motifs_regex(dna, motif):
    positions = []
    pattern = motif.replace('N', '[ACGT]')
    for match in re.finditer(pattern, dna):
        positions.append(match.start())
    return positions


# 7a. Uncomment the line below to test your function
assert find_motifs_regex('AACGATTTTTTTGCAA', 'CGANNNNNNTGC') == [2]

bcgi_fwd = find_motifs_regex(chrom1_seq.upper(), 'CGANNNNNNTGC')
print("Number of BcgI sites (CGANNNNNNTGC):", len(bcgi_fwd))
print("First 5:", bcgi_fwd[:5])

bcgi_rev = find_motifs_regex(chrom1_seq.upper(), 'GCANNNNNNTCG')
print("Number of BcgI sites (GCANNNNNNTCG):", len(bcgi_rev))
print("Total BcgI sites on both strands:", len(bcgi_fwd) + len(bcgi_rev))
