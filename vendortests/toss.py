import json
import sys
from random import randint

import generators
from generators import address
from generators import consumer
from generators import good
from generators import urls
from generators import transaction
from generators import payment
from generators import installments
from generators import goods
from generators import ext


def generate_toss():
    # TEMP: ignore and override path
    path = "./rules/processor/toss.json"

    data = {}
    # Open and load json file
    with open(path, "r") as json_config:
        data = json.load(json_config)
        # Payment must be generated before and passed to transaction
        data['payment'] = payment.generate_payment('./rules/payment/toss_payment.json', 'toss')
        data['installments'] = installments.generate_installment('./rules/installment/toss_installment.json', data)

        # Non-specific Values
        data['urls'] = urls.generate_urls(None)
        data['consumer'] = consumer.generate_consumer(None)
        # Goods automatically generates good(s), perhaps allow pass value
        data['goods'] = goods.generate_goods(None)
        data['ext'] = ext.generate_ext(None)

        data['transaction'] = transaction.generate_transaction(
            './rules/transaction/toss_transaction.json', data)


    return data
