list_1  = [1,2,3,4]
list_2 = [3,4,5,6]

answer = [n for n in list_1 if n in list_2]

# reverse names in list
names = ["Ellie", "Tim", "Matt"]

answer2 = [val[::-1].lower() for val in names]

numbers = [num for num in range(1, 101) if  num % 12 == 0]

answer = [letter for letter in 'amazing' if letter not in 'aeiou']

# nested list
nested_list = [[1,2,4], [4,5,6], [7,8,9]]

# spread nested list
[[print(val) for val in l] for l in nested_list]

list_ans = [[val for val in range(0,10)] for l in range(0,10)]

print(list_ans)