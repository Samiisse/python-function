#Implement a function that returns the factorial of a given number using recursion

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example usage:
number = 5
print("Factorial of", number, "is", factorial(number))
