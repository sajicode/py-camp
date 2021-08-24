## lambdas
square = lambda num: num * num
# print(square(2))

## maps
nums = [2, 4, 6, 8, 10]
doubles = map(lambda x: x * 2, nums)

# print(list(doubles))

names = [
  {'first': 'Rusty', 'last': 'Steele'},
  {'first': 'Colt', 'last': 'Steele'},
  {'first': 'Ruby', 'last': 'Steele'},
]

firsts = map(lambda name: name['first'], names);
# print(list(firsts))

## filter
all_names = ['leonard', 'penny', 'sheldon', 'raj',  'howard', 'bernadette', 'amy']

three_letters = filter(lambda name: len(name) == 3, all_names)
# print(list(three_letters))

## filter & map
users = [
  {"username": "raj", "tweets": ["Hail India", "Oh my cinnamon"]},
  {"username": "penny", "tweets": ["Acting is divine"]},
  {"username": "sheldon", "tweets": []},
  {"username": "amy", "tweets": []},
  {"username": "leonard", "tweets": ["Sheldon!!", "Oh Penny!", "Why mum"]},
  {"username": "howard", "tweets": ["I've been to space!!"]},
  {"username": "bernadette", "tweets": []},
]

inactive_users = list(map(lambda profile: profile['username'], list(filter(lambda user: not user['tweets'], users))))

## with list comprehension
# print([user['username'] for user in users if not user['tweets']])

# print(inactive_users)

def remove_negatives(nums):
    return list(filter(lambda num: num >= 0, nums))

# print(remove_negatives([-1, 3, 4, -99]))

## all
people = ['Ted', 'Marshall', 'Lily', 'Barney', 'Robin']

# returns true if all match the condition 
# print(all(name[0] == 'B' for name in people))
# returns true if at least one matches the condition
# print(any(name[0] == 'B' for name in people))

def is_all_strings(letters):
    return all(type(l) == str for l in letters)

# print(is_all_strings(['a', 'b', 2]))

## sorted
num_list = [4,6,1,30,55,23]

# print(sorted(num_list))
# print(sorted(num_list, reverse=True))

# sort alphabetically by username
# print(sorted(users, key=lambda user: user['username']))

# sort by length of tweets
# print(sorted(users, key=lambda user: len(user['tweets']), reverse=True))

stark_names = ['Arya', 'Sansa', 'Brandon', 'Rob']

# print min length
# print(min(len(name) for name in  stark_names))

# prrint length of each name
# print([len(name) for name in stark_names])

# print longest name
# print(max(stark_names, key=lambda name:len(name)))

songs = [
  {"title": "happy birthday", "playcount": 1},
  {"title": "survive", "playcount": 6},
  {"title": "ymca", "playcount": 99},
  {"title": "toxic", "playcount": 31},
]

# find song with least number of plays
# print(min(songs, key=lambda song:song['playcount'])['title'])

## reversed
# print(''.join(list(reversed('hello'))))

def max_magnitude(nums):
    return max(abs(num) for num in nums)

# print(max_magnitude([200, 300,-900]))

## zip
first_zip = zip([1,2,3], [4,5,6])

# print(list(first_zip))
# print(dict(first_zip))

# get higher score for each student
midterms = [80,91,78]
finals = [98,89,57]
students = ['joel', 'ellie', 'tommy']

final_grades =  [max(pair) for pair in zip(midterms, finals)]

final_scores = dict(zip(students, final_grades))
# print(final_scores)

# interleave('aaa', 'zzz') => 'azazaz'
def interleave(str1, str2):
  # str_tups = list(zip(list(str1), list(str2)))
  # return ''.join([''.join(item) for item in str_tups])

  # or
  return ''.join(''.join(x) for x in (zip(str1,str2)))

# print(interleave('lzr', 'iad'))

def triple_and_filter(nums):
  return list(map(lambda num: num * 3, list(filter(lambda num: num % 4 == 0, nums))))


# print(triple_and_filter([1,2,3,4]))

def extract_full_name(names):
  return [name['first'] + ' ' + name['last'] for name in names]

print(extract_full_name([{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]))