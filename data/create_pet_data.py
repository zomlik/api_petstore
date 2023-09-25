from model.create_user_model import RequestCreateUserModel


# данные для тестов ('request_parameters')
data = (RequestCreateUserModel(id=65, name="Doggi", category={"id": 35, "name": "Jojo"},
                               photourls="HHT", tags=None),

        )
#{"id": 36, "name": "Lol"}