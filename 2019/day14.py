from collections import namedtuple, Counter
from collections import defaultdict
import math

Reaction = namedtuple('Reaction', 'input output')
reactions = [Reaction(input={'ORE': 10}, output={'A': 10}),
             Reaction(input={'ORE': 1}, output={'B': 1}),
             Reaction(input={'A': 7, 'B': 1}, output={'C': 1}),
             Reaction(input={'A': 7, 'C': 1}, output={'D': 1}),
             Reaction(input={'A': 7, 'D': 1}, output={'E': 1}),
             Reaction(input={'A': 7, 'E': 1}, output={'FUEL': 1})]


def needed_input(output, amount=1):
    needed = []
    for reaction in reactions:
        if output in reaction.output:
            for k, v in reaction.input.items():
                needed.append((k, v))
    return needed


print(needed_input('FUEL', 2))
