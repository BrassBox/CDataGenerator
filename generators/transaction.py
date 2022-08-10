# Creates and returns a dict containing an address
import json
from generators import fake


# Generate address given template
# Currently ignored and uses generic address
def generate_transaction(path, details):
    # TEMP: ignore and override path
    # path = "./rules/urls/urls.json"

    # Open and load json file
    with open(path, "r") as file:
        data = json.load(file)

        return generate_transaction_map(data, details)


def generate_transaction_map(data, request):
    data['reference'] = fake.pystr(min_chars=data['reference']['minLength'],
                                   max_chars=data['reference']['maxLength'])

    # Calculate goods total cost
    goods = request['goods']['data']['item']
    amount = 0
    for good in goods:
        amount += good['total_tax_amount']

    data['amount'] = amount

    data['currency'] = fake.currency_code()

    data['country'] = fake.country()

    data['auto_capture'] = True \
        if any(method == request['payment']['method'] for method in data['auto_capture']['required']) else fake.pybool()

    data['note'] = ""

    return data
