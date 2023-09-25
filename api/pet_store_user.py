import allure
from api.api import Api
from model.create_user_model import RequestCreateUserModel


class PetStoreUser(Api):
    _URL = "https://petstore.swagger.io/v2"
    _ENDPOINT = "/pet"
    
    @allure.step("Запрос по user id")
    def pet_store_get(self, user_id: str):
        return self.get(url=self._URL, endpoint=self._ENDPOINT + str(user_id))

    @allure.step("Запрос на создания петомца")
    def pet_store_create(self, param_request_body: RequestCreateUserModel):
        return self.post(url=self._URL,
                         endpoint=self._ENDPOINT,
                         json_body=param_request_body.to_dict())

