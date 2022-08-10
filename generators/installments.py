# Creates and returns a dict containing an address
import json
from generators import fake


# Generate installment given template
def generate_installment(path, request, **kwargs):
    # Open and load json file
    with open(path, "r") as file:
        data = json.load(file)

        return __generate_installment_map(data, request, **kwargs)


def __generate_installment_map(data, request, **kwargs):

    payment_method = request['payment']['method']

    # Note: the following blocks make the assumption that the correct file is opened
    # Ex. Toss opens toss_installment.json
    # Check if payment method matches restrictions for id
    if any(method == payment_method for method in data['id']['restriction'].keys()):
        data['id'] = fake.pyint(min_value=data['id']['restriction'][payment_method]['min_value'],
                                max_value=data['id']['restriction'][payment_method]['max_value'])
    else:
        data['id'] = fake.pyint(min_value=0, max_value=12)  # Assumed Default

    # Check if payment method matches restrictions for quantity
    if any(method == payment_method for method in data['quantity']['restriction'].keys()):
        data['quantity'] = fake.pyint(min_value=data['quantity']['restriction'][payment_method]['min_value'],
                                      max_value=data['quantity']['restriction'][payment_method]['max_value'])
    else:
        data['quantity'] = fake.pyint(min_value=0, max_value=12)  # Assumed Default

    data['payment_number'] = fake.pyint(min_value=0, max_value=data['quantity'])  # Unknown, assumed bounds

    data['promo'] = [fake.pystr(min_chars=5, max_chars=10)]

    return data
