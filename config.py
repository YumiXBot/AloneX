import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "23531711"))
API_HASH = getenv("API_HASH" "65780e80712347f6b824a0666f040d79",)

BOT_TOKEN = getenv("BOT_TOKEN", "5824606541:AAFu5wYG0NfDkF5d0DtZ26DvmSHoyPgGvVg")
 
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "1000")
)

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001603822916"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "ᴧŁꪮɳᴇ ꭙ")

OWNER_ID = list(
    map(int, getenv("OWNER_ID", "6079943111").split())
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/YumiXBot/AloneX")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/AloneXBots")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/AlonesHeaven")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400")
)

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

SET_CMDS = getenv("SET_CMDS", True)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/TeamAloneOp/AloneX/fork")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "315d8e2d77b74ad3ad99547238f56ee8")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2b82b996eb2c4161b21119b82700d67a")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "10")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQAYRIV3qXq3m1FAxBMdztIUOHwwDExkepJ-qFAAyz0lbUs48jpsmSaGBepzasm4Z6tfl80Ha0jE1E_dhFqWweeZXUxTAX5AInJGHXOM-8Xl_zXl8mlTNH3Wib-4EzTvjTl-sYkge31FqdIRhilty7w76NTxz0ytIM6-0X3DYY4BMwo9bENx4nr_rLHUidlJDRfPxq8Txigzao1lJBtpc1Vng7HU0iqWkYmNe9cNjHLAMXJGsokmAWxLVKgcVhxXLZn5W6Ash1QFVSgrYAu8ZhdbXhdMlbfeL7JqfegLYQk8gQQ1h0xRsj0aagT2NyoVvnpjuXmtlperbwqO_5tNRSFlasK9dAA")
STRING2 = getenv("STRING_SESSION2", "BQDCOPgeUReF0HwCz6fMErWe1fi4sacDU80Lmz3dq6tr3-EX7WiEZLl4LuYxSeoji_UrPnMJ7p7qLHqhTr7cG_McwY3khAmLtCbbalEQ8dYLh3uGNg7ha9iIyyFJihHfvVJuj7Yo023LbLVx0Y03hQ7Z2LeDRTiHcy5I0eCqZJnpKrqyK8XeHmJHeL93ybIEvjqxdILpPYqdTIeyAH6WkTnNobxTV0PQ9A0RrDGgPPtgVYibBp1onA5CSj3BSH-SDtUDhmy1TUQmxnds7EIuGpALrO0jR7dhRIswamr9znzBRuiaXZJ-b9Gkjt0R7sZziQHZdSHpbY7ZdZnaAAx1eMxTAAAAAW8fDwQA")
STRING3 = getenv("STRING_SESSION3", "BQDE7lb5HBwKXmn_ZsJDkYw-FmLKyiM6YPK5jdpjCOLYwhjy0NliV37D5CuL1UyeOF8Xu66twwCd8VkbqpsPt78xqsKJVApQTgwbFautRSmPURuZPRlCgQZg56dsF4mqIxj6uKBnaCsReGNmXJm3gl6o_1rkkzbH2-LjAn2u1HWdU8s8RyGSZCwkGxXufIBSmlQnKNu_isZEWTigpiNwCPYETz7kaufrb5Q1BxXqqFcAwuwmX3MTPetTi6XTRl7buPyVvIghH0dh3Xit0U6aFVhmWdFniU90kKWVUflUuRGgQdUhMaQ11vofCUbaHAu9NnrbWWQ2qQCKxlNyl7o-Lt2vAAAAAVsVsXEA")
STRING4 = getenv("STRING_SESSION4", "BQBGGIA7PckZ-ZjTFPJoXdp8FQlgfxzWICurX77JLe9NRqN9h-68A3GjWh9yMrHYFnyFDNHbdGlcL06E7ByUpmM4-JjNuLrvkDAJrAOAUwU7SX4Fw86o5H8CF46Vr-6CBc_frMyhjhsj9nyOj43rBNfcEWrRg_CtoBFdOxAAx7WJYhjWs7Eu1Y1GQpksFjMZOwTgeeQ0kaKz4sHPAjBf_DwdJ6BkivMaAkuYwYDrrEAOHPCNiGXcaZBqp68-6zjO7aRqmVsPZAMdcPJUR2MeBtHSKxm00OjcDNPtqVOcI_-bl9SARzfEF0A9pHHozGmszD1kXp6ErwRk-b-65A8cCEAAAAAVNeIMAA")
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "ᴀʟᴏɴᴇ log.txt"
adminlist = {}
lyrical = {}
DEV = 6045293810
chatstats = {}
userstats = {}
clean = {}
votemode = {}
autoclean = []
confirmer = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/b15c198fb79ce6e71c5b0.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/eee5e3d03dbfcf6514595.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://te.legra.ph/file/c5ae7505b832353b2dbfc.jpg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://te.legra.ph/file/df481726bdfafdbc7d85c.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://te.legra.ph/file/df481726bdfafdbc7d85c.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://te.legra.ph/file/a44ac871100a1aabb360f.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://te.legra.ph/file/a44ac871100a1aabb360f.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://te.legra.ph/file/a44ac871100a1aabb360f.jpg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://te.legra.ph/file/a44ac871100a1aabb360f.jpg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://te.legra.ph/file/389f11da55c1c1a60a215.jpg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://te.legra.ph/file/a44ac871100a1aabb360f.jpg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://te.legra.ph/file/a44ac871100a1aabb360f.jpg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://te.legra.ph/file/a44ac871100a1aabb360f.jpg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "AloneX/assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "AloneX/assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "AloneX/assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "AloneX/assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "AloneX/assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "AloneX/assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "AloneX/assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "AloneX/assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "AloneX/assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if not MUSIC_BOT_NAME.isascii():
    print(
        "[KYA RE LAVDE] - BOHOT FONT LAGANE KA SHAUKH HAI. JAA PHIR IRO KO APNI CHUMT DEKE AA"
    )
