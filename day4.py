#Pizza order practice

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What pizza size do you want?") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni?") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese?") # Do you want extra cheese? Y or N
bill = 0
if size =="S":
  bill +=15
if size =="M":
  bill +=20
if size =="L":
  bill +=25
if add_pepperoni =="Y":
  if size == "S":
    bill =+2
  else:
    bill +=3  
if extra_cheese =="Y":
  bill +=1
  
print(f"Your final bill is: ${bill}.")

#Love calculator
print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") 
name2 = input("What is their name?") 
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t+r+u+e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l+o+v+e

score = int(str(first_digit) + str(second_digit))
if (score<10) or (score>90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score>=40) and (score<=50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
  






  

  
