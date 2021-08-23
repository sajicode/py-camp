from random import choice

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

for month in months:
  print(month)

values = [10,20,30]

static_values = tuple(values)

rand = choice(range(0, 12))

def generate_evens():
  return [i for i in range(1, 50) if i % 2 != 0]

print(generate_evens())

def yell(word):
  return '{word}!'.format(word=word.upper())

print(yell("good morning"))