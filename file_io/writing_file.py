with open('haiku.txt', 'w') as file:
  file.write('There are 9 million bicycles\n')
  file.write('In Beijing.\n')
  file.write('That\'s a fact\n')


with open('lol.txt', 'w') as file:
  file.write('hahahah who\'s laughing now ' * 1000 )

# append
with open('haiku.txt', 'a') as file:
  file.write('Like the fact that I will love you till I die\n')

with open('haiku.txt', 'r+') as file:
  file.write('I am the genesis\n')

# r+ works only with an existing file
# r+ replaces the text on the line it is entered