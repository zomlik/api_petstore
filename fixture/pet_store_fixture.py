import pytest
from api.pet_store_user import PetStoreUser


@pytest.fixture(scope="function")
def pet_store_user() -> PetStoreUser:
    """Коннект к api petStoreUser"""
    return PetStoreUser()

