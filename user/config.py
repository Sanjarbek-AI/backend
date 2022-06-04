import base64

# from decouple import config
from django.conf import settings


class Config:
    URL = settings.API_URL
    PREFIX = settings.PREFIX
    DEFAULT_ORIGINATOR = settings.ORIGINATOR
    ORIGINATOR = '3700' if DEFAULT_ORIGINATOR == '' else DEFAULT_ORIGINATOR
    LOGIN = settings.LOGIN
    PASSWORD = settings.PASSWORD

    def __init__(self):
        self.HEADER = self.header()

    def header(self):
        data = '{}:{}'.format(self.LOGIN, self.PASSWORD)
        encoded = base64.b64encode(data.encode('utf-8'))
        header = {'Authorization': 'Basic {}'.format(str(encoded, 'utf-8'))}
        return header
