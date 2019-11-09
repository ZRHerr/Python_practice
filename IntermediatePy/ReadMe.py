# Python Philosophy  | Lists, Conditionals, List Operations, Sets & Dictionaries Below! 

# Beautiful is better than ugly, Explicit is better than implicit, Simple is better than complex.
# Complex is better than complicated, Flat is better than nested, Sparse is better than dense.
# Readability counts, Special cases aren't special enough to break the rules, Although practicality beats purity.
# Errors should never pass silently, Unless explicitly silenced, In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it, Although that way may not be obvious at first unless you're Dutch.
# Now is better than never, Although never is often better than *right* now, If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea, Namespaces are one honking great idea -- let's do more of those!

# List Comprehensions

names = ["Zach", "Michael", "Bob", "Jeff"]
upper_names = []
for name in names:
    upper_case_name = name.upper()
    upper_names.append(upper_case_name)

# Shortcut for the above 
[name.upper() for name in names] 
# Create Lists Recursively
[num * num for num in range(6)]
# List of Tuples
[("length", len(name)) for name in names]
# easy concat
", ".join([f"Name is {name} " for name in names])
# adding conditional for even numbers only
even_squares = [num * num for num in range(6) if num % 2 == 0]
", ".join([str(even_square)for even_square in even_squares])
# Converting list of strings to list of ints
lottery = "1, 22, 54, 288"
lottery.split(", ")
[int(num) for num in lottery.split(", ")]
# Set (collection of keys) Dictionary (Key/Value Pairs)
# Key is original number value is the square
{num: num * num for num in range(11)}
# Generator object 
(num * num for num in range(6))
# Slicing a list
my_string = "Hello, World!"
my_string[0:5] # Returns 'Hello'
my_string[-2] # Returns 'd' - can index through in a circular motion
# Using a list renders same results as string
names[-1] # Last item in names
names[0:2] # Returns first two elements
names.append("Zachary")
# zip function
players = ["Zach", "Alex", "Bobby", "Bill"]
scores = [100,5,88,21]
zip(players, scores)
for name, score in zip(players, scores):
    print(f"Name: {name} had a score of {score}")
#Dictionary
dict(zip(players, scores))