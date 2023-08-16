number = int(input("Enter a decimal no: ")) # Decimal Number entered by the user
if number < 0: # User entered a negative number
    print("Please write a valid positive decimal number") 
    exit() # Exiting the script
exp_list = [] # A list to store all the powers of 2 which add up to make the number
binary_number = 0 # Variable to show the binary number
og_number = number # Variable to store the original decimal number

# find_largest_number(number)
# Function to find the largest power of 2 included in the decimal number
# For example, find_largest_number(63) returns 32 as it is the highest power of 2 included in 63
def find_largest_number(number):
    largest_number = 1 # Just assuming the largest number to be 1
    largest = False # A boolean to use to stop the loop (Can remove it and add break in the loop)
    while not largest:
        if largest_number > number: # If the l_number (referring to largest_number) is greater than the number in the argument, that means the prev number was the largest included
            largest_number = largest_number/2 # So we divide lnumber by 2 to get the lnumber
            largest = True # Setting boolean to true to break the loop
        else:
            largest_number = largest_number*2 # Increasing the number by a power of 2 since it is not lnumber
    return largest_number # Returning the lnumber

# find_exp(number)
# Function to find the power of 2
# For example, find_exp(8) returns 3 as 2**3=8
def find_exp(number):
    exp = 0 # Assuming the power to be 0
    while number > 1: # Loop breaks as soon as number reaches less than 1, i.e., 0
        number = number/2 # Breaking no one by one to find its power and increasing exp by 1
        exp+=1
    return exp # Returing the variable

while number > 0: # As long as the decimal number is greater than 0, the loop should work
    num = find_largest_number(number) # Find the lnumber
    number = number - num # Subtract the lnumber from the number
    exp_list.append(num) # Appending the lnumber to the list

for num in exp_list: # Loop to get the binary number
    exp = find_exp(num) # Finding the power of 2
    binary_number = binary_number + 10**exp # Logic for this is explained below

binary_number_str = str(binary_number) # Converting the binary output to string 
rem = 8 - len(binary_number_str) # Knowing the no of times we have to run loop to make the binary number 8 bit
for i in range(rem): # Making it 8 bit by adding 0 at start
    binary_number_str = '0' + binary_number_str

## LOGIC for above conversion
# Binary number - Decimal number
# 1 - 1
# 10 - 2
# 100 - 4
# 1000 - 8
# As visible, the number of zeroes after 1 equals to the 2 raised to the same power 

# Printing the results
print("Decimal number:", og_number) 
print("Binary number:", binary_number_str)
