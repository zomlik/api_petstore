import requests
import allure
from helper.load import load_json_schema
from jsonschema import validate


class Api:
    _TIMEOUT = 10

    def __init__(self):
        self.response = None

    # METHODS:
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
        with allure.step(f"PUT запрос на:{url}{endpoint}"
                         f"\nТело запроса:\n {json_body}"):
            self.response = requests.put(url=f"{url}{endpoint}",
                                         params=params,
                                         json=json_body,
                                         timeout=self._TIMEOUT)
        return self

    def path(self, url: str, endpoint: str, params: dict = None, json_body: dict = None):
        pass

    @allure.step("Отправка запросов DELETE")
    def delete(self, url: str, endpoint: str):
        with allure.step(f"DELETE запрос на:{url}{endpoint}"):
            self.response = requests.delete(url=f"{url}{endpoint}",
                                            timeout=self._TIMEOUT)
        return self

    # ASSERTS:
    @allure.step("Статус код {expected_code}")
    def status_code_should_be(self, expected_code):
        actual_code = self.response.status_code
        assert actual_code == expected_code, f"ОР:{expected_code}"\
                                             f"ФР:{actual_code}"
        return self

    @allure.step("Cхема ответа json валидна")
    def json_shema_should_be_valid(self, path_json: str, name_json: str = "schema"):
        json_shema = load_json_schema(path_json, name_json)
        validate(self.response.json(), json_shema)
        return self
