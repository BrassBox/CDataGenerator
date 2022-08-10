# Creates and returns a dict containing an address
import json
from generators import fake

# Generate address given template
# Currently ignored and uses generic address
from generators.address import generate_address_map


def generate_payment(path, vendor):

    # Open and load json file
    with open(path, "r") as file:
        data = json.load(file)

        return generate_payment_map(data, vendor)


def generate_payment_map(data, vendor):
    data['method'] = fake.random_element(data['method'][vendor])

    data['indicator'] = fake.pystr(min_chars=5, max_chars=10)

    data['request_token'] = fake.pybool()

    data['token'] = fake.pystr(min_chars=5, max_chars=10)

    data['nonce'] = fake.pystr(min_chars=5, max_chars=10)

    data['timeout'] = fake.pyint(min_value=1, max_value=100) \
        if any(method == data['method'] for method in data['timeout']['required']) \
        else fake.pyint(min_value=0, max_value=100)

    # Can do multiple types via random_choices (unique)
    data['client'] = [fake.random_element(data['client']['items']['enum'])]

    data['data']['pan'] = fake.credit_card_number()

    data['data']['first_name'] = fake.first_name()

    data['data']['last_name'] = fake.last_name()

    data['data']['expiry'] = fake.credit_card_expire()

    data['data']['cvv'] = fake.credit_card_security_code()

    generate_address_map(data['billing_address'])

    data['3ds'] = {
        "indicator": fake.pystr(min_chars=5, max_chars=10),
        "id": fake.pystr(min_chars=5, max_chars=10),
        "authentication": fake.pystr(min_chars=5, max_chars=10),
        "server": fake.pystr(min_chars=5, max_chars=10),
        "version": fake.pystr(min_chars=5, max_chars=10)
    }

    data['cof'] = {
        "indicator": fake.pystr(min_chars=5, max_chars=10),
        "id": fake.pystr(min_chars=5, max_chars=10),
        "request": fake.pybool()
    }

    # Assumed True else fails request
    data['check'] = {"cvv": True, "avs": True}

    return data
