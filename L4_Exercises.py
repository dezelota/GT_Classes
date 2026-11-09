"""
Group Members: []

Week 4 Exercise (8 Points)

Due Date: Check the Assignments section in Canvas

Directions: To complete this assignment, run the command(s) on your terminal to complete each question.
Please use and edit this python script directly for this assignment.

Collaboration:
You are welcome to discuss this assignment with your TA or classmates, but each student must write and
submit their own script.

Submission Details:
Please submit your completed script individually.

Sources: At the end of the script, in a comment block like this one, please include a list of any links to any webpages (stackoverflow, github, geeksforgeeks etc.) used for help completing the assignment.

NOTE: Please leave all the print statements that say print(Q# Output: ). Do not edit these. These lines will be helpful to the TA for grading.
Add additional print statements after these lines if needed to answer the questions.
"""

# 1. Use a method of the string class to separate the genus and the species name into two different variables
# Do this in one line
# print the output to the terminal (this output will be used for grading)
print('Q1 Output: ')
organism = "Homo sapiens"
# [your code starts here]
first, second = organism.split(" ")
print(first, second)



# 2. The number of files to analyze is given by the variable below.
# Print out the number of files using the variable like so: “You would like to analyze 3 files” (this output will be used for grading)
print('Q2 Output: ')
num_files = 3
# [your code starts here]
print("You would like to analyze", num_files, "files")



# 3. Store your first name as a variable and your second name as a variable.
# Create a new variable from these called full_name that contains your first and last name separated by a space.
# print the outputs to the terminal (these outputs will be used for grading)
# Do this in two ways:
# a.	Using the string + operator
# b.	Using the join method of the list class
print('Q3 Outputs: ')
first_name = 'Desiree'
last_name = 'Bogen'
# [your code starts here]
full_name = first_name+" "+last_name
print(full_name)
full_name = " ".join([first_name, last_name])
print(full_name)


# 4. Given the DNA variable, create a list that contains the number of each nucleotide stored as an element.:
# Store the counts in order for [A, C, G, T]
# ex: DNA = "aaAcCggGGtttTT"
# desired_output: [3,2,4,5]
# a.	Do this however you can manage it using multiple lines if necessary
# b.	Do this in a single line using a list comprehension
# print the outputs to the terminal (these outputs will be used for grading)
print('Q4 Outputs: ')
DNA = "ACgttGTcgtTTgaCCGacACCGGTTAACCGGTACGGTAACAAGGTTTAGGTA"
# [your code starts here]
A = DNA.upper().count("A")
T = DNA.upper().count("T")
C = DNA.upper().count("C")
G = DNA.upper().count("G")
DNA_count_list = [A, C, G, T]
print(DNA_count_list)

print([DNA.upper().count(base) for base in ["A", "C", "G", "T"]])



#5.	Words is a list variable given below. You are given a second phrase (new_words) to add to that list (given as a string)
# Add the individual words in the new_words string to the words list in three ways
# Hint: the result you're looking for in a--> c is: ['I', 'love', 'Watership', 'Down.', 'It', 'is', 'a', 'book', 'about', 'rabbits.', 'I', 'like', 'this', 'book!']
#a. The + operator of list.
#b.	The append method of list
#c.	The extend method of list
#d. Convert your combined list (from part c) into a set and print how many unique words it contains.
#   Then, in a comment below your code, briefly answer: why might this number not equal len(words_c)?
# Be sure to print the outputs to the terminal (these outputs will be used for grading)
print('Q5 Outputs: ')
words = ['I','love','Watership','Down.']
new_words = 'It is a book about rabbits. I like this book!'
# [your code starts here]
new_words2 = new_words.split()

# a:
words_a = words + new_words2 # [replace with code to answer a]
print(words_a)

#b
words_b = words.copy() # [replace with code to answer b]
words_b.append(new_words2)
print(words_b)

#c
words_c = words.copy()  # [replace with code to answer c]
words_c.extend(new_words2)
print(words_c)

#d
set_d = set(words_c) # [replace with code to answer d]
print(set_d)
print("length of words_c:", len(words_c))
print("length of set_d:", len(set_d))
print("because sets only keep unique elements, and the word 'I' appears twice in words_c, so the duplicate collapses into a single entry in the set.")
# [Replace with your answer for "why might this number not equal len(words_c)"]



#6. A classic prank is to secretly change a friend's phone autocorrect settings so that certain words or
# characters get swapped for something else. Below is a sentence and a dictionary called replacements
# that maps two characters to what they should be "autocorrected" to.
#a.	Use the dictionary's values (accessed with the [] operator) along with the string's .replace() method
#	to create a new string called joke_sentence, where every comma in sentence is replaced with a period,
#	and every capital I is replaced with a lowercase i. Call .replace() twice (once per character), looking
#	up each replacement value from the dictionary rather than typing '.' or 'i' directly in your code.
# print the output to the terminal (this output will be used for grading)
print('Q6 Outputs: ')
sentence = "I think, Ian, that I am going, right now, to the lab, and I hope I remembered my goggles."
replacements = {',': '.', 'I': 'i'}
# [your code starts here]
joke_sentence = sentence.replace(",", replacements[","])
joke_sentence = joke_sentence.replace("I", replacements["I"])
print(joke_sentence)



#7. Convert the following list of numbers into a csv type line where each element is separated by a comma
# Do this using a combination of list comprehension and the join method
# print the output to the terminal (this output will be used for grading)
print('Q7 Outputs: ')
data = [2,5,2,1,43,234,12,1,4,1,6,7,8,3]
# [your code starts here]
data2 = ",".join([str(num) for num in data])
print(data2)

#8. Below is a real protein sequence (the A-chain of human insulin), written using the standard single-letter
# amino acid codes.
#a.	Determine how many unique amino acids are present in the sequence. Do this using a set and the len()
#	function -- you should not need a loop.
# print the output to the terminal (this output will be used for grading)
print('Q8 Outputs: ')
protein = "GIVEQCCTSICSLYQLENYCN"
# [your code starts here]
print(len(set(protein)))
