###########################################################
## tshirt greeter chatbot2
## assignment2
# cmpt120
# yanjin chen
#

# greet the user
print("Hi! I am the T-shirt Greeter Chatbot 2! ")

# ask the user for a name
name = input("your first name and last name (one space in between)? ==>")
#
#
words = name.split()
letters = [word[0].upper() for word in words]
print("Welcome", "".join(letters), "!!!")
#
#ask the user for age
age = int(input("Please type your age ==>"))
#
title, handle = name.split()
#
#
#
if handle[0].upper() == "A" or handle[0].upper() == "B":
    mssg = "Queue A or B "

    if age <= 18:
        mssg = mssg + "(youth)"
    else:
        mssg = mssg + "(adult)"

elif handle[0].upper() < "L" and handle[0].upper() > "B":
    mssg = "Queue before L "

    if age <= 18:
        mssg = mssg + "(youth)"
    else:
        mssg = mssg + "(adult)"

else:
    mssg = "Queue L or after "

    if age <= 18:
        mssg = mssg + "(youth)"
    else:
        mssg = mssg + "(adult)"
#
print("You should go to: " + mssg)
#
#
import random
import math

#
num = len(title) + len(handle) + age
num1 = math.sqrt(num)
n = int(num1)
ran = random.randint(0, n)
#
print("TRACE - the sum is:", num, "- the sq root is:", num1, "- n is:", n,
      "- ran is:", ran)
#
text = str((title[0] + title[1]) * ran) + str(ran) + "!!"
print("Your t-shirt will have the text: " + text)
#
#say bye to the user
print("Bye " + title + ", hope to see you again!!")
#
#
