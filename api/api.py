import requests
import allure


class Api:
    _TIMEOUT = 10

    def __init__(self):
        self.response = None

    # METOD
    @allure.step("Отправка запроса GET")
    def get(self, url: str, endpoint: str):
        with allure.step(f"Get запрос на:{url}{endpoint}"):
            self.response = requests.get(url=f"{url}{endpoint}",
                                         timeout=self._TIMEOUT)
        return self

    @allure.step("Отправка запроса POST")
    def post(self, url: str, endpoint: str, params: dict = None, json_body: dict = None):
        with allure.step(f"Post запрос на:{url}{endpoint}"
                         f"\nТело запроса:\n {json_body}"):
            self.response = requests.post(url=f"{url}{endpoint}",
                                          params=params,
                                          json=json_body,
                                          timeout=self._TIMEOUT)
        return self

    @allure.step("Отправка запроса PUT")
    def put(self, url: str, endpoint: str, params: dict = None, json_body: dict = None):
        with allure.step(f"PUT запрос на:{url}{endpoint}"):
            self.response = requests.put(url=f"{url}{endpoint}",
                                         params=params,
                                         json=json_body,
                                         timeout=self._TIMEOUT)
        return self
