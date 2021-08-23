# ask for age
age = input("How old are you?: ")

if age:
  age = int(age)
  if age >= 18 and age < 21:
    print("You can enter, but need a wristband")

  elif age >= 21:
    print("you are good to enter & drink")

  else:
    print("you shall not pass young blood 🥲")

else:
  print("Please enter an age")