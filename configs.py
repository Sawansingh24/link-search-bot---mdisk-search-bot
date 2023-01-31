import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 16445683))
    API_HASH = os.environ.get("API_HASH", "d0852e13eee2389ff2d9183b00649547")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5824194422:AAElt9rqqxGu86kZNvHLqRmx6A9oKkUTRsg")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOKkBuwQyP-TOXJflP5WzX9798ExXs_njb3uszrypVzNkHTR_B2Mb3hMpMp-LbQq36fDUownhDNLiFkCiPLuzvc3cyvH-Nfzhmo2vELwXThmGa8YeiYTZVM7N1fLEjAJPiAJTdww78xdZJe5k0Em_c6hUNF5Ei_qDDTqCXF6YsLvx1QXUYBFpVL9AYqhzSH86K1H22evyah_2fsPvrbA6Lvr5CPILUOaookLGBftNQZhGWX27hGtw_9ePcbKCD87A2Ws7jdgGaqDYIKPRVpomdr4mfqkNXOIseRCghcfFipR0GSHfwft2PFGrsRAMd8eOV5ZRCo1ZygEHdNz0FaqX21u1lB8=")
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

