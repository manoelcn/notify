import requests
from django.conf import settings


class CallMeBot:

    def __init__(self):
        self.__base_url=settings.CALLMEBOT_BASE_URL
        self.__phone=settings.CALLMEBOT_PHONE
        self.__api_key=settings.CALLMEBOT_API_KEY

    def send_message(self, message):
        response = requests.get(
            url=f'{self.__base_url}?phone={self.__phone}&text={message}&apikey={self.__api_key}'
        )
        return response.text