file = open('story.txt')

file.read()
file.seek(0)
file.readline()
file.readlines()
file.closed
file.close()

# with
with open('story.txt') as file:
  data = file.read()