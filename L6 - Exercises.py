"""
Group Members: []

Lecture 6 Exercise (11 Points)

Due Date: TBD

Directions: This assignment has 3 parts to it. Add code below to each of the functions to accomplish the goals
of each section. You must use, edit, and submit this python script directly for this assignment.

This script gets ALL of its input from the command line using argparse -- there is no input() anywhere in this
script. Run it like this, filling in your own values for --path and --dna, and any number of integers for
--numbers (try it with 4 numbers, then try it again with 7 -- your Part III functions should work either way):

    python3 "L6 - Exercises.py" --path /Users/pmcgrath7/PythonClass/first_script.py --numbers 4 8 15 16 23 42 --dna ACCGGTATCG

Collaboration:
You are welcome to work with your team on this assignment.

Submission Details:
Please submit one script per team.
"""

import argparse
import statistics
import os


def parse_arguments():
    """
    Build an ArgumentParser with three REQUIRED arguments and return the parsed result:
      --path     a single file path (type=str)
      --numbers  one or more integers (type=int, nargs='+') -- this should work with any number of values
      --dna      a single DNA sequence (type=str)
    """
    # your code here
    parser = argparse.ArgumentParser(description= "The script will return a DNA sequence that has been modified by user input")
    parser.add_argument('--path', help = "what is the path to the file", required=True, type=str)
    parser.add_argument('--numbers', help = "takes an interger value", type=int, nargs='+')
    parser.add_argument('--dna', help = "a single DNA sequence", type=str)
    return parser.parse_args()

args = parse_arguments()
print(args.path)


print("Below is the output for part 1: ")  # leave this line to help the TA with grading

"""
Exercise_6 Part I (3 points; 1 per function)
Using the path you get from --path (e.g. /Users/pmcgrath7/PythonClass/first_script.py), write a function that
prints out just the name of the file (e.g. first_script.py), and a function that prints out the ABSOLUTE path
of the directory it is found in (e.g. /Users/pmcgrath7/PythonClass -- not just "PythonClass", and not a
relative path -- the full path starting from the root, the same way it was given to you in --path).
"""

# write a function to print out the filename of a given path
def print_filename(path):
    # your code here. You'll notice that "filename" is not yet defined in this function. You need to write code to define it. Comment out the below line for now when testing other parts of the script and remove the comment once filename is defined.
    filename = path.split('/')[-1]
    print('filename: {}'.format(filename))

# write a function to print out the absolute path of the directory containing a given file
def print_directory(path):
    # your code here. You'll notice that "directory" is not yet defined in this function. You need to write code to define it. Comment out the below line for now when testing other parts of the script and remove the comment once directory is defined.
    directory = path.split('/')[:-1]
    directory = '/'.join(directory)
    print('directory: {}'.format(directory))


# write a function combining the above two functions -- i.e., a function that takes a path and prints out both
# the filename and directory
def analyze_path(path):
    print_filename(path)
    print_directory(path)

analyze_path(args.path)


print("\nBelow is the output for part 2: ")  # leave this line to help the TA with grading

"""
Exercise_6 Part II (3 points; 1 per function)
Recall from lecture: functions can take positional parameters and parameters with default values, and when you
CALL a function you can pass arguments positionally or by name (keyword arguments).

Write check_DNA_sequence(DNA), which returns True if DNA contains only the letters A, C, G, and T
(case-insensitive), and False if it contains anything else.

Write reverse_complement(DNA, mode='reverse_complement'). mode is a parameter with a default value, and can be
set to 'reverse', 'complement', or 'reverse_complement':
    'reverse'            -- return DNA with the order of the bases reversed (no base substitution)
    'complement'         -- return DNA with each base swapped for its complement (A<->T, C<->G), same order
    'reverse_complement' -- (the default) do both: complement every base AND reverse the order

Write analyze_dna(DNA), which:
    1. Calls check_DNA_sequence(DNA). If DNA is not valid, print a message saying so and return -- do not call
       reverse_complement on invalid input.
    2. If DNA is valid, call reverse_complement three separate times on it, printing each result:
       once passing mode positionally, once passing mode by name (mode=...), and once passing BOTH DNA and mode
       by name (DNA=..., mode=...).
"""

def check_DNA_sequence(DNA):
    valid_bases = {"A", "C", "T", "G"}
    for nuc in DNA.upper():
        if nuc not in valid_bases:
            return False
    return True

def reverse_complement(DNA, mode='reverse_complement'):
    complement_dict = {'A':'T','T':'A', 'C':'G','G':'C'}
    sequence = DNA.upper()
    dna_string = ''

    if mode == "reverse":
        dna_string = sequence[::-1]

    elif mode == "complement":
        for nuc in sequence:
            dna_string = dna_string + complement_dict[nuc]

    elif mode == "reverse_complement":
        for nuc in sequence:
            dna_string = dna_string + complement_dict[nuc]
        dna_string = dna_string[::-1]  # reverse once, after the loop finishes

    print(dna_string)

def analyze_dna(DNA):
    if not check_DNA_sequence(DNA):
        print("Invalid DNA sequence")
        return
    reverse_complement(DNA)
    reverse_complement(DNA, mode='complement')
    reverse_complement(DNA, mode='reverse')

analyze_dna(args.dna)


print("\nBelow is the output for part 3: ")  # leave this line to help the TA with grading

"""
Exercise_6 Part III (5 points; 1 per function)
Using the list of integers you get from --numbers, print out the sum, mean, and median of the numbers.
This should be broken down into a series of smaller functions that all get called together at the end of this
section -- same general structure as Part I.

Remember --numbers can be given ANY number of values -- write these functions so they work for a list of any
length, not just however many you happen to test with. For mean and median, don't calculate these by hand --
"import statistics" at the top of this script and use statistics.mean() and statistics.median(). (statistics.median()
already handles the odd-vs-even-length cases for you.)
"""

def sort_and_print(input_list):
    sorted_num = sorted(input_list)
    print(sorted_num)
    # print out the sorted list as the output for this function.
    # Hint: think back to the shallow vs. deep copy lecture material -- list.sort() sorts a list IN PLACE (it
    # changes the original list, even outside this function!), while sorted(list) returns a brand new sorted
    # list and leaves the original alone. Either one is fine for full credit here, but pay attention to which
    # one you picked -- the check at the very bottom of this script will show you whether it affected the
    # original data or not.
    # your code here

def print_sum(input_list):
    # in general, you don't want to use a "built-in" name as a variable name. Built-in's include function names (like "sum") and types (like "float" or "list"). 
    # Since "sum" is a built-in, avoid trying to initiate a variable called "sum"
    # your code here
    print(sum(input_list))

def print_mean(input_list):
    # use statistics.mean() here -- don't calculate this by hand
    # your code here
    print(statistics.mean(input_list))

def print_median(input_list):
    # use statistics.median() here -- it handles the odd-length and even-length cases for you, so you don't
    # need to calculate this by hand
    # your code here
    print(statistics.median(input_list))
    

def print_stats(input_list):
    # Here, just collect all of the functions you wrote into a single function that runs them sequentially
    # your code here
    sort_and_print(input_list)
    print_sum(input_list)
    print_mean(input_list)
    print_median(input_list)


# finally, call print_stats() outside of the function definitions so that we actually get output when we run
# this script from the command line (analyze_path() and analyze_dna() were already called above, right after
# their own Part's functions were defined).
print_stats(args.numbers)
# One more check tied to the shallow-copy hint above: print the ORIGINAL --numbers list one final time here, so
# you (and we) can see whether your sort_and_print() function changed the order of the original data outside
# the function or not. Either result is fine -- now you'll know which you built.
print("original --numbers, after all Part III functions have run:")
print(args.numbers)