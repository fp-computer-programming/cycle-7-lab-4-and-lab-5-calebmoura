# Author: Caleb Moura

# Function to find the sum of two numbers.
def find_sum(num1, num2):
    """
    Add the arguments and store the result in num_sum.
    Return the sum.
    """
    num_sum = num1 + num2
    return num_sum

# Call function to find the sum 111 and 222.
my_sum = find_sum(111, 222)

# Print the result of the two numbers.
print("The sum is:", my_sum)

# Test Case 1
# Check if the sum of 5 and 10 is correct.
if find_sum(5, 10) == 15:
    print("15")
else:
    print("Sum is Incorrect")

# Test Case 2
# Check if the sum of -3 and 8 is correct.
if find_sum(-3, 8) == 5:
    print("5")
else:
    print("Sum is Incorrect")

# Test Case 3
# Check if the sum of -7 and -2 is correct.
if find_sum(-7, -2) == -9:
    print("-9")
else:
    print("Sum is Incorrect")

# Test Case 4
# Check if the sum of 100 and 200 is correct.
if find_sum(100, 200) == 300:
    print("300")
else:
    print("Sum is Incorrect")