import requests

from .settings import Settings


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
