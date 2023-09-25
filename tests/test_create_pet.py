import allure
import pytest
from helper.load import load_data

pytest_plugins = ["fixture.pet_store_fixture"]
pytestmark = [allure.parent_suite("petStore"), allure.suite("create_pet")]


@allure.step("Запрос на создание петомца")
@pytest.mark.parametrize('test', load_data("create_pet_data", "data"))
def test_pet_create(pet_store_user, test):
    pet_store_user.pet_store_create(test).status_code_should_be(200)

