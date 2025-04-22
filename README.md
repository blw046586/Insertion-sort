# Insertion-sort
The script has four steps:

Read a list of integers (no duplicates).
Output the numbers in the list.
Perform an insertion sort on the list.
Output the number of comparisons and swaps performed during the insertion sort.
Steps 1 and 2 are provided in the script.

Implement step 3 based on the insertion sort algorithm in the book. Modify insertion_sort() to:

Count the number of comparisons performed.
Count the number of swaps performed.
Output the list during each iteration of the outside loop.
Implement step 4 at the end of the script.

Hints: In order to count comparisons and swaps, modify the while loop in insertion_sort(). Use global variables for comparisons and swaps.

The script includes three helper functions:

read_nums() # Read and return a list of integers.
print_nums(nums) # Output the numbers in nums
swap(nums, n, m) # Exchange nums[n] and nums[m]
Ex: When the input is:

3 2 1 5 9 8
the output is:

3 2 1 5 9 8

2 3 1 5 9 8
1 2 3 5 9 8
1 2 3 5 9 8
1 2 3 5 9 8
1 2 3 5 8 9

comparisons: 7
swaps: 4
