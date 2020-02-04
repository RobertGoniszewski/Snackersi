import random
import string
import datetime


def unique_strings(self, k: int, ntokens: int,
                   pool: str = string.ascii_letters) -> set:
    seen = set()
    # An optimization for tightly-bound loops:
    # Bind these methods outside of a loop
    join = ''.join
    add = seen.add
    while len(seen) < ntokens:
        token = join(random.choices(pool, k=k))
        add(token)
    return seen


def path(self, instance, filename):
    date = datetime.datetime.now()
    user = instance.User.id
    item = instance.Item.id
    use_random = self.unique_strings(4, 1)
    return f'{date}/{user}_{item}_{use_random}'
