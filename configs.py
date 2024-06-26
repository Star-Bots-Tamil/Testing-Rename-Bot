import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    API_ID = int(os.environ.get("API_ID", "11973721"))
    API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6809904281:AAGdbV-NFrCtnNhwhXoBuXdDJf-evqRUkec")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./Downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 1391556668))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "1391556668 5162208212").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001821439025"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "zM4WB3RxQeIogb")
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "d1cf7f6a67162eacdd77")
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
