"""
Group Members: [Desiree Bogen, Ashley Bolen, Nathan Solomon]

Exercise 15 - Joining Tables: COVID-19 Deaths by Country (15 points)

Due Date: Monday November 9th, 2026 @ 12:30pm

Directions:
Complete the questions below. Questions are worth 1 point each unless marked otherwise.
Edit this script directly and submit it.
Keep WorldDemographics.csv in the same folder as this script, then run it from the terminal:
    python3 "Exercise 15 - Joining Tables.py"
Do not delete the "Q# Output(s):" print statements. The TA uses them to find your answers.
Some questions ask you to look up something we did not cover in class. Searching the pandas
documentation or the web is fine; using AI tools is not.

Collaboration:
You are welcome to work with your team on this assignment.

Submission Details:
Please submit one script per team.
"""
# In this exercise you will estimate what would have happened if COVID-19 had spread with no
# protective measures. Assume everyone in the world was infected with the original strain of
# COVID-19 and no one had a vaccine. You will figure out:
#   1. How many people would die in each country?
#   2. What percentage of each country's population would die?
#   3. Which 5 countries would lose the highest percentage of their population, and which 5 the lowest?
#   4. What is the average age of the world's population before COVID, and after?
#
# To do this you need two tables:
#   - The infection-fatality ratio (IFR) for every age: the percent of infected people of that age who
#     die. This comes from Table 1 of COVID-19 Forecasting Team, Lancet 2022,
#     "Variation in the COVID-19 infection-fatality ratio by age, time, and geography during the
#     pre-vaccine era" (https://pmc.ncbi.nlm.nih.gov/articles/PMC8871594/).
#   - WorldDemographics.csv, which has the number of people alive at every age in every country.
# Then you will JOIN (merge) the two tables on Age.

import pandas as pd

# The rows of Table 1, copied exactly as they are printed in the paper. Each inner list is one row:
# [age, IFR with its 95% uncertainty interval].
ifr_rows = [
    ['1 year', '0·0054% (0·0021–0·0114)'],
    ['2 years', '0·0040% (0·0020–0·0070)'],
    ['3 years', '0·0032% (0·0019–0·0051)'],
    ['4 years', '0·0027% (0·0018–0·0043)'],
    ['5 years', '0·0024% (0·0017–0·0039)'],
    ['6 years', '0·0023% (0·0016–0·0038)'],
    ['7 years', '0·0023% (0·0015–0·0039)'],
    ['8 years', '0·0023% (0·0015–0·0042)'],
    ['9 years', '0·0025% (0·0016–0·0046)'],
    ['10 years', '0·0028% (0·0018–0·0050)'],
    ['11 years', '0·0031% (0·0021–0·0056)'],
    ['12 years', '0·0036% (0·0024–0·0063)'],
    ['13 years', '0·0042% (0·0028–0·0073)'],
    ['14 years', '0·0050% (0·0034–0·0084)'],
    ['15 years', '0·0060% (0·0041–0·0097)'],
    ['16 years', '0·0071% (0·0050–0·0113)'],
    ['17 years', '0·0085% (0·0060–0·0134)'],
    ['18 years', '0·0100% (0·0071–0·0157)'],
    ['19 years', '0·0118% (0·0084–0·0183)'],
    ['20 years', '0·0138% (0·0098–0·0214)'],
    ['21 years', '0·0162% (0·0114–0·0250)'],
    ['22 years', '0·0188% (0·0133–0·0292)'],
    ['23 years', '0·0219% (0·0153–0·0335)'],
    ['24 years', '0·0254% (0·0178–0·0385)'],
    ['25 years', '0·0293% (0·0207–0·0441)'],
    ['26 years', '0·0337% (0·0241–0·0504)'],
    ['27 years', '0·0386% (0·0280–0·0575)'],
    ['28 years', '0·0442% (0·0324–0·0658)'],
    ['29 years', '0·0504% (0·0372–0·0757)'],
    ['30 years', '0·0573% (0·0418–0·0870)'],
    ['31 years', '0·0650% (0·0469–0·0983)'],
    ['32 years', '0·0735% (0·0526–0·1108)'],
    ['33 years', '0·0829% (0·0590–0·1246)'],
    ['34 years', '0·0932% (0·0663–0·1398)'],
    ['35 years', '0·1046% (0·0747–0·1564)'],
    ['36 years', '0·1171% (0·0842–0·1746)'],
    ['37 years', '0·1307% (0·0950–0·1944)'],
    ['38 years', '0·1455% (0·1070–0·2161)'],
    ['39 years', '0·1616% (0·1197–0·2420)'],
    ['40 years', '0·1789% (0·1319–0·2706)'],
    ['41 years', '0·1976% (0·1440–0·3038)'],
    ['42 years', '0·2177% (0·1575–0·3397)'],
    ['43 years', '0·2391% (0·1714–0·3731)'],
    ['44 years', '0·2620% (0·1861–0·4122)'],
    ['45 years', '0·2863% (0·2016–0·4540)'],
    ['46 years', '0·3119% (0·2176–0·4980)'],
    ['47 years', '0·3389% (0·2350–0·5437)'],
    ['48 years', '0·3672% (0·2541–0·5906)'],
    ['49 years', '0·3968% (0·2748–0·6380)'],
    ['50 years', '0·4278% (0·2958–0·6858)'],
    ['51 years', '0·4606% (0·3180–0·7346)'],
    ['52 years', '0·4958% (0·3430–0·7855)'],
    ['53 years', '0·5342% (0·3720–0·8398)'],
    ['54 years', '0·5766% (0·4028–0·8992)'],
    ['55 years', '0·6242% (0·4358–0·9715)'],
    ['56 years', '0·6785% (0·4736–1·0602)'],
    ['57 years', '0·7413% (0·5181–1·1621)'],
    ['58 years', '0·8149% (0·5698–1·2796)'],
    ['59 years', '0·9022% (0·6304–1·4162)'],
    ['60 years', '1·0035% (0·7002–1·5727)'],
    ['61 years', '1·1162% (0·7776–1·7462)'],
    ['62 years', '1·2413% (0·8635–1·9438)'],
    ['63 years', '1·3803% (0·9588–2·1644)'],
    ['64 years', '1·5346% (1·0645–2·4094)'],
    ['65 years', '1·7058% (1·1817–2·6813)'],
    ['66 years', '1·8957% (1·3117–2·9830)'],
    ['67 years', '2·1064% (1·4557–3·3175)'],
    ['68 years', '2·3399% (1·6154–3·6881)'],
    ['69 years', '2·5986% (1·7928–4·0983)'],
    ['70 years', '2·8851% (1·9893–4·5519)'],
    ['71 years', '3·2022% (2·2069–5·0532)'],
    ['72 years', '3·5527% (2·4476–5·6064)'],
    ['73 years', '3·9402% (2·7139–6·2162)'],
    ['74 years', '4·3679% (3·0083–6·8875)'],
    ['75 years', '4·8397% (3·3336–7·6254)'],
    ['76 years', '5·3597% (3·6926–8·4353)'],
    ['77 years', '5·9320% (4·0887–9·3240)'],
    ['78 years', '6·5612% (4·5253–10·2959)'],
    ['79 years', '7·2520% (5·0061–11·3392)'],
    ['80 years', '8·0093% (5·5339–12·4411)'],
    ['81 years', '8·8381% (6·1140–13·6344)'],
    ['82 years', '9·7437% (6·7643–14·9249)'],
    ['83 years', '10·7311% (7·4783–16·3145)'],
    ['84 years', '11·8054% (8·2609–17·8063)'],
    ['85 years', '12·9717% (9·1175–19·4030)'],
    ['86 years', '14·2346% (10·0530–21·1061)'],
    ['87 years', '15·5984% (11·0729–22·9162)'],
    ['88 years', '17·0669% (12·1823–24·8326)'],
    ['89 years', '18·6431% (13·3860–26·8535)'],
    ['90 years', '20·3292% (14·6888–28·9754)'],
    ['91 years', '22·1263% (16·0949–31·1935)'],
    ['92 years', '24·0344% (17·6000–33·5013)'],
    ['93 years', '26·0519% (19·1384–35·8908)'],
    ['94 years', '28·1760% (20·7725–38·3524)'],
    ['95 years', '30·4021% (22·4676–40·8752)'],
    ['96 years', '32·7239% (24·2367–43·4272)'],
    ['97 years', '35·1335% (26·0981–46·0137)'],
    ['98 years', '37·6213% (28·0497–48·6219)'],
    ['99 years', '40·1762% (30·0877–51·2376)'],
    ['100 years', '42·7856% (32·2380–53·8466)'],
]


# Q1: Build a DataFrame called df from scratch using ifr_rows (a list of lists, one inner list per row).
# Do not give it column names yet. Print the first 5 rows with .head(). (1 point)
df = pd.DataFrame(ifr_rows)  # your code here

print("Q1 Output(s):")
print(df.head())


# Q2: Rename the columns. (1 point)
# With no names given, pandas named the columns 0 and 1. Use df.rename() to name them "Age" and "IFR".
# We did not cover .rename() in class. Look up how its columns= option works.
# Print df.columns.
# your code here
df.rename(columns={0: "Age", 1: "IFR"}, inplace=True)
print("Q2 Output(s):")
print(df.columns)


# Q3: Reformat the data so we can use it. (6 points: 1 for each part)
# Right now both columns hold text, and the text has extra pieces we don't want.

# Q3.1: Remove " years" and " year" from the Age column, so '1 year' becomes '1' and '2 years' becomes '2'.
# Hint: use .str.replace() on the column. Think about which one to remove first.
# your code here
df['Age'] = df["Age"].str.replace(" years", "")
df['Age'] = df["Age"].str.replace(" year", "")
print("Q3.1 Output(s):")
print(df.head())

# Q3.2: Keep only the IFR value: everything before the '%'. For example
# '0·0054% (0·0021–0·0114)' becomes '0·0054'.
# Hint: .str.split('%') splits each string into a list, and .str[0] takes the first item.
# your code here
df["IFR"] = df["IFR"].str.split('%').str[0]
print("Q3.2 Output(s):")
print(df.head())

# Q3.3: The "decimal point" in the IFR values is actually a middle dot (·), not a period (.).
# Python can't turn '0·0054' into a number, so replace the middle dot with a period.
# Don't copy and paste the middle dot from this file. Instead, get it out of the data with indexing:
# store it in a variable called middle_dot, then use .str.replace().
# Hint: df.loc[0, 'IFR'] is the string '0·0054'. Which position holds the middle dot?
middle_dot = df.loc[0, 'IFR'][1]  # your code here

# your code here
df['IFR'] = df['IFR'].str.replace(middle_dot, ".")

print("Q3.3 Output(s):")
print(df.head())

# Q3.4: WorldDemographics.csv has people of age 0, but the IFR table starts at age 1. Add a row at the
# end for age 0 with the same IFR as age 1 (0.0054). Both columns still hold strings, so the new
# values should be strings too. Print the last 5 rows with .tail().
# Hint: df.loc[len(df)] = [...] adds a row with the next unused index number.
# your code here
df.loc[len(df)] = {'Age': "0", 'IFR': "0.0054"}
print("Q3.4 Output(s):")
print(df.tail())

# Q3.5: Convert the Age column to int and the IFR column to float.
# Look up the .astype() method. Print df.dtypes.
# your code here

df['Age'] = df['Age'].astype(int)
df['IFR'] = df['IFR'].astype(float)

print("Q3.5 Output(s):")
print(df.dtypes)

# Q3.6: The IFR values are percents. Convert them to fractions (divide by 100), so 0.0054% becomes
# 0.000054. Print the rows for ages 0, 50 and 100.
# Hint: Age is a column, not the index, so filter with df['Age'].isin([0, 50, 100]).
# your code here
df['IFR'] = df['IFR']/100

print("Q3.6 Output(s):")
# your code here
print(df[df['Age'].isin([0, 50, 100])])

# Q4: Read WorldDemographics.csv into a DataFrame called df2. Use its first column as the index.
# Print df2.shape. (1 point)
df2 = pd.read_csv('WorldDemographics.csv', index_col=0)  # your code here

print("Q4 Output(s):")
print(df2.shape)


# Q5: Join the two tables on Age with pd.merge(), so every row of df2 gets the IFR for its age.
# Store the result in df_merged and print df_merged.shape. (1 point)
# Think about it: df2 has every age (0-100) for every country, and df now has every age once.
# How many rows should df_merged have?
df_merged = pd.merge(left=df2, right=df, on="Age")  # your code here

print("Q5 Output(s):")
print(df_merged.shape)


# Q6: Add a column called 'Deaths' to df_merged: the expected number of deaths at that age in that
# country (number alive times IFR). Print the first 5 rows. (1 point)
# your code here
df_merged["Deaths"] = df_merged['#Alive']*df_merged['IFR']
print("Q6 Output(s):")
print(df_merged.head())


# Q7: Make a new DataFrame called df_population_stats with one row per country (PopulationID) that has
# each country's total population ('#Alive') and total expected deaths ('Deaths'). (1 point)
# Hint: groupby, then .agg() with a dictionary.
# Print the first 5 rows.
df_population_stats = df_merged.groupby('PopulationID').agg({'#Alive': 'sum', 'Deaths': 'sum'})  # your code here

print("Q7 Output(s):")
print(df_population_stats.head())


# Q8: Add a column called '% Deaths' to df_population_stats: the percent of each country's population
# that would die. Print the first 5 rows. (1 point)
# your code here
df_population_stats['% Deaths'] = df_population_stats['Deaths'] / df_population_stats['#Alive']
print("Q8 Output(s):")
print(df_population_stats.head())


# Q9: Which 5 countries would lose the HIGHEST percent of their population, and which 5 the LOWEST?
# Sort df_population_stats by '% Deaths', then print the 5 highest and the 5 lowest. (1 point)
# your code here
df_population_stats = df_population_stats.sort_values('% Deaths', ascending=False)
print("Q9 Output(s):")
# your code here
print(df_population_stats.head(5))
print(df_population_stats.tail(5))

# Q10: What is the average age of the world's population before COVID, and after? (1 point)
# The average age is (each age times the number of people of that age, all added up) divided by the
# total number of people. Use df_merged, which has every age in every country.
#   - Before: use '#Alive' as the number of people.
#   - After: the number of people left is '#Alive' minus 'Deaths'.
# Print both averages, rounded to 2 decimal places.
age_before = round((df_merged['Age'] * df_merged['#Alive']).sum() / df_merged['#Alive'].sum(), 2)  # your code here
age_after = round((df_merged['Age'] * (df_merged['#Alive'] - df_merged['Deaths'])).sum() / (df_merged['#Alive'] - df_merged['Deaths']).sum(), 2)  # your code here

print("Q10 Output(s):")
print(age_before)
print(age_after)
