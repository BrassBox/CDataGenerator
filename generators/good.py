# Creates and returns a dict containing an address
import json
from generators import fake


# Generate address given template
# Currently ignored and uses generic address
def generate_good(path, **kwargs):
    # TEMP: ignore and override path
    path = "./rules/goods/good.json"

    # Open and load json file
    with open(path, "r") as file:
        data = json.load(file)

        return generate_good_map(data)


def generate_good_map(data, **kwargs):
    data['name'] = fake.pystr(min_chars=5, max_chars=10)

    data['sku'] = fake.pystr(min_chars=5, max_chars=10)

    data['url'] = fake.uri()

    data['quantity'] = fake.pyint(min_value=1, max_value=50)

    data['unit_amount'] = fake.pyint(min_value=1, max_value=10000)

    data['total_amount'] = int(data['unit_amount']) * int(data['quantity'])

    data['total_tax_rate'] = fake.pyint(min_value=1, max_value=150)  # Interpreted as 1.11?

    data['taxable_amount'] = data['total_amount']

    data['tax_exempt_amount'] = data['total_amount'] - data['taxable_amount']

    data['total_tax_amount'] = int(data['taxable_amount'] * (float(data['total_tax_rate']) / 100)
                                   + data['tax_exempt_amount'])

    data['total_discount_amount'] = 0

    return data
