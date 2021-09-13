import requests
import logging
from logging.config import dictConfig

from .settings import Settings
from .logconfig import LogConfig


dictConfig(LogConfig().dict())
logger = logging.getLogger("logger")

settings = Settings()


class ApiNumber():

    api = settings.API_EXTRACT
    page = 1
    array_numbers = []

    def get_numbers(self, page=1):
        response = requests.get(f'{self.api}/numbers?page={page}')

        if response.status_code == 200 and response.json()['numbers']:
            self.page += 1
            self.array_numbers += response.json()['numbers']
            self.get_numbers(page=self.page)
        else:
            logger.info(
                'Finished ApiNumber -> Response Code: {0}'.format(
                    response.status_code
                    )
                )
