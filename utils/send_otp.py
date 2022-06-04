import math
import random
import time

import requests
from decouple import config

from user.config import Config

api_url = config('API_URL')
login_sms = config('LOGIN')
password = config('PASSWORD')
prefix = config('PREFIX')
originator = config('ORIGINATOR')

cf = Config()


class generateKey:
    """Class to generate the OTP key"""

    @staticmethod
    def returnValue():
        """Generate and return the OTP key"""

        nums = [i for i in range(0, 10)]
        random_code = str()

        for i in range(6):
            num = math.floor(random.random() * 10)
            random_code += str(nums[num])

        return {"OTP": random_code}


def send_sms(user, otp_key):
    """Function for sending OTP through SMS"""
    user_phone_number = user.phone_number

    data = {
        'messages': [
            {
                'recipient': user_phone_number,
                'message-id': prefix,
                'sms': {
                    'originator': originator,
                    'content': {
                        'text': 'Ваш код активации ' + otp_key + '. Никому не сообщайте этот код.'
                    }
                }
            }
        ]
    }

    response = requests.post(api_url, json=data, headers=cf.header())

    # Time pasted here to measure 2 minute length
    user.time_otp = time.time()
    user.save()
    return response.status_code
