from random import choice

print("How many kilometers did you run today?")
kms = float(input())
miles = kms/1.60934
print(f"OK! You ran {round(miles, 2)} miles")
