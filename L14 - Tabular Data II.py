"""
Group Members: []

Exercise 14 - Analyzing Tabular Data II (14 points)

Due Date: Wednesday November 4th, 2026 @ 12:30pm

Directions:
Complete the questions below. Each question is worth 1 point. Edit this script directly and submit it.
Keep GproteinDb.html in the same folder as this script, then run it from the terminal:
    python3 "Exercise 14 - Tabular Data II.py"
Do not delete the "Q# Output(s):" print statements. The TA uses them to find your answers.
The two cheat sheet slides from today's lecture have most of what you need. Searching the pandas
documentation or the web is fine; using AI tools is not.

Collaboration:
You are welcome to work with your team on this assignment.

Submission Details:
Please submit one script per team, along with the tracker.csv file your script makes.
"""
import pandas as pd


# ==================================================================================================
# PART 1: A lab tracking table (5 points)
# ==================================================================================================
# Our lab films cichlid tanks and then runs several analyses on each recording. We keep track of
# which analyses are done in a table like the one on the "Tabular data is very common in biology"
# slide. In Part 1 you will build that table yourself, add new recordings, and update it as
# analyses finish.

# Q1: Build a DataFrame called tracker from scratch using the dictionary below. Use the
# project_ids list as the index. Print tracker. (1 point)
tracker_data = {'tankID': ['t001', 't002', 't003'],
                'NumVideos': [13, 13, 10],
                'Prep': [True, False, True],
                'Depth': [True, False, False],
                'Cluster': [True, False, False]}
project_ids = ['MC_939_t001_tr1', 'YH_123_t002_tr1', 'CV_567_t003_tr1']
tracker = pd.DataFrame(tracker_data, index = project_ids)  # your code here

print("Q1 Output(s):")
print(tracker)


# Q2: Two more tanks finished recording. Add them as new rows with .loc, then print tracker.shape.
# (1 point)
#   MCYHF1_004_t004_tr1: tank t004, 9 videos, Prep True,  Depth False, Cluster False
#   MCYHF1_535_t011_tr1: tank t011, 9 videos, Prep False, Depth False, Cluster False
# your code here

print("Q2 Output(s):")
# your code here
tracker.loc['MCYHF1_004_t004_tr1'] = ["t004", 9, True, False, False]
tracker.loc['MCYHF1_535_t011_tr1'] = ["t011", 9, False, False, False]
print(tracker.shape)

# Q3: Change individual cells with .loc. (1 point)
#   a. The Prep analysis just finished for YH_123_t002_tr1. Set its Prep value to True.
#   b. Tank t003 (CV_567_t003_tr1) recorded 2 more videos. Add 2 to its NumVideos using +=.
# Print those two rows.
# your code here

print("Q3 Output(s):")
# your code here
tracker.loc['YH_123_t002_tr1', 'Prep'] = True
tracker.loc['CV_567_t003_tr1', 'NumVideos'] +=2
print(tracker.loc[['YH_123_t002_tr1', 'CV_567_t003_tr1']])

# Q4: Write a function called run_analysis(df, projectID, analysis_type) that marks an analysis as
# done. It should do these steps in order: (1 point)
#   1. If analysis_type is not 'Prep', 'Depth', or 'Cluster' (spelled exactly like that), raise a
#      ValueError with a message that lists the allowed values.
#   2. If that analysis is already True for projectID, print a specific message, for example:
#      "The Depth analysis was already run for MC_939_t001_tr1"
#   3. Otherwise, change that cell from False to True.
#   4. Return the row for projectID.
# Hint: change df directly with df.loc[projectID, analysis_type] = True
def run_analysis(df, projectID, analysis_type):
    # your code here
    if analysis_type not in ['Prep', 'Depth', 'Cluster']:
        raise ValueError("Allowed values: Prep, Depth, Cluster")
    if df.loc[projectID, analysis_type] == True:
        print(f"The {analysis_type} was already run for: {projectID} ")
    else:
        df.loc[projectID, analysis_type] = True
    return(df.loc[projectID])

# Do not change these tests.
print("Q4 Output(s):")
print(run_analysis(tracker, 'MCYHF1_535_t011_tr1', 'Depth'))  # Depth changes from False to True
print(run_analysis(tracker, 'MC_939_t001_tr1', 'Cluster'))    # already True, so your message prints
try:
    run_analysis(tracker, 'MCYHF1_004_t004_tr1', 'depthh')   # misspelled, so a ValueError is raised
    print("No error was raised")
except ValueError as error:
    print("ValueError raised:", error)


# Q5: Use .str and save the table. (1 point)
#   a. The letters before the first '_' in each projectID name the fish lineage (MC, YH, CV, MCYHF1).
#      Make a new column called Lineage from the index. The index has a .str too.
#      Hint: .str.split('_') splits each name into a list, and .str[0] then takes the first item.
#   b. Print how many recordings come from each lineage with .value_counts().
#   c. Save tracker to a file called tracker.csv with .to_csv(). Keep the index (it holds the projectIDs).
# your code here

print("Q5 Output(s):")
# your code here
tracker["Lineage"] = tracker.index.str.split('_').str[0]
print(tracker["Lineage"].value_counts())
tracker.to_csv('tracker.csv', index = True)

# ==================================================================================================
# PART 2: G protein structures (9 points)
# ==================================================================================================
# G proteins relay signals from G protein-coupled receptors (GPCRs) on the cell surface, which often
# leads to important downstream effects like changes in gene expression. GproteinDb
# (https://gproteindb.org/structure/g_protein_structure_browser) lists every solved 3D structure of a
# G protein. GproteinDb.html is a copy of that page saved from a web browser, so everyone works from
# the same data. pd.read_html() reads a saved .html file the same way it reads a web address.
#
# pd.read_html() needs the lxml package. If you get an error about lxml, run: pip install lxml
# (or: conda install lxml)
#
# Open GproteinDb.html in your web browser to see what the table looks like. You'll find that the
# column names are messy once pandas reads them, so first we clean them, then we analyze the data.

# Q6: Read GproteinDb.html with pd.read_html() and store the result in all_tables. read_html returns
# a LIST with one DataFrame for each table on the page. Print how many tables it found. Then store
# the G protein table (the one with data in it) in df and print df.shape. (1 point)
all_tables = pd.read_html('https://gproteindb.org/structure/g_protein_structure_browser')  # your code here
print(len(all_tables))
#print(all_tables[0])
#print(all_tables[1])
df = all_tables[0]  # your code here
print(df.shape)
print("Q6 Output(s):")
# your code here


# Q7: Delete the first and last columns of df. (1 point)
# The first column comes from the check boxes on the website, so it is all NaN. The last column has no
# name on the website and holds the site's own ID numbers, which we don't need.
# Hint: .iloc[] can select every row and all columns except the first and last.
# Print df.shape.
# your code here

print("Q7 Output(s):")
df = df.iloc[:, 1:-1]
print(df.shape)


# Q8: Fix the column names. (1 point)
# The website has two rows of headers (for example "G PROTEIN" above "Fam."), so pandas made each
# column name a tuple: df.columns[0] is ('G PROTEIN', 'Fam.').
# Join the two parts of each name with an underscore, so the first column is named 'G PROTEIN_Fam.',
# and assign the new names to df.columns. Print the first 5 column names.
# Hint: '_'.join(('a', 'b')) gives 'a_b'. A list comprehension can do this for every column.
# your code here

print("Q8 Output(s):")
df.columns = ["_".join(cols) for cols in df.columns]
print(df.columns[:5].tolist())


# Q9: Remove the first row. (1 point)
# Under the column names, the website has a row of search boxes for filtering. pandas reads it as a
# row that is all NaN, with the index label 0. Remove it with df.drop(). Print df.shape.
# (FYI: read_html can also skip it when reading. Look up its skiprows option. For this question, use
# df.drop() so everyone's Q6 shape matches.)
# your code here

print("Q9 Output(s):")
df = df.drop([0], axis=0)
print(df.shape)


# Q10: Clean up the column names. (1 point)
# Some names contain two spaces and an "×" from the website's close buttons, e.g. 'STRUCTURE  ×_Method'.
# Note: "×" is a multiplication sign, not the letter x. Copy it from this comment.
# Use df.columns.str.replace() to remove the two spaces and the × so that, for example,
# 'STRUCTURE  ×_Method' becomes 'STRUCTURE_Method'. Print the full list of column names.
# your code here

print("Q10 Output(s):")
df.columns = df.columns.str.replace('  x'), ''
print(df.columns.tolist())


# Q11: Remove rows with no receptor. (1 point)
# Some structures have no receptor. On the website these show '-' in the receptor columns.
# Keep only the rows where 'RECEPTOR_Receptor family' is not '-'. Print df.shape.
# your code here
df = df[df['RECEPTOR_Receptor family'] != '-']

print("Q11 Output(s):")
print(df.shape)


# Q12: How many structures are there for each receptor family? (1 point)
# Use groupby on 'RECEPTOR_Receptor family' and count the rows in each group.
# Print the 5 families with the most structures (largest first).
# Hint: .sort_values(ascending=False) sorts a Series from largest to smallest.
#
# One way to think about groupby: picture sorting a deck of cards by suit. You end up with four piles
# (clubs, diamonds, hearts, spades). Then you can ask questions about each pile: how many cards are in
# it, what is the sum of the numbered cards, and so on.
family_counts = df.groupby('RECEPTOR_Receptor family').size().sort_values(ascending=False)  # your code here

print("Q12 Output(s):")
# your code here


# Q13: Which G protein family ('G PROTEIN_Fam.') has the most structures? (1 point)
# Print the name of that family, then print how many structures it has as an int.
# your code here

print("Q13 Output(s):")
# your code here
gprotein_counts = df.groupby('G PROTEIN_Fam.').size().sort_values(ascending=False)
print(gprotein_counts.index[0])
print(int(gprotein_counts.iloc[0]))

# Q14: For each structure method ('STRUCTURE_Method'), what are the mean resolution
# ('STRUCTURE_Resolution') and the number of structures? Use groupby with .agg(). Print the result.
# (1 point)
# (Resolution is in angstroms; a smaller number means a sharper structure.)
method_summary = df.groupby('STRUCTURE_Method')['STRUCTURE_Resolution'].agg(['mean', 'count'])  # your code here

print("Q14 Output(s):")
print(method_summary)
