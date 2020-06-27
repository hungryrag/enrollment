import os


class Config(object):
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or b"\x97\xcc\x91\x9f\xd9\xb0b\xe8\xff0[\x98\xd3}+,"
    )

    MONGODB_SETTINGS = {"db": "UTA_Enrollment"}
