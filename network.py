from user import User

'''
I added an error alert that will pop up to the user in the sign_up function.
It will be written to the user what errors he made:
"There is already such a username on the network"
or
"The password is not the right length"
'''


class SocialNetwork:
    __instance = None
    __is_initialized = False

    def __new__(cls, name: str):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name: str):
        if self.__is_initialized:
            return
        self.name = name
        self.users = dict()
        self.__is_initialized = True
        print(f"The social network" + " " + self.name + " " + "was created!")

    def __str__(self):
        result = f"{self.name} social network:\n"
        for user in self.users.values():
            result += str(user) + "\n"
        return result

    def sign_up(self, username, password):
        if username not in self.users:
            if 4 <= len(password) & len(password) <= 8:
                new_user = User(username, password, True)
                self.users[new_user.username] = new_user
                return new_user
            else:
                raise ValueError("Password length should be between 4 and 8 characters")
        else:
            raise ValueError(f"Username {username} is already in use")

    def log_out(self, username):
        if username in self.users:
            self.users[username].connect = False
        print(f"{username} disconnected")

    def log_in(self, username, password):
        if username in self.users and self.users[username].password == password:
            self.users[username].connect = True
        print(f"{username} connected")


network = SocialNetwork("Twitter")
print()

# Creating users
u1 = network.sign_up("Alice", "pass1")
u2 = network.sign_up("Bob", "pass2")
u3 = network.sign_up("Charlie", "pass3")
u4 = network.sign_up("David", "pass4")
u5 = network.sign_up("Eve", "pass5")

# Creating followers
u1.follow(u2)
u1.follow(u5)
u2.follow(u5)
u2.follow(u1)
u3.follow(u1)
u3.follow(u2)
u4.follow(u3)
u4.follow(u1)
u5.follow(u2)
u5.follow(u4)
print()

# Creating text post
p1 = u1.publish_post("Text", "In 1492, Christopher Columbus set sail,\n"
                             "hoping to find a westward route to Asia, but instead,\n"
                             "he discovered the Americas, changing the course of history forever.")
# Creating image post
p2 = u4.publish_post("Image", 'image1.jpg')

# Creating sale post
p3 = u3.publish_post("Sale", "Toyota prius 2012", 42000, "Haifa")

# Creating likes and comments
p2.like(u4)
p1.like(u4)
p1.like(u2)
p1.comment(u3, "Columbus's bold journey!")
p2.comment(u1, "So beautiful!")
p2.like(u1)
p2.like(u2)
p2.like(u5)
p1.comment(u5, "A pivotal moment")
p3.comment(u2, "Exorbitant price")
print()

# Price reduction of the product for sale
p3.discount(10, "pass3")
print()

# more likes and comments
p3.like(u2)
p3.comment(u2, "Can you give me your phone number?")
p3.comment(u4, "+97255576433")
print()

# Defining the product as sold
p3.sold("pass3")
print()

print(p3)

# Displaying the image of the post
p2.display()
print()

p2.comment(u5, "Amazing picture!")
print()

# Using unfollow
u2.unfollow(u1)
u3.unfollow(u2)
print()

# Using log_in & log_out
network.log_out("Charlie")
network.log_in("Charlie", "pass3")
print()

# User printing
print(u1)
print()

# Post printing
print(p1)
print(p2)

# Printing all notifications received by a certain user
u4.print_notifications()
print()

# Network printing
print(network, end='')
