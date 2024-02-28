from abc import abstractmethod, ABC
import matplotlib.pyplot as plt


class Post():
    def __init__(self, user):
        self.user = user

    @abstractmethod
    def like(self, user):
        if self.user != user:
            print(f"notification to {self.user.username}: {user.username} liked your post")
            self.user.receivedPost.append(f"{user.username} liked your post")
            # self.update(self, user, "like")

    @abstractmethod
    def comment(self, user, contentOfComment):
        print(f"notification to {self.user.username}: {user.username} commented on your post: {contentOfComment}")
        self.user.receivedPost.append(f"{user.username} commented on your post")
        # self.update(self, user, "comment")

    @abstractmethod
    def print_data(self):
        pass


class PostFactory:
    @staticmethod
    def create_post(user, post_type, *args):
        if post_type == "Text":
            return TextPost(user, post_type, *args)
        elif post_type == "Image":
            return ImagePost(user, post_type, *args)
        elif post_type == "Sale":
            return SalePost(user, post_type, *args)


class ImagePost(Post, ABC):
    def __init__(self, image, imageFile, user, matplotlib=None):
        super().__init__(user)
        self.image = "Image"
        self.imageFile = matplotlib.imread(imageFile)

    def display(self):
        plt.imshow(self.imageFile)
        plt.title(self.image)
        plt.axis('off')  # Hide axis
        plt.show()

    def __str__(self):
        return f"Image: {self.imageFile}"


class SalePost(Post, ABC):
    def __init__(self, user, sale, product, cost, location):
        super().__init__(user)
        self.sale = "For sale!"
        self.product = product
        self.cost = cost
        self.location = location

        print(f"{self.user.username} posted a product for sale:")
        print(f"{self.sale} {self.product}, price: {self.cost}, pickup from: {self.location}")

    def __str__(self):
        return f"{self.user.username} posted a product for sale:\n{self.sale} {self.product}, price: {self.cost}, pickup from: {self.location}"

    def discount(self, priceOfDiscount, password):
        if password == self.user.password:
            self.cost *= ((100 - priceOfDiscount) / 100)
            print(f"Discount on {self.user.username} product! the new price is: {self.cost}")

    def sold(self, password):
        if password == self.user.password:
            print(f"{self.user.username}'s product is sold")
            self.sale = "Sold!"


class TextPost(Post, ABC):
    def __init__(self, user, text, contentOfText):
        super().__init__(user)
        self.text = "Text"
        self.contentOfText = contentOfText

        print(f"{self.user.username} published a post:\n\"{self.contentOfText}\"")

    def __str__(self):
        return f"{self.user.username} published a post:\n\"{self.contentOfText}\""
