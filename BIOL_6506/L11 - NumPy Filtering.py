"""
Group Members: []

Exercise 11 - NumPy Filtering and Axes (11 points)

Due: Monday, October 26, 2026 @ 12:30pm

Directions:
Complete the questions below. Edit this python script directly and submit it.
Put daily_depths.npy in the same folder as this script, then run it from the terminal:
    python "Exercise 11 - NumPy Filtering.py"
Print each answer under its "Q# Output(s):" line so the TA can find it.
If numpy and axes are confusing, read "How do axes work in numpy?" at the bottom of this script first.

Collaboration / Submission:
You are welcome to work with your team on this assignment. Please submit one script per team.
"""
# In this exercise you will keep working with daily_depths.npy, the bower-building depth data from Exercise 10.
# Reminder: the array has one 2D depth image per day. Each value is the distance from the depth sensor (above the
# tank) down to the sand surface, in cm. A bigger value means the sand is farther away (lower).
# You will change the data in the array and look at the results with save_array_visualization().

import numpy as np
import matplotlib
matplotlib.use('Agg')  # save figures to files without opening a window
import matplotlib.pyplot as plt


def save_array_visualization(array, filename, vmin=-5, vmax=5):  # (0 points) GIVEN - do not change
    # Saves a picture of a 2D numpy array. Give it the array and a filename.
    # vmin and vmax set the range of the color scale: values at or below vmin are dark purple, values at or above
    # vmax are yellow. NaN values are not drawn, so they show up white.
    if not filename.endswith('.jpg'):
        filename = filename + '.jpg'
    plt.figure()
    plt.imshow(array, cmap='viridis', vmin=vmin, vmax=vmax)
    plt.colorbar()
    plt.savefig(filename, format='jpg')
    plt.close()


# Q1: Loading the array (1 point)
#   Load "daily_depths.npy" into a variable called data. Print its shape. How many days and how many pixels per
#   image are there?
print('Q1 Output(s):')
### Your Code Here ###
data = np.load('daily_depths.npy')  # replace None
print(f"The shape of data is:\n {data.shape}")
print(f"There are {data.shape[0]} days and {data.shape[1]} x {data.shape[2]} pixels per image.")
print("-" * 50)


# Q2: Minimum and maximum of each day using axis (1 point)
#   Find the minimum and maximum depth for each day (one value per day), ignoring NaNs.
#   Hint: if you want one value per day, what shape should your answer have? Which axes do you need to collapse?
#   You can collapse more than one axis at once with a tuple, e.g. axis=(1, 2).
print('Q2 Output(s):')
### Your Code Here ###
mins = np.nanmin(data, axis=(1, 2))  # replace None
maxs = np.nanmax(data, axis=(1, 2))  # replace None
print(f"The min depth value for each day is:\n {mins}")
print(f"The max depth value for each day is:\n {maxs}")
print("-" * 50)


# Q3: Which pixels have missing data? (1 point)
#   For each pixel, count how many days it is NaN. The result should be one 2D image (same shape as one day).
#   This can be done with one line of numpy code.
#   Save it with save_array_visualization() as "Q3_Nans.jpg". Use vmin=0 and vmax set to the number of days, so the
#   color scale runs from "never missing" to "always missing".
#   Print the largest count, and how many pixels are missing on EVERY day.
#   You will be graded on Q3_Nans.jpg and the two numbers.
print('Q3 Output(s):')
### Your Code Here ###
nan_counts = np.isnan(data).sum(axis=0)  # replace None
save_array_visualization(nan_counts, "Q3_Nans.jpg", vmin=0, vmax=data.shape[0])
print(f"The most days any pixel is missing:\n {nan_counts.max()}")
print(f"Pixels missing on every day:\n {(nan_counts == data.shape[0]).sum()}")
print("-" * 50)


# Q4: Standard deviation of each pixel over time (1 point)
#   Like Q3, make one 2D image: the standard deviation of each pixel across all days, ignoring NaNs.
#   Save it as "Q4_Stds.jpg" with vmin=0 and vmax=3.
#   (numpy may print a "Degrees of freedom" RuntimeWarning for pixels that are NaN on every day. That is OK.)
#   In a print statement: where in the tank is the standard deviation highest, and why?
print('Q4 Output(s):')
### Your Code Here ###
stds = np.nanstd(data, axis=0)  # replace None
save_array_visualization(stds, "Q4_Stds.jpg", vmin=0, vmax=3)
print("The standard deviation is highes where the fish moved sand (the bower area), because the depth there changed from day to day while the rest of the tank stayed pretty constant.")
print("-" * 50)


# Q5: Change since the first day (1 point)
#   Make a new 3D array called change_from_first. For each day, it holds that day's depth minus the first day's depth.
#   You can use a list comprehension or a for loop, then turn the list into an array with np.array(your_list).
#   (numpy can also do this in one step: data - data[0]. Try it and check you get the same answer!)
#   change_from_first must have the same shape as data.
print('Q5 Output(s):')
### Your Code Here ###
change_from_first = np.array([day - data[0] for day in data])  # replace None
print(f"The shape of change_from_first is:\n {change_from_first.shape}")  # uncomment once you have made it
print("-" * 50)


# Q6: Thresholding with Boolean masks (1 point)
#   Make a copy of change_from_first called thresh (done for you). Then change its values:
#     where change_from_first > 1   (sand dug out by more than 1 cm)   -> 1
#     where change_from_first < -1  (sand piled up by more than 1 cm)  -> -1
#     where change_from_first is between -1 and 1                       -> 0
#     NaN values stay NaN
#   Hint: make all three masks from change_from_first (not from thresh), before you change anything.
#   Save the LAST day of thresh as "Q6_Thresh.jpg" with vmin=-1 and vmax=1.
#   Print how many pixels on the last day are 1, -1, and 0.
print('Q6 Output(s):')
thresh = np.array(change_from_first)  # a copy of change_from_first (given)
### Your Code Here ###
dug_mask = change_from_first > 1
piled_mask = change_from_first < -1
unchanged_mask = (change_from_first >= -1) & (change_from_first <= 1)
thresh[dug_mask] = 1
thresh[piled_mask] = -1
thresh[unchanged_mask] = 0
save_array_visualization(thresh[-1], "Q6_Thresh.jpg", vmin=-1, vmax=1)
print(f"Last day: {(thresh[-1] == 1).sum()} pixels dug out (1), {(thresh[-1] == -1).sum()} pixels piled up (-1), {(thresh[-1] == 0).sum()} pixels unchanged (0)")
print("-" * 50)


# Q7: Crop to the bower (1 point)
#   Using the last day of change_from_first, slice out a rectangle that contains the yellow region in Q6_Thresh.jpg
#   (where the sand was dug out). Use the axis numbers on your picture to choose the rows and columns.
#   Save it as "Q7_Cropped.jpg". Any reasonable crop that contains the yellow region gets full credit.
print('Q7 Output(s):')
### Your Code Here ###
cropped = change_from_first[-1][15:150, 150:175]  # replace None
save_array_visualization(cropped, "Q7_Cropped.jpg", vmin=-1, vmax=1)
print(f"The shape of the cropped image is:\n {cropped.shape}")
print("-" * 50)


##### Additional numpy practice #####
# These questions do not use daily_depths.npy. Use the arrays A, B and X below.
A = np.arange(24).reshape(3, 8)
B = np.array([[0.41764458, 0.27689998],
              [0.30636599, 0.12114929],
              [0.55663027, 0.14760081]])
X = np.array([[0.24059682, 0.77305076, 0.78273994, 0.60932274, 0.22433695, 0.3386874, 0.96034407, 0.55920026],
              [0.68400244, 0.17110986, 0.60284033, 0.66178183, 0.11580537, 0.88716068, 0.01607122, 0.09068437],
              [0.8349345, 0.28651606, 0.34316561, 0.50695525, 0.97961933, 0.80191967, 0.4272247, 0.83928686]])


# Q8: Indexing practice (1 point)
#   1) Get the value at A[2, 3]. What is its type?
#   2) Make a new array C with all rows of A but only the last 2 columns.
#   3) Make a new array D with only column 0 of A. What is its shape?
#   4) Make a new array E with only column 0 of A, but keep it 2D, so its shape is (3, 1).
#      Hint: compare A[:, 0] with A[:, 0:1].
print('Q8 Output(s):')
### Your Code Here ###
value = A[2, 3]
C = A[:, -2:]
D = A[:, 0]
E = A[:, 0:1]
print(f"Q8.1: A[2, 3] is {value} and its type is {type(value)}")
print(f"Q8.2: C is:\n {C}")
print(f"Q8.3: D is:\n {D}\n The shape of D is: {D.shape}")
print(f"Q8.4: E is:\n {E}\n The shape of E is: {E.shape}")
print("-" * 50)


# Q9: Reassignment (1 point)
#   1) Change the value at A[2, 3] to 12. Print A.
#   2) Try to change A[0, 1] to np.nan inside the try/except below, and print the error message.
#      Then convert A to floats with A = A.astype(float) and try again. Print A and its old and new dtype.
#      Why did the first try fail?
#   3) Run F = A. Then change F[0, 0] to 15. Print F and A. What happened to A? Why? How would you prevent it?
print('Q9 Output(s):')
### Your Code Here ###
A[2, 3] = 12
print(f"Q9.1: After reassigning A[2, 3], A is:\n {A}")
try:
    A[0, 1] = np.nan  # replace pass with your line that sets A[0, 1] to np.nan
except ValueError as error:
    print(f"Q9.2: Error: {error}")
old_dtype = A.dtype
A = A.astype(float)
A[0, 1] = np.nan
print(f"Q9.2: After reassigning A[0, 1], A is:\n {A}\n The old dtype was {old_dtype} and the new dtype is {A.dtype}")
print("Q9.2: It failed because: A held integers, and NaN is a float, so it cannot be stored in an integer array.")
F = A
F[0, 0] = 15
print(f"Q9.3: F is:\n {F}")
print(f"Q9.3: A is:\n {A}")
print("Q9.3: What happened to A, why, and how to prevent it: A changed too. F = A does not copy the data, it makes F a second name for the same array in memory. Use F = A.copy() to prevent it.")
print("-" * 50)


# Q10: Boolean indexing (1 point)
#   1) Make mask1, which is True wherever A is less than 5 and False otherwise. Print it.
#   2) Print A[mask1].
#   3) Try B[mask1] inside the try/except below. What happens, and why?
#   4) Use mask1 to set every value in A that is less than 5 to np.nan. Print A.
#   5) Invert mask1 and save it as mask2. Print mask2.
#   6) Print A[mask2].
print('Q10 Output(s):')
### Your Code Here ###
mask1 = A < 5
masked_values = A[mask1]
print(f"Q10.1: mask1 is:\n {mask1}")
print(f"Q10.2: mask1 applied to A is:\n {masked_values}")
try:
    print(B[mask1])  # replace pass with print(B[mask1])
except IndexError as error:
    print(f"Q10.3: Error: {error}")
print("Q10.3: What happened and why: IndexError. mask1 has shape (3, 8) but B has shape (3, 2), so a boolean mask must have the same shape as the array it indexes.")
A[mask1] = np.nan
mask2 = ~mask1
print(f"Q10.4: A is now:\n {A}")
print(f"Q10.5: mask2 is:\n {mask2}")
print(f"Q10.6: mask2 applied to A is:\n {A[mask2]}")
print("-" * 50)


# Q11: Aggregation and combining arrays (1 point)
#   1) What is the sum of the non-NaN values in A?
#   2) How many NaN values are in A?
#   3) What is the sum (ignoring NaNs) of each column of A? Of each row?
#   4) Join A and B side by side into a new array G with shape (3, 10). Hint: np.concatenate with an axis. Print G.
#   5) Stack A and X into a new 3D array H with shape (2, 3, 8). Hint: np.stack. Print H.
#   6) What is the mean (ignoring NaNs) of H along the new axis? What shape is the result?
print('Q11 Output(s):')
### Your Code Here ###
G = np.concatenate([A, B], axis=1)
H = np.stack([A, X])
H_mean = np.nanmean(H, axis=0)
print(f"Q11.1: The sum of non-NaN values in A is:\n {np.nansum(A)}")
print(f"Q11.2: There are {np.isnan(A).sum()} NaN values in A")
print(f"Q11.3: The sum of each column of A is:\n {np.nansum(A, axis=0)}")
print(f"Q11.3: The sum of each row of A is:\n {np.nansum(A, axis=1)}")
print(f"Q11.4: G is:\n {G}")
print(f"Q11.5: H is:\n {H}")
print(f"Q11.6: The mean of H along the new axis is:\n {H_mean}\n Its shape is {H_mean.shape}")


#####################################################################################################################
### How do axes work in numpy? ###
# Make a small 3D array to explore:      arr = np.arange(24).reshape(2, 3, 4)
# arr.shape is (2, 3, 4): arr holds two 2D arrays, each with 3 rows and 4 columns.
#   axis 0 has length 2 (which 2D array), axis 1 has length 3 (rows), axis 2 has length 4 (columns).
#   arr[0, 1]    is row 1 of the first 2D array
#   arr[1, :, 2] is column 2 of the second 2D array
#
# A summary along an axis COLLAPSES that axis and keeps the others.
#   np.sum(arr, axis=0) adds the two 2D arrays together, one position at a time:
#       result[r, c] = arr[0, r, c] + arr[1, r, c]                            -> shape (3, 4)
#   np.sum(arr, axis=1) adds up the rows inside each 2D array:
#       result[i, c] = arr[i, 0, c] + arr[i, 1, c] + arr[i, 2, c]             -> shape (2, 4)
#   np.sum(arr, axis=2) adds up the columns inside each row:
#       result[i, r] = arr[i, r, 0] + arr[i, r, 1] + arr[i, r, 2] + arr[i, r, 3]   -> shape (2, 3)
#   np.sum(arr, axis=(1, 2)) collapses both rows and columns: one total per 2D array  -> shape (2,)
#
# A quick way to check yourself: the result's shape is arr.shape with the collapsed axis removed.
# For daily_depths.npy (days, rows, columns):
#   axis=0       -> one value per pixel (a 2D image), e.g. the NaN count of each pixel over time
#   axis=(1, 2)  -> one value per day
# Open a python interpreter, make arr, and try each line above. Printing arr first helps a lot.
# This video explains the same idea: https://www.youtube.com/watch?v=nS0oKBbNjWY
#####################################################################################################################
