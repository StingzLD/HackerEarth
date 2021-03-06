"""
Last Occurrence

You have been given an array of size N consisting of integers. In addition you have been given an element M you need to find and print the index of the last occurrence of this element M in the array if it exists in it, otherwise print -1. Consider this array to be 1 indexed.

Input Format:

The first line consists of 2 integers N and M denoting the size of the array and the element to be searched for in the array respectively . The next line contains N space separated integers denoting the elements of of the array.

Output Format

Print a single integer denoting the index of the last occurrence of integer M in the array if it exists, otherwise print -1.

SAMPLE INPUT
5 1
1 2 3 4 1
SAMPLE OUTPUT
5
"""

# Write your code here
size, ele = input().split(" ")
lst = input().split(" ")
last_index = -1

for i in range(int(size)):
    if lst[i] == ele:
        last_index = i + 1

print(last_index)
