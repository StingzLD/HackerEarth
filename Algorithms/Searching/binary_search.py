"""
Rank It

You have been given an array A consisting of N integers. All the elements in this array A are unique. You have to answer some queries based on the elements of this array. Each query will consist of a single integer x. You need to print the rank based position of this element in this array considering that the array is 1 indexed. The rank based position of an element in an array is its position in the array when the array has been sorted in ascending order.

Note: It is guaranteed that all the elements in this array are unique and for each x belonging to a query, value x shall exist in the array

Input Format

The first line consists of a single integer N denoting the size of array A. The next line contains N unique integers, denoting the content of array A. The next line contains a single integer q denoting the number of queries. Each of the next q lines contains a single integer x denoting the element whose rank based position needs to be printed.

Output Format

You need to print q integers denoting the answer to each query.

SAMPLE INPUT
5
1 2 3 4 5
5
1
2
3
4
5
SAMPLE OUTPUT
1
2
3
4
5

Input Sets 1-3:
binary_search_input_set_1.txt
binary_search_input_set_2.txt
binary_search_input_set_3.txt
"""
size = int(input())
lst = list(map(int, input().split(" ")))
queries = int(input())


if lst[0] > lst[1]:
    lst.sort()

for i in range(queries):
    x = int(input())
    low = 0
    high = size - 1
    mid = (low + high) // 2

    while lst[mid] != x:
        if x > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    print(mid + 1)
