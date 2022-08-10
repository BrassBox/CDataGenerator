# Creates and returns a dict containing an address
import json
from generators import fake


def generate_ext(path, **kwargs):
    # TEMP: ignore and override path
    path = "./rules/misc/ext.json"

    # Open and load json file
    with open(path, "r") as file:
        data = json.load(file)
        return generate_ext_map(data, **kwargs)


def generate_ext_map(data, **kwargs):
    data['device'] = {
        "id": fake.pystr(min_chars=5, max_chars=10),
        "ip": fake.ipv4(),
        "fingerprint": fake.pystr(min_chars=5, max_chars=10)
    }
    data['client'] = {
        "app": fake.pystr(min_chars=5, max_chars=10),
        "version": fake.pystr(min_chars=5, max_chars=10)
    }
    data['transaction'] = {
        "cash_receipt": fake.pystr(min_chars=5, max_chars=10),
        "registration_number": fake.pystr(min_chars=5, max_chars=10)
    }

    return data
