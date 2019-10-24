#Fizz buzz challenge - Trying to do in python without referencing any resources
def fizzbuzz(n):
    for i in range(n + 1):
        if not i % 3:
            print("fizz"),
        if not i % 5:
                print("buzz"),
        if i % 3 and i % 5:
            print(i),
        print

fizzbuzz(100)

# After looking it up heres what most of the solutions looked like So i was slightly off.
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

