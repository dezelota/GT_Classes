import argparse
import pdb

parser = argparse.ArgumentParser(description= "The script will return a DNA sequence that has been modified by user input")

#define inputs user will need
parser.add_argument('SequenceName', help= "what is the name of the sequence")
parser.add_argument('DNASequence', help= "what is the DNA sequence (only ACTG allowed)", )
parser.add_argument('Mode', help= "how to modify the DNA sequence", choices= ['reverse', 'reverse_complement', 'complement'])
parser.add_argument("--lower", "-l", action="store_true", help="convert string to lowercase")

#parse what user input and check if this words?
user_data=parser.parse_args()

#need to make sure that the sequence is valid, if not raise error and print out a statement
for i in user_data.DNASequence:
    if i not in ["a", "c", "t", "g", "A", "C", "T", "G"]:
        print("DNA Sequence not valid")

#make complement dictionary to be reference for the modes
complement_dict = {'A':'T','T':'A', 'C':'G','G':'C'}
sequence = user_data.DNASequence
dna_string=''

if user_data.Mode == "reverse":
    dna_string = user_data.DNASequence[::-1]

elif user_data.Mode == "complement":
    for nuc in user_data.DNASequence:
        dna_string = dna_string + complement_dict[nuc]

elif user_data.Mode == "reverse_complement":
    for nuc in user_data.DNASequence:
        dna_string = dna_string + complement_dict[nuc]
        dna_string = dna_string[::-1]

#now we need to tell python what to do if the flag is provided
#here we are going to use conditionals.
#evals whether a statement is True or False
print('>' + user_data.SequenceName)
if user_data.lower == True:
    print(dna_string.lower())
else:
    print(dna_string.upper()) 

#python debugger. runs code until it hits this line then enters it into the debugger
#pdb.set_trace()
