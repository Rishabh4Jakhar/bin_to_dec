# bin_to_dec (Integer to Binary)
A simple code for converting integers to binary numbers. 

## How to use
- Simply copy the code from the `bin_to_dec.py` file and run it in your device.
- Enter your integer when asked to in console and see the result

Note: If the number is between 0-255, it is converted to a 8 bit binary number (idk why I decided on this)

## Why I made this ?
ChatGPT thought this would be a good project to help broaden my python knowledge. Even though I know this is a bad, unoptimized code but I tried.

## Working
The code tries to find the largest exponent of 2 in the given number and continues to do so until the number left is 0. For example, number is 153. So the code splits the number into `[128, 16, 8, 1]`. It stores this data and then by using the simple logic that the power of 2 is equal to the same power raised to for 10 in binary. It converts and adds all the numbers, forming the binary number. 
So for 153, it would work in the following way:
- List of numbers: `[128, 16, 8, 1]`
- 128 => 2^7 => 10000000
- 16 => 2^4 => 10000
- 8 => 2^3 => 1000
- 1 => 2^0 => 1
- Adding all the numbers => 10011001 (Final Output)

## Note
For any suggestions or stuff, dm me on [discord](https://discord.com/users/713056818972066140) and thanks for visiting here :)
