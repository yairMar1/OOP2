from abc import ABC, abstractmethod
from Post import PostFactory


class Sender(ABC):
    def __init__(self):
        self.whoFollowMe = set()  # Initialize as an empty set

    def notify(self, message):
        for member in self.whoFollowMe:
            member.update(message)


class Member(ABC):
    @abstractmethod
    def update(self, message):
        pass


class User(Sender, Member):
    def __init__(self, username, password, connect: bool = True, numberOfPost=0):
        super().__init__()
        self.username = username
        self.password = password
        self.connect = connect
        # self.whoFollowMe = set()   # Initialize as an empty set
        self.receivedPost = []  # Initialize as an empty list # username:Post/like/comment
        self.numberOfPost = numberOfPost

    def __str__(self):
        return f"User name: {self.username}, Number of posts: {self.numberOfPost}, Number of followers: {len(self.whoFollowMe)}"

    def follow(self, user):
        # if self.username not in user.whoFollowMe:
        user.whoFollowMe.add(self)  # added the name of the user who follows you to the list
        print(f"{self.username} started following {user.username}")

    def unfollow(self, user):
        if self in user.whoFollowMe:
            user.whoFollowMe.remove(self)  # removed the name of the user who follows you to the list
            print(f"{self.username} unfollowed {user.username}")

    def publish_post(self, post_type, *args):
        # for i in self.whoFollowMe:
        #     i.receivedPost.append(f"{self.username} has a new post")
        self.notify(message=f"{self.username} has a new post")
        self.numberOfPost += 1
        return PostFactory.create_post(self, post_type, *args)

    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for i in self.receivedPost:
            print(i)

    def update(self, message):
        self.receivedPost.append(message)
