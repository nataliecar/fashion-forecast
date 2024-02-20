from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader

L = instaloader.Instaloader()
L.interactive_login('natalierc_') 
print('hello1')
posts = instaloader.Profile.from_username(L.context, "voguemagazine").get_posts()
print('hello2')

SINCE = datetime(2023, 1, 1)
UNTIL = datetime(2024, 1, 1)

print('started')
for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
    print(post.date)
    L.download_post(post, "voguemagazine")