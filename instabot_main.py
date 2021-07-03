from instabot import Bot
import os
import shutil


dir = "config"
remove_me = "C:\pycharm projects\pics\{}.REMOVE_ME"
# checking whether config folder exists or not
if os.path.exists(dir):
    try:
            # removing it so we can upload new image
            shutil.rmtree(dir)
    except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
if os.path.exists(remove_me):
        src = os.path.realpath("C:\pycharm projects\pics")
        os.rename(remove_me, src)



bot = Bot()

bot.login(username="usr", password="pwd")
bot.upload_photo("C:/pycharm projects/pics/_MG_0266.jpg", caption="Cool bird pose")



