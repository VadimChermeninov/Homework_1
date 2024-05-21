from Models.post import Post
class Storage:
    def __init__(self):
        self.dict = {}
        self.id = 0
    def create_post(self, post:Post):
        self.id += 1
        self.dict[self.id] = post
        return str(self.id)
    def read_post(self, post_id:str):
        if post_id in self.dict:
            return self.dict[post_id]
        else:
            print("No such post")
    def delete_post(self, post_id:str):
        if post_id in self.dict:
            del self.dict[post_id]
        else:
            print("No such post")