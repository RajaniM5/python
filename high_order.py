# high order funtion = a function that takes another function as an argument or returns a function  
#                                   1. accepts a function as an argument
#                                or 2. returns a function   
#                               returns a function
#                                (In python, functions are treated as objects)

def divisor(n):
    def dividend(y):
        return y / n
    return dividend

divide = divisor(2)
print(divide(10))  # Output: 5.0


# lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

double = lambda x: x+x
print(double(5))  # Output: 10

multi = lambda x,y: x*y
print(multi(4,4))
