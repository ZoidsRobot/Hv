# (©)Codexbotz
# Recode by @kang_culiknee


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6054460716:AAF0QMTcE_Kv3iHwLC_F4RJXnmdUZHcpsG8")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "11698078"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "cdab9ff055e4eb433fc4bd771d143298")

# ID Channel Databas
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001610757631"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1245451624"))

# NAMA OWNER
OWNER = os.environ.get("OWNER","gkushskap")

# Databasenya 
DB_URI = os.environ.get("DATABASE_URL", "postgres://awxqnloq:A871j1eJ9OHBUwyb00babO3uw3HWd_Dj@castor.db.elephantsql.com/awxqnloq")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "vvslh_pro")
GROUP = os.environ.get("GROUP", "vvslh_pro")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL","-1001700029476"))

FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001733281482"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>JOIN VVIP MURAH DAN TERPERCAYA DI @testivipexo.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "2119055068 5589797950 1245451624 2110216783").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nJOIN VVIP MURAH DAN TERPERCAYA DI @testivipexo</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", True) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(5396158379)
ADMINS.append(1996472517)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
