# python error types

# SyntaxError
# NameError
# TypeError
# IndexError
# KeyError
# ValueError
# AttributeError

# raise ValueError('invalid value')
# raise NameError('invalid value')
import keyword

def contains_keyword(*args):
  for item in args:
      if keyword.iskeyword(item): return True
  return False

# print(contains_keyword('de', 'return'))

def colorize(text, color):
  colors = ("cyan", "yellow", "blue", "green", "magenta")
  if type(text) is not str:
    raise TypeError("text must be instance of str")
  if color not in colors:
    raise ValueError(f"color {color} is invalid")
  print(f"Printed {text} in {color}")

# colorize("hello", "yeaga")

## try - except
def get(d, key):
  try:
      return d[key]
  except KeyError:
      return None

dictio = {"name": "Rick Sanchez"}
# print(get(dictio, "ui"))

def checkNum(num):
  try:
    if type(num) != int:
      raise TypeError('Invalid type, enter a number')
  except:
      print("Bollocks, does that look like a number fam?")
  else:
      print("yo fam!!")
  finally:
    print('whatevs')

# checkNum('34')

def divide(a, b):
  try:
      result = a/b
  except (ZeroDivisionError, TypeError) as err:
      print("Something went wrong")
      print(err)
  else:
    print(f"{a} divided by {b} is {result}")

# divide(2, '7')


## pdb
def add_nums(a,b,c,d):
  import pdb; pdb.set_trace()

  return a + b + c + d

# print(add_nums(1,2,3,4))

def divide(a,b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total
