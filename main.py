isHungry = input("Y/N: Are you hungry? ")
isBored = input("Y/N: Are you bored? ")

if(isHungry == "Y"or isHungry == "y"):
  print("Go eat")
else:
  print("Don't eat")
if(isBored == "Y" or isBored == "y"):
  print("Go to sleep")
else:
  print("Do nothing")

userNumber = int(input("Give me a number: "))
if(userNumber > 0):
  print("Your number is positive")
else:
  print("Your number is negative")

# Ask the user fo their age. If the user is older than 17, let them know that they can watch all movies.
# If they are younger than 17 but older than 13 let them know that they can watch G-Rated and PG-13.
# If they are younger than 13, they are only allowed to watch just G-Rated movies.

userAge = int(input("Enter your age: "))

if(userAge > = 17):
  print("You can watch all movies! ")
elif(userAge > = 13):
  print("You can watch g-rated and PG-13 movies.")
elif(userAge < 13):
  print("You can only watch G-Rated movies.")

# Ask the user for an x and a y value
# Based on the x and y value, output which quadrant they're in

x = int(input("Give me an x value: "))
y = int(input("Give me a y value"))

if(x > 0 and y > 0):
  print("Quadrant I")
elif(x > 0 and y < 0):
  print("Quadrant IV")
elif(x < 0 and y > 0):
  print("Quadrant II")
elif(x < 0 and y < 0):
  print("Quadrant III")
elif(x == 0 and y != 0):
  print("y-axis")
elif(x != 0 and y == 0):
  print("x-axis")