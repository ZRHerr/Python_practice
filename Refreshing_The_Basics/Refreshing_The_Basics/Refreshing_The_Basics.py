# User input Exercise Calculating Tip Recommendations
import random
from math import sqrt
# Displaying a message to the user to let them know what they are inputting.
print("What is the total cost of the bill?: ")
# Assigning a variable to the user input of how much their bill costed
total_cost = float(input())
# printing out a confirmation displaying their input to ensure there wasn't any accidental input that could render
# their tip percentages inaccurate.
print(f"The recommended tip amounts for {total_cost} are: ")
# printing out the total at 15% by multipling the total cost by 0.15 than formatting to show only 2 decimal spaces for cents
print(f"${round(total_cost * 0.15, 2)} at 15 percent - your server did their job well")
# printing out the total at 18% and formatting to only display 2 decimal places for cents
print(f"${round(total_cost * 0.18, 2)} at 18 percent - your server had a great personality")
# same as above but at 20%
print(f"${round(total_cost * 0.20, 2)} at 20 percent - your server did an amazing job")

# Practicing some basic if/else conditional statments

answer = input("Do you want to hear a joke? ")
affirmative_responses = ["yes", "y"]
negative_responses = ["no", "n"]
if answer.lower() in affirmative_responses:
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedburg (RIP)
elif answer.lower() in negative_responses:
    print("Fine.")
else:
    print("I don't understand.")


#Practicing some basic loops

#Microsoft random interview results
students_first_names = ["Zach","Will","Stephen","Lindsay","Alex","Tyler","Josh","Tom"]
answers = ["Yes","No","Not Right Now","Never","Please work for us"]

for name in students_first_names:
	print(f"{name}'s answer is", {random.choice(answers)})

# Challenge: print out the squares of the number 1-10
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
	print(f"{num} square root is", {sqrt(num)})


