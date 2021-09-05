class User(object):
    #* class attributes
    active_users = 0

    #* class method
    @classmethod
    def display_active_users(cls):
        return f"There are curretly {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        #* this is like calling User(first, last, age)
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self._secret = "I'm an alien"
        self.__weapons = "katana"
        # increment for every newly created user
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}. {self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def __repr__(self):
        return f"{self.first} is {self.age}"

    def full_name(self):
        return f"{self.first} {self.last}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"

user1 = User("Joe", "Biden", 67)
user2 = User("Walter", "White", 54)
user2 = User("Walter", "White", 36)

# tony = User.from_string('Tony,Stark,45')

class Moderator(User):
    total_mods = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active mods"

    def remove_post(self):
        return f"{self.full_name()} removed a post from {self.community} community"

jasmine = Moderator("Jasmine", "O'Connor", 65, "Beverly Hills")

# print(jasmine.community)


# print(tony.full_name())
# print(tony) after using __repr__

# print(f"{user1.first} {user1.last}")
# print(user2._secret)
# print(user2.full_name())
# _name - internal use in a class
# __name - name mangling
# __name__ -  python specific methods
# print(User.active_users)
# print(User.display_active_users())

class BankAccount():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
        
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

# account = BankAccount('Playboy')

# print(account.owner)
# print(account.balance)
# account.deposit(7)
# print(account.balance)
# account.withdraw(3)
# print(account.balance)

class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return "Fly You fools!!!"


villager  = NPC('Gandalf', 120, 15)

# print(villager.speak())