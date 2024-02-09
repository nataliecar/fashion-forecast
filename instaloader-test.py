import numpy as np
import pandas as pd
import instaloader
from instaloader import Profile

# Get instance

L = instaloader.Instaloader()
L.interactive_login('natalierc_')

#p = L.download_profiles(profile)

profile = Profile.from_username(L.context, 'voguemagazine')
data = {}
post_arr = np.array()
for post in profile.get_posts():
    post_arr.append(post)
data[profile.username] = post_arr

print(post_arr[0])
#df = pd.DataFrame(profile_arr, columns=['profile_name', ])
