from user import User


class Network:
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
            if 4 <= len(password) <= 8:
                new_user = User(username, password, True)
                self.users[new_user.username] = new_user
                return new_user

    def log_out(self, username):
        if username in self.users:
            self.users[username].connect = False
        print(f"{username} disconnected")

    def log_in(self, username, password):
        if username in self.users and self.users[username].password == password:
            self.users[username].connect = True
        print(f"{username} connected")


# network = Network("Twitter")
#
# u1 = network.sing_up("yair", "0123")
# u2 = network.sing_up("orel", "4567")
# u3 = network.sing_up("shira", "8741")
# u4 = network.sing_up("yael", "3264")
#
# u1.follow(u2)
# u3.follow(u2)
# u4.follow(u2)
# u1.follow(u3)
#
# print(list(u2.whoFollowMe))
# u1.unfollow(u2)
# print(list(u2.whoFollowMe))
#
# # print(network)
#
# print(u1)
# print(u2)
# print(u3)
# print(u4)
#
# network.log_out("shira")
# print()
# print(u3)
# network.log_in("shira", "8741")
# print(u3)
# print()
# p1 = u3.publish_post("Text", "In 1492, Christopher Columbus set sail,""\n"
#                              "hoping to find a westward route to Asia, but instead,\n"
#                              "he discovered the Americas, changing the course of history forever.")
#
# p3 = u3.publish_post("Sale", "Toyota prius 2012", 42000, "Haifa")
# print()
# p3.discount(10, "8741")
# print()
# print(p3)
# p3.sold("8741")
# print()
# print(p3)
# print()
# p1.like(u3)
# p1.like(u4)
# p1.like(u1)
# print()
# p1.comment(u1, "Columbus's bold journey!")
# p3.comment(u1, "So beautiful!")
# print()
# u3.print_notifications()
# print()
# u1.print_notifications()
# print()
# u2.print_notifications()
# print()
# u4.print_notifications()
# print()
# print(network, end='')

network = Network("Twitter")
print()

u1 = network.sign_up("Alice", "pass1")
u2 = network.sign_up("Bob", "pass2")
u3 = network.sign_up("Charlie", "pass3")
u4 = network.sign_up("David", "pass4")
u5 = network.sign_up("Eve", "pass5")

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

p1 = u1.publish_post("Text", "In 1492, Christopher Columbus set sail,\n"
                                 "hoping to find a westward route to Asia, but instead,\n"
                                 "he discovered the Americas, changing the course of history forever.")
print()

#p2 = u4.publish_post("Image", 'image1.jpg')

print()

p3 = u3.publish_post("Sale", "Toyota prius 2012", 42000, "Haifa")
print()

#p2.like(u4)
p1.like(u4)
p1.like(u2)
p1.comment(u3, "Columbus's bold journey!")
#p2.comment(u1, "So beautiful!")
#p2.like(u1)
#p2.like(u2)
#p2.like(u5)
p1.comment(u5, "A pivotal moment")
p3.comment(u2, "Exorbitant price")
print()

p3.discount(10, "pass3")
print()

p3.like(u2)
p3.comment(u2, "Can you give me your phone number?")
p3.comment(u4, "+97255576433")
print()

p3.sold("pass3")
print()

print(p3)

#p2.display()
print()

#p2.comment(u5, "Amazing picture!")
print()

u2.unfollow(u1)
u3.unfollow(u2)
print()

network.log_out("Charlie")
network.log_in("Charlie", "pass3")
print()

print(u1)
print()

print(p1)
#print(p2)
print()
u4.print_notifications()
print()

print(network, end='')

