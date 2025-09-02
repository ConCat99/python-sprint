# Challenge 1: My First Python Function
# MVP
# Write a function called my_first_function.
# Your function should take in a string as an argument.
# It should print in the format: "I love {argument}!".

def my_first_function(param):
    print(f"I love {param} ")

my_first_function('cookies')


# MVP
# Write a function tripler().
# It should take in a number and return the number × 3.
# Print the results with three different arguments.

def tripler(num):
   return  num*3
print(tripler(3))


# Challenge 3: Greeter
# MVP
# Write a function greet() that takes a name as a parameter.
# It should return "Hello, {name}!".

def greet(name):
    return f"Hello, {name}"

print(greet('Connie'))

# Challenge 4: Even or Odd?
# MVP
# Write a function is_even() that takes a number as input.
# Return "Even" if the number is even, "Odd" if it’s odd.

def is_even(num):
    if num%2 ==0:
        return f"{num} is even"
    else:
        return f"{num} is odd"
print(is_even(5))

# Challenge 5: Word Multiplier
# MVP
# Write a function repeat_word(word, times)
# It should return the word repeated times number of times.

def repeat_word(word, iterations):
    ## MY ATTEMPT
    # words: []
    # for word in range (iterations):
    #     words.append(word)
    #     return words

    ##ANS:
 words = word * iterations


print((repeat_word('blah', 3)))





# Challenge 6: Factorial (Stretch)
# MVP
# Write a function factorial(n) that calculates the factorial of n.
# Example: factorial(5) → 5 * 4 * 3 * 2 * 1 = 120.



#-----------------------------------------------------
# LAMDA FUNCTIONS
import math

circle_area_lambda = lambda radius: math.pi  * radius**2

# convert to lambda syntax
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

## MY ATTEMPT
#triangle_area_lambda = lambda a, b, c :((a + b + c) / 2) *  math.sqrt(s * (s - a) * (s - b) * (s - c))

## MAP, FILTER, REDUCE
# Given the list:
nums = [2, 5, 7, 32, 100, 9, 56, 74, 97, 22, 13, 80]
#
# Use a lambda function to filter out even numbers.

even_nums = list(filter(lambda num: num%2 == 0, nums))
print(even_nums)

# Use map with a lambda to multiply all numbers by 3.
tripled_nums= list(map(lambda num: num*3, nums ))
print(tripled_nums)

# Use reduce with a lambda to find the sum of the list.
from functools import reduce
sum = reduce(lambda a, b: a+b, nums )
print(sum)

# Print the final result.
