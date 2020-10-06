# class User:
#     active_users = 0

#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         User.active_users += 1

#     def full_name(self):
#         return f"{self.first} {self.last}"

#     def initials(self):
#         return f"{self.first[0]}.{self.last[0]}."

#     def likes(self, thing):
#         return f"{self.first} likes {thing}"

#     def is_senior(self):
#         return self.age >= 65

#     def birthday(self):
#         self.age += 1
#         return f"Happy {self.age}th birthday {self.first}"

# print(User.active_users)
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.active_users)
# print(user1.full_name())



#example of class method

class User:
    active_users = 0

    @classmethod
    def display_active_user(cls):
        return f"There are currently {cls.active_users} active users"
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday {self.first}"

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.display_active_user())
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.display_active_user())