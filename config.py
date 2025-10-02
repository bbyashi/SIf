import re
from os import getenv
import config
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "21189715"))

API_HASH = getenv("API_HASH", "988a9111105fd2f0c5e21c2c2449edfd")

BOT_TOKEN = getenv("BOT_TOKEN","7026867682:AAGjBzbfNklXEdh5usx-ykQ8odIY2Q3uEoQ")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ayanosuvii0925:subhichiku123@cluster0.uw8yxkl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", "-1001956979385"))

OWNER_ID = int(getenv("OWNER_ID", 8111174619))

BOT_USERNAME = getenv("BOT_USERNAME" , "sifrababybot")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
VIDEO_API_URL = getenv("VIDEO_API_URL", 'https://api.video.thequickearn.xyz')
API_KEY = getenv("API_KEY", "30DxNexGenBots7fG9kL") # youtube song api key, generate free key or buy paid plan from panel.thequickearn.xyz


UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ayanokozii/Sifra2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Anya")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/acxbots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Friend_Chat_International")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION",  "BQGuP2cAhsHBKCkwsUAEySw3Q-AZ8Tj6gnj3RCle2b5BHbI-LQ_q7lmmk8WEVGHfQPvxWzPATbk5P_feSE9PtiWObVKB2-xhXJWlPrrVA5b0pJ1j17eSD2TomJauwonnqlOqayu7i7jhWQEUFw0faoyfv9NRXVvxYhSBV9DfYI-i1JCK1tTmaPwnYAnym0Bi7K_Ff0QPhFxy2BWX4ssBcpH3cjmqTjiSZofLAYBrRnMOy61RwpOC32v_y5NTClgC942FtN3Y7s87YmOapxM6I7zlpdJRaw_4xab17Y3f7f_LnoNJVG8J7YxkfMjX0L9KOJ2LQeqczWGsDkFatH7KKQ-kZhedGgAAAAFGEz7IAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"
STATS_IMG_URL = "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/81df44f3679946babd8c3.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/81df44f3679946babd8c3.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )


