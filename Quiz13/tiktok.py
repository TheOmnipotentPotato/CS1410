from post import Post

class Tiktok_Post(Post):
    def __init__(self, text: str, video_path: str, audio_path: str):
        super().__init__(text)
        self.mVideo_path = video_path
        self.mAudio_path = audio_path

    def __repr__(self):
        return self.mAudio_path + '\n' + self.mVideo_path + '\n' + self.mText
