def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def subtract(a, b):
    return a - b

def factorial(a):
    if a <= 1: return 1
    return a * factorial(a - 1)
