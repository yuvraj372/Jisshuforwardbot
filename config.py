# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "26583504")
    API_HASH = environ.get("API_HASH", "ef9d71b20a1a32669edd7cb458535fae")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7823841864:AAEk0r-97SxwQlHNa8RBgcQyAuHFSORP1sA") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6471106079').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "Forward6336bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Forwardbot:yuvraj178@forwardbot.xnamt.mongodb.net/?retryWrites=true&w=majority&appName=Forwardbot")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forwardbot")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002399867259'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1002304371242") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
