# Author: Caleb Moura

# 6-5
# Defining the function that takes a list of numbers as input
def find_highest_and_lowest(numbers):
    # Check if the list has at least 2 unique numbers
    unique_numbers = set(numbers)
    if len(unique_numbers) < 2:
        return "error: list does not meet specifications"

    # Find highest and lowest values in list
    highest = max(numbers)
    lowest = min(numbers)

    # Return the results
    return highest, lowest


# Example usage of the function
if __name__ == "__main__":
    # Testing with lists
    list1 = [3, 1, 7, 4, 2, 5]
    result1 = find_highest_and_lowest(list1)
    print(f"List: {list1}, Result: {result1}")

    list2 = [5, 5, 5, 5, 5]
    result2 = find_highest_and_lowest(list2)
    print(f"List: {list2}, Result: {result2}")

    list3 = [8, 8, 1, 2, 3, 4]
    result3 = find_highest_and_lowest(list3)
    print(f"List: {list3}, Result: {result3}")

# 6-6:
# Prompt user to input 5 unique words
word1 = input("Enter the first unique word: ")
word2 = input("Enter the second unique word: ")
word3 = input("Enter the third unique word: ")
word4 = input("Enter the fourth unique word: ")
word5 = input("Enter the fifth unique word: ")

# List of the input values in the order given by the user
words_list = [word1, word2, word3, word4, word5]

# List display where each index corresponds to length of the word at corresponding index
lengths_list = [len(word) for word in words_list]
print("List of word lengths:", lengths_list)

# I got lost on the last part so I looked at a "python for dummies" vid to guide me a bit with tags

#6-7:
# Prompt user to input 3 numeric values
value1 = float(input("Enter the first numeric value: "))
value2 = float(input("Enter the second numeric value: "))
value3 = float(input("Enter the third numeric value: "))

# List of the 3 input values in the order provided by the user
values_list = [value1, value2, value3]

# Display of the original list
print("Original list:", values_list)

# Each value doubled and displayed in the the updated list
doubled_values = [int(value * 2) for value in values_list]
print("Doubled values:", doubled_values)

# 6-8:
# Prompt input from the user
num1 = float(input("Enter the first numeric value: "))
num2 = float(input("Enter the second numeric value: "))
num3 = float(input("Enter the third numeric value: "))

# List with the user-input values
numbers_list = [num1, num2, num3]

# Checking if all numbers in the list are even
if all(num % 2 == 0 for num in numbers_list):
    print("even")

# Checking if all numbers in the list are odd
elif all(num % 2 != 0 for num in numbers_list):
    print("odd")

# Neither all even nor all odd = mixed list
else:
    print("mixed")


# 6-5
# Defining the function that takes a list of numbers as input
def find_highest_and_lowest(numbers):
    # Check if the list has at least 2 unique numbers
    unique_numbers = set(numbers)
    if len(unique_numbers) < 2:
        return "error: list does not meet specifications"

    # Find highest and lowest values in list
    highest = max(numbers)
    lowest = min(numbers)

    # Return the results
    return highest, lowest

# Test cases for find_highest_and_lowest function
list1 = [3, 1, 7, 4, 2, 5]
result1 = find_highest_and_lowest(list1)
print(f"List: {list1}, Result: {result1}")

list2 = [5, 5, 5, 5, 5]
result2 = find_highest_and_lowest(list2)
print(f"List: {list2}, Result: {result2}")

list3 = [8, 8, 1, 2, 3, 4]
result3 = find_highest_and_lowest(list3)
print(f"List: {list3}, Result: {result3}")

list4 = [10, 20, 30, 40, 50]
result4 = find_highest_and_lowest(list4)
print(f"List: {list4}, Result: {result4}")

# 6-6:
# Function to get word lengths from user input
def get_word_lengths():
    words_list = [input(f"Enter the {i+1} unique word: ") for i in range(5)]
    lengths_list = [len(word) for word in words_list]
    print("List of word lengths:", lengths_list)

# Test case for get_word_lengths function
get_word_lengths()

#6-7:
# Function to double numeric values
def double_values():
    values_list = [float(input(f"Enter the {i+1} numeric value: ")) for i in range(3)]
    print("Original list:", values_list)
    doubled_values = [int(value * 2) for value in values_list]
    print("Doubled values:", doubled_values)

# Test case for double_values function
double_values()

# 6-8:
# Function to check if a list of numbers is all even, all odd, or mixed
def check_numbers():
    numbers_list = [float(input(f"Enter the {i+1} numeric value: ")) for i in range(3)]
    
    if all(num % 2 == 0 for num in numbers_list):
        print("even")
    elif all(num % 2 != 0 for num in numbers_list):
        print("odd")
    else:
        print("mixed")