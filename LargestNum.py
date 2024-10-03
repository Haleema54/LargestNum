'''

3)Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6
program:
# Input: Read the size of the list
size = int(input())

# Initialize an empty list
numbers = []

# Input: Read the elements of the list
for _ in range(size):
    number = int(input())
    numbers.append(number)  # Append each number to the list

# Find the largest number in the list
largest_number = max(numbers)

# Output: Display the largest number
print(largest_number)
'''
