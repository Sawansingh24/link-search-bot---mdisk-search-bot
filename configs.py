import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 16445683))
    API_HASH = os.environ.get("API_HASH", "d0852e13eee2389ff2d9183b00649547")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5824194422:AAElt9rqqxGu86kZNvHLqRmx6A9oKkUTRsg")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQCLkj43D1a17zuy0xHSzJDcAxpq3meiuwFhmCNKoV3IhnuOlgY2z_G6dhu_kE5W1d1CJZ54q3cnwwfjoOolX97qklBeDwsWTcMMIWU8DQbMv0IFHWISnWrsCNwWuDeFB9IJYfuKPSnhW1IC221STCqu_mTC3UFyin9P6iaamEgs_fR9Haz7XvQu1R2uQrUQh_OiyezNW2eeb0Ax01UCM1kRQHbQuzvxnFZL8CvbrarQvyYybzKgcfX2FcEYGLBF4bzW_Blx9CO8zGhrzKPv1Mr3EsLQcCdqPXGLOykecaaLHIz4HsGjNKeh7qpukCUxHqg9bUBec8gcN7GyZ9H6yE5TAAAAAVrKRZwA")
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

