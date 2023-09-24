import requests
import allure


class Api:
    _TIMEOUT = 10

    def __init__(self):
        self.response = None

    @allure.step("Отправка запроса Post")
    def post(self, url, endpoint, params: None, json_body):
        self.response = requests.post(url=f"{url}{endpoint}",
                                      params=params,
                                      json=json_body,
                                      timeout=self._TIMEOUT)
        return self
