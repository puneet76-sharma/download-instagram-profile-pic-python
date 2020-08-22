# pip install instaloader

import instaloader as insta

mod= insta.Instaloader()

user= input("Enter the UserName to download profile pic: ")

mod.download_profile(user, profile_pic_only=True)

input()