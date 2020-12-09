##
#cmpt120-d200
#yanjin chen

import random
import math

#greet the user
print("Hi! I am your travel agent bot!")

#ask the user for name
name = input("\nWhat is your name? ==> ")
print("Nice to meet you, " + name)

#inform user the general traveling options
note1 = "- where to go"
note2 = "- travel modality"
note3 = "- style of trip"
note4 = "- lenght of trip"

print("\nNOTE: ")
print("You will be able to choose: ")
print(" " + note1.center(30) + " ")
print(" " + note2.center(33) + " ")
print(" " + note3.center(32) + " ")
print(" " + note4.center(32) + " ")

#notice to user
print("\nPlease provide your choice as asked.")
print("if I do not understand you, I will choose for you.")

input()
#ask user where to go
print("We offer trips to Antartica, Bahamas, Cartagena or Washington")
dest = input("Where would you like to go? ==> ").capitalize()

deses = ["Antartica", "Bahamas", "Cartagena", "Washington"]

if dest in deses: 
  dest = dest
  print("Nice! You chose " + dest)
else:
  dest = random.choice(deses)
  print("I did not understand." + " I chose " + dest + " for you")

#ask user the first travel modality
print("\nWe offer trips via 1-plane, 2-cruise, 3-bus, 4-hiking")
fmodal = input("Your first travel modality? (indicate the number) ==> ")

chos = ["plane", "cruise", "bus", "hiking"]

if fmodal == "1":
  print("Good, your first choice is plane")
  fmodal = "plane"
elif fmodal == "2":
  print("Good, your first choice is cruise")
  fmodal = "cruise"
elif fmodal == "3":
  print("Good, your first choice is bus")
  fmodal = "bus"
elif fmodal == "4":
  print("Good, your first choice is hiking")
  fmodal = "hiking"
else:
  print("That is not a valid modality." + " I chose " + random.choice(chos) + " for you")
  fmodal = random.choice(chos)

#ask user the second travel modality
smodal = input("\nYour second travel modality? (number, 0 if none) ==> ")

chos = ["plane", "cruise", "bus", "hiking"]

if smodal == "1":
  print("Good, you also chose: plane")
  smodal = "plane"
elif smodal == "2":
  print("Good, you also chose: cruise")
  smodal = "cruise"
elif smodal == "3":
  print("Good, you also chose: bus")
  smodal = "bus"
elif smodal == "4":
  print("Good, you also chose: hiking")
  smodal = "hiking"
elif smodal == "0":
  print("I see that you do not want another travel modality")
  smodal = "none"

else:
  print("That is not a valid modality." + " I chose " + random.choice(chos) + " for you")
  smodal = random.choice(chos)

#ask user the style of trip
print("\nWe offer trips style: regular or deluxe")

if fmodal == "4" or smodal == "4" or fmodal == "hiking" or smodal =="hiking" :
  print("Since you will be hiking, the style can only be regular")
  softrp = "regular"
else: 
  softrp = input("Which style do you prefer? ==> ").lower()
  
  sty = ["regular", "deluxe"]

  if softrp in sty:
      print("Nice! you chose: " + softrp)
      softrp = softrp
  else:
      print("I did not understand." + " I chose " + random.choice(sty) + " for you")
      softrp = random.choice(sty)

#ask user the lenght of trip 
lenght = input("\nHow many days would you like to travel? (indicate the number) ==> ")

# cost calculation 
print("\nTRACE - Intermediate calculations cost")

# calculate traveling cost
if fmodal == "plane" or fmodal == "cruise":
  travelcost = int(lenght) * 400
else:
  travelcost = int(lenght) * 200


if smodal == "none":
  travelcost = travelcost
elif smodal == "plane" or smodal == "cruise":
  travelcost = travelcost + int(lenght) * 400 
else: 
  travelcost = travelcost + int(lenght) * 200


# calculate extra cost 
if dest[0].upper() > "K":
  extracost = 50
elif softrp == "deluxe":
  extracost = 1000
elif dest[0].upper() > "K" and softrp == "deluxe":
  extracost = 1050
else:
  extracost = 0

#calculate tax 
tax = math.pi* (len(name))* 0.1
#total cost 
totalcost =int( tax + travelcost + extracost )

#trace all costs
print("\nTRACE - travelling cost for ", lenght, " days" + " is: ", travelcost)
print("TRACE - extras (deluxe and destination > 'K') cost is: ", extracost)
print("TRACE - len(name): ", len(name))
print("TRACE - tax 10% len(name)* math.pi: ", tax)

note = "Your cost is: " + str(totalcost)
print("***", note.ljust(30))

input()
#reservation code
n = 3 + int(lenght) % 4 
code1 = dest[0:3].upper() * n
code2 = str(n)  

if smodal =="0": 
  code3 = fmodal[0:2] + "*"
else: 
  code3 = fmodal[0:2] + smodal[0:2]

reservcode = code1 + code2 + code3
lgh_code = len(reservcode)

if len(reservcode) % 2 == 0:
  reservcode = reservcode + "$$" 
else:
  reservcode = reservcode + "$"

#trace all info and reservation code
print("\n*******************")
print("Your trip will be to: ", dest.capitalize())

if smodal == "0": 
  modal = fmodal
else:
  modal = fmodal + " and " + smodal

print("Traveling via: ", modal)
print("with style:", softrp)
print("And reservation code: ", reservcode)

#trace my calculation 
print("\n*******************")
print("\nTRACE - n: 3 + reminder days divided by 4 is: ", n)
print("TRACE - length of reservation code before $ is: ", lgh_code)

#ending 
yeses = ["yes", "y","of course","certainly", "sure","yes of course", "likely yes"]

noses = ["no", "n","no way", "of course not", "never"]

res = input("\nDo you think you will travel with us (yes/no)? ==> ").strip("!").lower()

if res in noses: 
  print("Ohhh maybe next time!")
elif res in yeses: 
  print("Great!! Glad to hear that!")
else: 
  print("sorry, I don't understand...")

print("Bye, see you next time!")

input()
### END THE PROGRAM













