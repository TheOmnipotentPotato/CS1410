from post import Post

class Instagram_Post(Post):
    def __init__(self, text:str, image_path:str):
        super().__init__(text)
        self.mImage_path = image_path

    def __repr__(self):
        return self.mImage_path + "\n" + self.mText
