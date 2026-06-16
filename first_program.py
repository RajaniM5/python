s = "Python"

reversed_string = s[::-1]
print(reversed_string)

name= input("Enter your name: ")
while name=="":
    print("Name is empty. Please enter a valid name.")
    name= input("Enter your name: ")
print("Hello, " + name + "!")

age= int(input("Enter your age: "))

while age <0:
    print("age cant be negative. Please enter a valid age.")
    age= int(input("Enter your age: "))
    print("Your name is: " + name)
print("Your age is: " + str(age))

num= int(input("Enter a number between 1 and 10: "))
while num < 1 or num > 10:
    print("Number must be between 1 and 10. Please enter a valid number.")
    num= int(input("Enter a number between 1 and 10: "))