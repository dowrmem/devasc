# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

# Ask user for input number and convert to integer
n1 = int(input('Enter a number to see list of divisors: '))

# range of numbers to find divisors
for number in range(1, n1):
    if n1 % number == 0:
        print(number)
