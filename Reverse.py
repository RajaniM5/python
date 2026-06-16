"""Basic Input & Arithmetic
Hello, User!: Write a program that asks for the user's name and prints a personalized greeting.

Simple Calculator: Create a program that takes two numbers from the user and prints their sum, difference, product, and quotient.

Temperature Converter: Write a program that converts a temperature entered by the user from Celsius to Fahrenheit.

Area of a Circle: Ask the user for the radius of a circle and calculate its area."""

name = input("Enter your name: ")
print(f"Hello, {name}!")

sum = 5 + 3
print(f"Sum: {sum}")


calculator = input("Enter two numbers separated by a space: ")
num1, num2 = map(float, calculator.split())
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")

temperature = float(input("Enter temperature in Celsius: "))
fahrenheit = (temperature * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * radius ** 2
print(f"Area of the circle: {area}")


"""
Conditionals (If/Else)
Odd or Even: Take an integer input from the user and determine whether it is an odd or even number.

Leap Year Checker: Write a program that takes a year as input and checks whether it is a leap year or not.

Voting Eligibility: Ask the user for their age. If they are 18 or older, tell them they are eligible to vote; otherwise, tell them how many years they have left until they can vote.

Max of Three: Write a program that accepts three numbers from the user and displays the largest of the three without using the built-in max() function.

"""

num=input("Enter a number: ")
if int(num%2==0):
    print("The number is even.")
else:
    print("The number is odd.")

vote_age = int(input("Enter your age: "))
if vote_age >= 18:
    print("You are eligible to vote.")
else:
    years_left = 18 - vote_age
    print(f"You have {years_left} years left until you can vote.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")


"""Prime Number Checker: Write a function that checks whether a given number is a prime number (only divisible by 1 and itself) and returns True or False.

Guess the Number Game: Write a small program where the computer chooses a random number between 1 and 20, and the user has to guess it. The program should tell the user if their guess is "too high" or "too low" until they get it right.

Word Counter: Ask the user to input a sentence, and write a program that counts and prints the total number of words in that sentence.
"""

prime_check = int(input("Enter a number to check if it's prime: "))
is_prime = True
if prime_check < 2:
    is_prime = False
else:
    for i in range(2, int(prime_check ** 0.5) + 1):
        if prime_check % i == 0:
            is_prime = False
            break
print(f"{prime_check} is {'prime' if is_prime else 'not prime'}")
