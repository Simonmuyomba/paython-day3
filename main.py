#Control flow with if / else and conditional operators

print("Welcome to my page 🫥")
user_input = int(input("What is your age? "))

if user_input >= 16:
  print("Access granted ")
  num = int(input(print("Enter your number : ")))
  if num >= 100:
    print("Congrats.....You may enter ")
  elif num < 100:
    print("Sorry...You're not allowed to enter ")
  elif num == 0:
    print("You not recognized ")
else:
  print("Access denied!")
