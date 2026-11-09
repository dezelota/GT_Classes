"""
Group Members: []

Exercise 13 - Analyzing Tabular Data with pandas (11 points)

Due Date: Monday November 2nd, 2026 @ 12:30pm

Directions:
Complete the questions below. Each question is worth 1 point. Edit this script directly and submit it.
Keep penguins.tsv in the same folder as this script, then run it from the terminal:
    python3 "Exercise 13 - Tabular Data.py"
Do not delete the "Q# Output(s):" print statements. The TA uses them to find your answers.
Some questions ask you to look up something we did not cover in class. Searching the pandas
documentation or the web is fine; using AI tools is not.

Collaboration:
You are welcome to work with your team on this assignment.

Submission Details:
Please submit one script per team. Include the two .txt files your script makes
(species_island.txt and adelie_flipper_lengths.txt).
"""
import pandas as pd

# The data: measurements of 344 penguins from three islands in Antarctica (the Palmer Penguins dataset).
# Each row is one penguin. The first column, observation_ID, has a name for each row (obs_1, obs_2, ...).
file_path = 'penguins.tsv'


# Q1: Load the file into a pandas DataFrame called df. (1 point)
# - The file is tab-delimited (.tsv), not comma-delimited. Find the read_csv() option that sets the delimiter.
# - Use the first column (observation_ID) as the index.
df = pd.read_csv(file_path, sep='\t', index_col=0)  # your code here

print("Q1 Output(s):")
print(type(df))


# Q2: Print the first 7 rows of df. (1 point)
# We did not cover this in class. Look up how to show the first few rows of a DataFrame.
print("Q2 Output(s):")
# your code here
print(df.head(7))


# Q3: Print the number of rows and columns in df. (1 point)
# This was also not covered in class. Look up the DataFrame attribute that gives its shape.
print("Q3 Output(s):")
# your code here
print(df.shape)


# Q4: Write the species and island of every penguin to a file called species_island.txt,
# one penguin per line, formatted exactly like this:
#     Species: Adelie, Island: Torgersen
# (1 point)
# your code here
with open('species_island.txt', 'w') as f:
    for species, island in zip(df['species'], df['island']):
        f.write('Species: ' + species + ', Island: ' + island + '\n')

print("Q4 Output(s):")
print("Output saved to species_island.txt")


# Q5: Make a list of the flipper lengths of all Adelie penguins and write it to a file called
# adelie_flipper_lengths.txt, one value per line. Do this without iterrows(). (1 point)
# Hints:
# - First make a new DataFrame with only the Adelie penguins (see the "Filtering data by values" slides).
# - Then take its flipper_length_mm column.
# - One Adelie penguin has no measurements. Remove the missing value with a built-in pandas method.
# - A column (Series) has a method that turns it into a regular Python list.
# Print how many values are in your list.
adelie_df = df[df['species'] == 'Adelie']
adelie_flipper_lengths = adelie_df['flipper_length_mm'].dropna().tolist()  # your code here

with open('adelie_flipper_lengths.txt', 'w') as f:
    for length in adelie_flipper_lengths:
        f.write(str(length) + '\n')

print("Q5 Output(s):")
print(len(adelie_flipper_lengths))
print("Output saved to adelie_flipper_lengths.txt")


# .iloc[] vs .loc[]
# .iloc[] picks rows and columns by POSITION, counting from 0, like a list.
#       df.iloc[0, 0] is the first row, first column. Slices leave out the end: df.iloc[0:3] gives rows 0, 1, 2.
# .loc[] picks rows and columns by NAME (the index label and the column name).
#       df.loc['obs_1', 'species']. Slices INCLUDE the end: df.loc['obs_1':'obs_3'] gives 3 rows.
# Note: the index (observation_ID) is not counted as a column, so column position 0 is 'species'.


# Q6: Use .iloc[] to get the value in the 5th row and 3rd column (row position 4, column position 2).
# Print it. (1 point)
value_q6 = df.iloc[4, 2]  # your code here

print("Q6 Output(s):")
print(value_q6)


# Q7: Use .iloc[] to get the 11th row (row position 10). Print it, then print its type. (1 point)
series_q7 = df.iloc[10]  # your code here

print("Q7 Output(s):")
print(series_q7)
print(type(series_q7))


# Q8: Use .iloc[] to get row positions 20 through 29 and column positions 1 through 4 (both ranges
# include their last number). Print it, then print its type. (1 point)
subset_df_q8 = df.iloc[20:30, 1:5]  # your code here

print("Q8 Output(s):")
print(subset_df_q8)
print(type(subset_df_q8))


# Q9: Use .loc[] to get the species of the penguin named 'obs_1'. Print it, then print its type. (1 point)
value_q9 = df.loc['obs_1', 'species']  # your code here

print("Q9 Output(s):")
print(value_q9)
print(type(value_q9))


# Q10: Use .loc[] to get the whole body_mass_g column. Print the first 5 values with .head(),
# then print its type. (1 point)
series_q10 = df.loc[:, 'body_mass_g']  # your code here

print("Q10 Output(s):")
# your code here
print(series_q10.head())
print(type(series_q10))


# Q11: Use .loc[] to get the penguins named 'obs_5' through 'obs_10' (including both), and only the
# species, island, and sex columns. Print it, then print its type. (1 point)
subset_df_q11 = df.loc['obs_5':'obs_10', ['species', 'island', 'sex']]  # your code here

print("Q11 Output(s):")
print(subset_df_q11)
print(type(subset_df_q11))
