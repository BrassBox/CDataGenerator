# Creates and returns a dict containing an address
import json
from generators import fake


# Generate address given template
# Currently ignored and uses generic address
def generate_shipping(path):
    # TEMP: ignore and override path
    path = "./rules/address/shipping.json"

    # Open and load json file
    with open(path, "r") as file:
        data = json.load(file)
        return generate_shipping_map(data)


def generate_shipping_map(data):
    data['first_name'] = fake.first_name()

    data['last_name'] = fake.last_name()

    data['phone'] = fake.phone_number()

    data['email'] = data['first_name'].lower() + str(fake.pyint()) + '@' + fake.free_email_domain()

    data['street'] = fake.street_address()

    # TODO: trim and move Apt, Suite to address line 2

    data['street2'] = ''

    data['city'] = fake.city()
    data['state'] = fake.state()

    data['zip'] = fake.postcode()

    data['country'] = fake.current_country()

    return data
