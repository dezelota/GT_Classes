"""
Group Members: []

Exercise 10 - NumPy Basics (10 points)

Due: Wednesday, October 21, 2026 @ 12:30pm

Directions:
Complete the questions below. Edit this python script directly and submit it.
Put daily_depths.npy in the same folder as this script, then run it from the terminal:
    python "Exercise 10 - NumPy Basics.py"
Print each answer under its "Q# Output(s):" line so the TA can find it.

Collaboration / Submission:
You are welcome to work with your team on this assignment. Please submit one script per team.
"""
# The McGrath lab studies the evolution of behavior using Lake Malawi cichlid fishes.
# In the lake, some of these fish live over sand and perform complex courtship behaviors to attract mates.
# Males move sand on the lake bottom (or in a lab tank) to dig large pits or build sand mounds called 'castles'.
# This behavior is called bower building. In the lab, we measure bower building by recording the sand surface
# with a depth sensor.
# The file daily_depths.npy holds 12 depth snapshots of the sand surface, one per day of bower building.
# Each value is the distance from the depth sensor (above the tank) down to the sand surface.
# In this exercise you will use this array to practice basic numpy operations.

# Install numpy and matplotlib with conda or pip if you don't already have them.
import numpy as np
import matplotlib
matplotlib.use('Agg')  # save figures to files without opening a window
import matplotlib.pyplot as plt


def save_array_visualization(array, filename):  # (0 points) GIVEN - do not change
    # Saves a picture of a 2D numpy array. Give it the array and a filename.
    # Values are colored from -5 (dark purple) to +5 (yellow). NaN values are not drawn, so they show up white.
    if not filename.endswith('.jpg'):
        filename = filename + '.jpg'
    plt.figure()
    plt.imshow(array, cmap='viridis', vmin=-5, vmax=5)
    plt.colorbar()
    plt.savefig(filename, format='jpg')
    plt.close()


# Q1: Loading an array from a file (1 point)
#   Load "daily_depths.npy" into a variable called data with np.load(). Then print the first element of the array.
print('Q1 Output(s):')
data = np.load('daily_depths.npy')  # replace None
# print(f"The first element in the loaded numpy array is:\n {data[0]}")
print("-" * 50)
print(data[0, 0, 0])

# Q2: Basic attributes of the array (2 points)
#   Print each of these attributes of data:
#     a) the shape
data_shape = data.shape
#     b) the size
data_size = data.size
#     c) the number of dimensions
data_dims = data.ndim
#     d) the data type
data_type = data.dtype
#     e) What do you think each of the three dimensions represents? Use the shape and the description at the top
#        of this file.
print('Q2 Output(s):')
print(f"The shape of the numpy array is:\n {data_shape}")
print(f"The size of the numpy array is:\n {data_size}")
print(f"The number of dimensions in the numpy array is:\n {data_dims}")
print(f"The type of data in the numpy array is:\n {data_type}")
print("The three dimensions represent: first dimension is days. The second and third are the row and column positions of the sensor frame. Each value is the distance from the sensor to the sand.")
print("-" * 50)


# Q3: Indexing the array (1 point)
#   a) Use indexing to get the first depth frame and the last depth frame
#   b) Subtract the first frame from the last frame (element-wise) to get the total depth change. Call it change.
#   c) Use save_array_visualization() to save change as "Q3.jpg"
#   d) Describe what the picture shows. What do the yellow and dark purple areas represent? What do the white areas represent?
#   You will be graded on Q3.jpg and your description.
print('Q3 Output(s):')
### Your Code Here ###
first_frame = data[0]
last_frame = data[-1]
change = last_frame - first_frame  # replace None
save_array_visualization(change, "Q3.jpg")
print("The colors in Q3.jpg represent: yellow = sand removed (pits, surface farther from the sensor), dark purple = sand added (mounds/castles, surface closer to the sensor), white = missing (nans)")
print("-" * 50)


# Q4: Summary statistics and NaN values (2 points)
#   a) Find the minimum and maximum values in data
#   b) Find the minimum and maximum again, but ignore the NaN values (hint: np.nanmin)
#   c) Find the mean, median, standard deviation, and sum of the non-NaN values in data
#   d) Find the minimum and maximum depth change in change from Q3. Does change also contain NaN values?
data_max = data.max()
data_min = data.min()
data_min_na = np.nanmin(data)
data_max_na = np.nanmax(data)
data_mean_na = np.nanmean(data)
data_med_na = np.nanmedian(data)
data_std_na = np.nanstd(data)
data_sum_na = np.nansum(data)
max_depth_change = np.nanmax(change)
min_depth_change = np.nanmin(change)

change_has_nans = np.isnan(change).any()

print('Q4 Output(s):')
print(f"The minimum value of all the data is:\n {data_min}")
print(f"The maximum value of all the data is:\n {data_max}")
print(f"The minimum value, ignoring NaNs, is:\n {data_min_na}")
print(f"The maximum value, ignoring NaNs, is:\n {data_max_na}")
print(f"The mean value, ignoring NaNs, is:\n {data_mean_na}")
print(f"The median value, ignoring NaNs, is:\n {data_med_na}")
print(f"The standard deviation, ignoring NaNs, is:\n {data_std_na}")
print(f"The sum, ignoring NaNs, is:\n {data_sum_na}")
print(f"The minimum depth change is:\n {min_depth_change}")
print(f"The maximum depth change is:\n {max_depth_change}")
print("-" * 50)
print(f"Does change have any NaNs?\n {change_has_nans}")


# Q5: Boolean arrays (1 point)
#   a) Make a boolean array called mask, the same shape as data. It should be True wherever data is NaN and False
#      everywhere else.
#   b) Use mask to count the total number of NaN values
#   c) Invert mask so it is True wherever data is NOT NaN. Call it inv_mask.
#   d) Use inv_mask and data to find the sum of the non-NaN values WITHOUT np.nansum. Check that it matches your
#      answer from Q4 with np.isclose(), which allows for tiny rounding differences.
print('Q5 Output(s):')
### Your Code Here ###
mask = np.isnan(data)
num_nas = mask.sum()
inv_mask = data[~mask]
num_vals = inv_mask.sum()
#matches = num_vals == data_sum_na
matches = np.isclose(num_vals, data_sum_na)
print(f"Using the mask array, the number of NaN values is:\n {num_nas}")
print(f"Using the inverted mask, the sum of non-NaN values is:\n {num_vals}")
print(f"Does it match Q4?\n {matches}")
print("-" * 50)


# Q6 (challenge): Day-by-day change (3 points)
#   In Q3 you found the change between the first and last day. Now find the change between each pair of
#   neighboring days (day 1 to day 2, day 2 to day 3, ...) and save a picture of each one.
#   Name the files Change1.jpg, Change2.jpg, ... (there should be 11 files).
#   Use a for loop. Try to do it in as few lines as possible.
#   Look at your 11 pictures. In a print statement, say which day had the most sand movement.
print('Q6 Output(s):')
### Your Code Here ###
for i in range(1, 12):
    first_frame = data[(i-1)]
    last_frame = data[i]
    change = last_frame - first_frame
    save_array_visualization(change, f"Change{i}.jpg")

print("The most sand moved between day 1 and day 2")
