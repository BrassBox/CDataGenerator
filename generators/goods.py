# Creates and returns a dict containing an address
import json
from generators import fake
from generators import good
from generators import shipping


# Generate address given template
# Currently ignored and uses generic address
# TODO: optional number input
def generate_goods(path, **kwargs):
    # TEMP: ignore and override path
    path = "./rules/goods/goods.json"

    # Open and load json file
    with open(path, "r") as file:
        data = json.load(file)

        return generate_goods_map(data, **kwargs)


def generate_goods_map(data, **kwargs):
    data['data'] = {
        "item": []
    }
    for x in range(0, 1):  # Future Accept kwarg range?
        data['data']['item'].append(good.generate_good(None))

    shipping.generate_shipping_map(data['shipping'])

    return data
