def copy(file_one, copy_file):
  with open(file_one) as file:
    data = file.read()

  with open(copy_file, 'w') as writer:
    writer.write(data)

copy('story.txt', 'story_copy.txt')

def reverse(file_one, reverse_file):
  with open(file_one) as file:
    with open(reverse_file, 'w') as reverser:
      reverser.write(file.read()[::-1])


reverse('story.txt', 'story_rev.txt')

def stats(file_name):
  with open(file_name) as file:
    lines = file.readlines()

  return {
    "lines": len(lines),
    "words": sum(len(line.split(" ") for line in lines)),
    "characters": sum(len(line) for line in lines)
  }

def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()