#!/usr/bin/env python
import getpass

import instabot

bot = instabot.Bot(filter_users=False)
bot.login(username=input('Enter Instagram Username: '), password=getpass.getpass())

target = "instagram"
print('This will like all followers of the instagram user "{}"'.format(target))
input('Press CTRL-C to cancel. Any key to continue')
bot.like_followers(target)
