import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "27501506"))
    API_HASH = os.environ.get("API_HASH", "30c400c8703260a92bc5ebd00422c903")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BAGjo8IAApnHj2nfaDHgAtFnGAZiQbySwRszECWfhXn9Vi118dkxEgr-rI0ZA8FZL9xXcrf9Jqz6xs1czhNlrtZtYMW1hZYjfqy49BrHjZzvsjBrNqMN4d_kanuSbZAcMPDjmsW9UhB-8W4j4x_2UbBF9u4ZlwvAbWdCfJERxhRTccXvMYU6fQAYeDO1MAOXL-c4HEcY6amfWbx5Y5CxH2Rz3jubyYWS6LKV4NZyuq_aFig77ZRacMosoMp8J7mfseNRLJJxB1q1o_yuSijkj3hZMVtgzAVJATy92BIsdh4RWKm7yUnJmSCxc86GgXgvtyxE_8BFksJcUiAIvwJoRkNQICWk1gAAAAGBOlRxAA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TUFISUN")
    CHANNEL = os.environ.get("CHANNEL", "TUFISUN")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/7c7e961ec6d48c8c3f6e6.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/3d4e9709614892e62a969.jpg")
    OWNER_ID = os.environ.get("OWNER_ID", "")

