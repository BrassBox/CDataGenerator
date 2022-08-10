from vendortests import toss
import json
from config import TESTS

output = []
for x in range(0, TESTS):
    output.append(toss.generate_toss())

with open('./output/test.json', 'w') as out:
    json.dump(toss.generate_toss(), out, indent=4)
