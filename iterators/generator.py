def week():
  days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
  ]

  for day in days:
    yield day

def yes_or_no():
  choice = "yes"
  while True:
    yield choice
    choice = "no" if choice == "yes" else "yes"

def current_beat():
  nums = (1,2,3,4)
  i = 0
  while True:
    if i >= len(nums): i = 0
    yield nums[i]
    i += 1

def make_song(times, drink):
  for num in range(times, -1, -1):
    if num > 1:
      yield "{} bottles of {} on the wall.".format(num, drink)
    elif num == 1:
      yield "Only 1 bottle of {} left".format(drink)
    else:
      yield "No more {}!".format(drink)