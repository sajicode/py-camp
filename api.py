from termcolor import colored
import requests

url = "https://icanhazdadjoke.com/search"

print(colored("Dad Joke 3000", color="magenta"))

term = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(url, headers={"Accept": "application/json"}, params={"term": term})

data = response.json()

results = data['results']

results_length = len(results)

if results_length == 1:
  print(f"I've got one jokes about {term}. Here it is:\n {results[0]['joke']}")
elif results_length > 1:
  print(f"I've got {results_length} jokes about {term}. Here's one: \n {results[1]['joke']}")
else:
  print(f"Sorry, I don't have any jokes about {term}! Please try another term")
