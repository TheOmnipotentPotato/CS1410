from post import Post
from instagram import Instagram_Post
from tiktok import Tiktok_Post


if __name__ == "__main__":
    old_tweet = Post("Hello, World!")
    print(old_tweet)

    print('-'*10)

    insta_post = Instagram_Post("Las Vegas Trip '23", "MGM Grand.heic")
    print(insta_post)

    print('*'*10)
    
    tt_post = Tiktok_Post("#FYP #Funny \nLittle Kid Biffs it down Stairs", "Oof.wav", "Little_Man_Falls.mov")
    print(tt_post)
    
