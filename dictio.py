user_info = {
  "name": "Julien",
  "gender": "male",
  "is_awesome": True,
  73: "magic number",
  "games": {

  }
}

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f"{artist['first']} {artist['last']}"


for key, value in user_info.items():
  print(f"key is {key}, value is {value}")

# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
    print(f"{str(bakery_stock[food])} left")
else:
  print("We don't make that")


game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

initial_game_state = dict.fromkeys(game_properties, 0)

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()
  
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

states = {list1[i]: list2[i] for i in range(0, 3)}

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

answerdict = {thing[0]: thing[1] for thing in person}

chars = {count: chr(count) for count in range(65, 91)}