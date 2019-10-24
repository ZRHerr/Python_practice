# Attempting first using no resource as help

# Getting User input
str = input("the string you want to reverse: ")
# Method that reversed the input - also added upper - not for any specific reason just looks
def uppercase_reverse(text):
    uppercase = str.upper()
    return uppercase[::-1]
# calling the method and adding the input
print(uppercase_reverse(str))

# after looking into the way of doing this below is what i found. good reference and 
# nice to see the difference from my original thought.
def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s

