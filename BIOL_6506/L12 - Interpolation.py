"""
Group Members: []

Exercise 12 - Interpolation (9 points)

Due Date: Wednesday October 28th, 2026 @ 12:30pm

Directions:
Complete the questions below. Each question is worth 1 point. Edit this script directly and submit it.
Keep InterpolationData.npy in the same folder as this script, then run it from the terminal:
    python3 "Exercise 12 - Interpolation.py"
Do not delete the "Q# Output(s):" print statements. The TA uses them to find your answers.
The "Cheat Sheet for Today" slide from today's lecture has the functions you need.

Collaboration:
You are welcome to work with your team on this assignment.

Submission Details:
Please submit one script per team. Include the .jpg files your script makes (Q2_Nans.jpg, Q6_Before.jpg, Q6_After.jpg).
"""
# This exercise uses numpy to fill in missing data by interpolation.
# In the last two exercises you analyzed daily depth data from a male cichlid building a bower. Some pixels had no
# data and were stored as np.nan. But sand doesn't jump around much from one moment to the next, so if a pixel is
# missing in one frame we can make a good guess at its value from the frames just before and after it.
# Estimating missing values from nearby good data is called interpolation.
#
# InterpolationData.npy holds 120 depth frames recorded over time from a single tank. Its shape is
# (120, 480, 640): axis 0 is the frame (time), axes 1 and 2 are the rows and columns of the image.

import numpy as np
import matplotlib
matplotlib.use('Agg')  # lets the script save figures without opening a window
from matplotlib import pyplot as plt


def save_array_visualization(array, filename, vmin, vmax):
    # This function is provided for you. It saves a picture of a 2D array.
    # vmin and vmax set the range of the color bar: values at or below vmin are dark purple,
    # values at or above vmax are yellow.
    if not filename.endswith('.jpg'):
        filename = filename + '.jpg'
    plt.figure()
    plt.imshow(array, cmap='viridis', vmin=vmin, vmax=vmax)
    plt.colorbar()
    plt.savefig(filename, format='jpg')
    plt.close()


# Q1: Load "InterpolationData.npy" into an array called data. Print its shape. (1 point)
data = np.load("InterpolationData.npy")  # your code here

print(f"Q1 Output(s): {data.shape}")
# your code here


# Q2: How many frames are missing at each pixel? (1 point)
# A pixel might have good data in 110 frames and np.nan in the other 10. Make a 2D array called nan_counts,
# shape (480, 640), that holds the number of nan frames at each pixel.
# Hint: np.isnan() gives True/False, and summing True/False along axis 0 counts the Trues.
# Then:
#   - save a picture of nan_counts with save_array_visualization(nan_counts, 'Q2_Nans.jpg', 0, 120)
#   - print how many pixels have at least one nan frame
#   - print how many pixels are nan in all 120 frames
nan_counts = np.isnan(data).sum(axis=0)  # your code here

save_array_visualization(nan_counts, 'Q2_Nans.jpg', 0, 120)

print("Q2 Output(s):")
print(f"pixels with at least one nan frame: {(nan_counts > 0).sum()}")
print(f"pixels that have nan in all 120 frames: {(nan_counts == 120).sum()}")
# your code here

# Q3: Find every pixel with one or two nan frames. (1 point)
# Use np.where to get the locations of these pixels and store the result in interp_pixels.
# Because nan_counts is 2D, np.where returns a tuple of TWO arrays: the row numbers and the column numbers.
# Print how many pixels you found (it should be 18632).
# Hint: combine two conditions with & and put each one in parentheses: (a >= 1) & (a <= 2)
interp_pixels = np.where((nan_counts >= 1) & (nan_counts <= 2))  # your code here

print("Q3 Output(s):")
# your code here
print(f"pixel with one or two nan frames: {len(interp_pixels[1])}")

# Q4: Interpolate the missing data at one pixel.
# The pixel at row 38, column 619 has a missing frame. We pull out its 120 values below.
# .copy() makes pixel its own array, so changing it will not change data. (Without .copy(), pixel would
# be a view, and changing it would also change data.)
pixel = data[:, 38, 619].copy()  # given

# Q4.1: Use np.where to find the frame numbers where pixel is nan. Store them in x_bad.
# Print x_bad and how many frames are missing. (1 point)
x_bad = np.where(np.isnan(pixel))[0]  # your code here

print("Q4.1 Output(s):")
# your code here
print(x_bad)
print(f"number of frames where pixel is nan: {len(x_bad)}")


# Q4.2: Use np.where to find the frame numbers where pixel is NOT nan. Store them in x_good.
# Print how many good frames there are. (1 point)
x_good = np.where(~np.isnan(pixel))[0]  # your code here

print("Q4.2 Output(s):")
print(x_good)
print(f"number of frames where pixel is NOT nan: {len(x_good)}")
# your code here

# Q4.3: Use np.interp to estimate the depth at each missing frame. Store the result in y_interp and print it.
# np.interp(x, xp, fp): x = the frames you want values for, xp = the frames you have data for,
# fp = the data at those frames. (1 point)
y_interp = np.interp(x_bad, x_good, pixel[x_good])  # your code here

print("Q4.3 Output(s):")
print(f"estimated depth at missing frame: {y_interp}")

# Q4.4: Put the interpolated values into pixel at the missing frames. Then print how many nans
# pixel has now (it should be 0). (1 point)
# your code here

print("Q4.4 Output(s):")
pixel[x_bad] = y_interp

# Count the NaNs that remain. This should be 0 now.
print(f"how many nans remain: {np.isnan(pixel).sum()}")
# your code here


# Q5: Repeat Q4.1-Q4.4 for every pixel in interp_pixels, changing data itself this time. (1 point)
# We only fill pixels missing 1-2 frames. With more missing data, the guesses would not be reliable.
# Hint: use zip() to loop over the row and column arrays in interp_pixels together:
#     for row, col in zip(interp_pixels[0], interp_pixels[1]):
# Here pixel = data[:, row, col] WITHOUT .copy() is what you want, because changing pixel then changes data.
# Note: if the missing frame is the first or last one, np.interp just copies the nearest good value.
# After the loop, print the total number of nan values left in data.
# your code here

print("Q5 Output(s):")
# your code here
for k in range(len(interp_pixels[0])):
    row = interp_pixels[0][k]
    col = interp_pixels[1][k]
    pixel = data[:, row, col]
    x_bad = np.where(np.isnan(pixel))[0]
    x_good = np.where(~np.isnan(pixel))[0]
    y_interp = np.interp(x_bad, x_good, pixel[x_good])
    pixel[x_bad] = y_interp

print(f"number of nan values left in data: {np.isnan(data).sum()}")


# Q6: Check your work. (1 point)
# Recalculate nan_counts from the updated data and print how many pixels still have at least one nan frame.
# This should be 18632 fewer than your first answer in Q2.
# Then save two pictures on a 0-5 scale so that small counts are easy to see:
#   save_array_visualization(<nan counts from BEFORE Q5>, 'Q6_Before.jpg', 0, 5)
#   save_array_visualization(<nan counts AFTER Q5>, 'Q6_After.jpg', 0, 5)
# In a comment, describe what changed between the two pictures.
# your code here

print("Q6 Output(s):")
# your code here
nan_counts_after = np.isnan(data).sum(axis=0)
save_array_visualization(nan_counts, 'Q6_Before.jpg', 0, 5)
save_array_visualization(nan_counts_after, 'Q6_After.jpg', 0, 5)

# What changed between Q6_Before.jpg and Q6_After.jpg?
# Answer: The scattered low-count pixels (the ones missing 1 or 2 frames) in Q6_Before.jpg are gone in Q6_After.jpg and now have a count of 0. 
# Pixels that are missing 3 or more frames were not filled, so they look the same in both pictures
