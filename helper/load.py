from importlib import import_module


def load_json_schema(path: str, json_shema: str = "schema"):
    modul = import_module(f"shema.{path}")
    return getattr(modul, json_shema)


def load_data(path: str, test_data: str = "data"):
    modul = import_module(f"shema.{path}")
    return getattr(modul, test_data)
