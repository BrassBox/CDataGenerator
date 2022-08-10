# Creates and returns a dict containing an address
import json
from generators import fake


# Generate address given template
# Currently ignored and uses generic address
def generate_address(path, **kwargs):
    # TEMP: ignore and override path
    path = "./rules/address/address.json"

    # Open and load json file
    with open(path, "r") as file:
        data = json.load(file)
        return generate_address_map(data)


def generate_address_map(data, **kwargs):
    data['street'] = fake.street_address()

    # TODO: trim and move Apt, Suite, Etc to address line 2

    data['street2'] = ''

    data['city'] = fake.city()

    data['state'] = fake.state()

    data['zip'] = fake.postcode()

    data['country'] = fake.current_country()

    return data
