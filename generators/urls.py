# Creates and returns a dict containing an address
import json
from generators import fake


# Generate address given template
# Currently ignored and uses generic address
def generate_urls(path, **kwargs):
    # TEMP: ignore and override path
    path = "./rules/urls/urls.json"

    # Open and load json file
    with open(path, "r") as file:
        data = json.load(file)

        return generate_url_map(data, **kwargs)


def generate_url_map(data, **kwargs):
    data['ipn'] = fake.uri()

    data['success'] = fake.uri()

    data['fail'] = fake.uri()

    data['mobile'] = fake.uri()

    data['cancel'] = fake.uri()

    return data
