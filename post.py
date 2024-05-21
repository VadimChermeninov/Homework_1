from Models.user import User
class Post:
    def __init__(self, author: User, body:str):
        self.author = author
        self.body =body