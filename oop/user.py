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

    def __repr__(self):
        return f"{self.first} is {self.age}"

    def full_name(self):
        return f"{self.first} {self.last}"

user1 = User("Joe", "Biden", 67)
user2 = User("Walter", "White", 54)
user2 = User("Walter", "White", 36)

tony = User.from_string('Tony,Stark,45')

print(tony.full_name())
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

account = BankAccount('Playboy')

# print(account.owner)
# print(account.balance)
# account.deposit(7)
# print(account.balance)
# account.withdraw(3)
# print(account.balance)