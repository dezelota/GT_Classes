"""
Group Members: []

L9 - Genomics II: Reading VCF files with PyVCF (10 points)

Due Date: Check the Assignment section in Canvas

Directions:
Complete the questions below. Questions are worth 1 point each unless marked otherwise.
Edit this script directly and submit it. Run it from the terminal with your VCF file:
    python3 "L9 - Genomics2.py" small_file.vcf.gz
Do not delete the "Q# Output(s):" print statements. The TA uses them to find your answers.
The "PyVCF Cheat Sheet" slide from today's lecture has most of what you need.

Setup (one time): pip install PyVCF3     (you still write "import vcf")

Collaboration:
You are welcome to work with your team on this assignment.

Submission Details:
Please submit one script per team.
"""
import argparse
import pdb  # pdb.set_trace() lets you pause and explore a record with dir()
import vcf


# Q1: Use argparse to take in the path to a VCF file as a positional argument named VCFFile.
# Then open it with vcf.Reader and store the result in a variable called vcf_obj. (1 point)
# your code here
parser = argparse.ArgumentParser()
parser.add_argument('VCFFile')
args = parser.parse_args()

vcf_obj = vcf.Reader(filename=args.VCFFile)  # your code here

print("Q1 Output(s):")
print(vcf_obj)


# Q2: Print the name and length of every contig in the file, one per line, separated by a tab.
# Hint: vcf_obj.contigs is a dictionary. Its values have .id and .length attributes. (1 point)
print("Q2 Output(s):")
# your code here
for contig in vcf_obj.contigs.values():
    print(f"{contig.id}\t{contig.length}")


# Q3: Print how many samples are in the file, then print each sample name on its own line. (1 point)
print("Q3 Output(s):")
# your code here
print(len(vcf_obj.samples))
for sample_name in vcf_obj.samples:
    print(sample_name)


# Q4: Use next() to get the first record (variant) in the file and store it in a variable called record.
# Print its chromosome, position, reference allele, and alternate allele(s). (1 point)
record = next(vcf_obj)  # your code here

print("Q4 Output(s):")
# your code here
print(record.CHROM, record.POS, record.REF, record.ALT)


# Q5: For this first record, what type of variant is it (snp, indel, ...) and how many alleles
# does it have (the reference allele plus all alternate alleles)? (1 point)
# Hint: use dir(record) to find attributes that might help.
var_type = record.var_type  # your code here
num_alleles = len(record.alleles)  # your code here

print("Q5 Output(s):")
print(var_type)
print(num_alleles)


# Q6: How many samples have a genotype call (are not ./.) at this record? (1 point)
num_called = record.num_called  # your code here

print("Q6 Output(s):")
print(num_called)


# Q7: For the first two samples, print the read depth (DP) and genotype (GT) at this record. (1 point)
dp_1 = record.samples[0]['DP']  # your code here
dp_2 = record.samples[1]['DP']  # your code here
geno_1 = record.samples[0]['GT']  # your code here
geno_2 = record.samples[1]['GT']  # your code here

print("Q7 Output(s):")
print(dp_1, geno_1)
print(dp_2, geno_2)


# Q8: Write a function called check_record that takes in a record and returns True only if ALL
# of the following are true for the first two samples. Otherwise it returns False. (2 points)
#   1. The record is a SNP
#   2. Both samples were called (neither is ./.)
#   3. There are exactly two alleles (one reference and one alternate)
#   4. Both samples have at least 5 reads
#   5. One sample is homozygous reference and the other is homozygous alternate
# Hints:
#   - Genotypes can be written 1/1 or 1|1 (phased). call.gt_type handles both for you:
#     0 = homozygous reference, 1 = heterozygous, 2 = homozygous alternate, None = not called
#   - Sometimes DP is missing and comes back as None. Make sure that returns False instead of crashing.
def check_record(record):
    # your code here
    if not record.is_snp:
        return False
    if len(record.alleles) != 2:
        return False
    s1 = record.samples[0]
    s2 = record.samples[1]
    if not s1.called or not s2.called:
        return False
    dp1 = getattr(s1.data, 'DP', None)
    dp2 = getattr(s2.data, 'DP', None)
    if dp1 is None or dp2 is None:
        return False
    if dp1 < 5 or dp2 < 5:
        return False
    return {s1.gt_type, s2.gt_type} == {0, 2}

print("Q8 Output(s):")
print(check_record(record))


# Q9: Loop through EVERY record in the file and count how many pass check_record and how many fail.
# Print the result exactly like this:   Pass: 12  Fail: 340
# Hint: vcf_obj has already given you the first record (Q4), and a reader can only be looped through
# once. Open the file again with vcf.Reader so your count starts from the first record. (1 point)
passed = 0
failed = 0
# your code here
vcf_obj = vcf.Reader(filename=args.VCFFile)
for rec in vcf_obj:
    if check_record(rec):
        passed += 1
    else:
        failed += 1

print("Q9 Output(s):")
print(f"Pass: {passed}  Fail: {failed}")