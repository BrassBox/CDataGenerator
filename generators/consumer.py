# Creates and returns a dict containing an address
import json
from generators import fake


def generate_consumer(path, **kwargs):
    # TEMP: ignore and override path
    path = "./rules/consumer/consumer.json"

    # Open and load json file
    with open(path, "r") as file:
        data = json.load(file)
        return generate_consumer_map(data)


def generate_consumer_map(data, **kwargs):
    data['reference'] = ''  # Don't know what for yet

    data['first_name'] = fake.first_name()
    data['last_name'] = fake.last_name()

    # TODO: make sure number is valid US Number, if only doing US
    data['phone'] = fake.phone_number()

    # TODO: config safe_mode
    data['email'] = data['first_name'].lower() + str(fake.pyint()) + '@' + fake.free_email_domain()

    data['ext_data']['document_id'] = ''
    data['ext_data']['eft_code'] = ''

    return data
