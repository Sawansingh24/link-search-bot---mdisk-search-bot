import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 16445683))
    API_HASH = os.environ.get("API_HASH", "d0852e13eee2389ff2d9183b00649547")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5824194422:AAElt9rqqxGu86kZNvHLqRmx6A9oKkUTRsg")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQCB5l57jOha9pZQGoPa1oSZ-Hz9GkB0tSLFLvOiDzdd-0lGzIGoipa9YA7LE9zKqCgykHl7L0ZxKH6dlTKHjARpByLBwbKcD8c74mThXY1ZsDRo89yYiDvydofFI8xi4F0vK7ia5bVjlmeO_NBnMBLiD5loNLn-UI684AYUHzLyUFWe7xmapTdJJ32M_OXir-WCgOGFPxNm63a5VhvGxDYoa7C1FJGAGsxkHfsENI-Uix5zAp-8iMoyeF3ntD0XAOCTO6gVdUtvOf5HW1_D4uV3XCXnosbA69qaMW1QmJZIcQajniSvr7fj7YUh4UoEEzvoAErwaNzC_W3gIM-dB1AKAAAAAU7MTqgA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001846372477"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Cw_search_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5628615681"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Sawansingh24:Sawansingh24@cluster0.uiuhxxj.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001889508148")
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://youtube.com/@GreyMattersBot'>Link Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""

