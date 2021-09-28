# custom for loop

def my_for(iterable, func):
  iterator = iter(iterable)
  while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    else:
      func(item)
# my_for('hello', print)