from dataclasses import dataclass, asdict


@dataclass
class RequestCreateUserModel:
    """Класс для параметров rquest"""
    id: int
    name: str

    def to_dict(self):
        """преобразование в dict для отправки body"""
        return asdict(self)


class ResponseCreateUserModel:
    pass
