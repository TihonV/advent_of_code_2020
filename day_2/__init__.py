from functools import partial
from pathlib import Path
from typing import Iterable, Callable
import re
import operator as op
import itertools as it


PASSWORD_PATTERN = re.compile(
    r'^(?P<minimum>\d+)-(?P<maximum>\d+)\s(?P<char>[a-z]):\s(?P<probe>[a-z]+)$',
)

input_data: str = Path(__file__).parent.joinpath('input.txt').read_text()


def read_input(t: str = input_data) -> Iterable[int]:
    yield from filter(bool, t.split('\n'))


def check_password_first_part(minimum: str, maximum: str, char: str, probe: str) -> bool:
    assert minimum.isalnum()
    assert maximum.isalnum()

    return int(minimum) <= probe.count(char) <= int(maximum)


def check_password_second_part(minimum: str, maximum: str, char: str, probe: str) -> bool:
    assert minimum.isalnum()
    assert maximum.isalnum()

    minimum, maximum = map(
        partial(op.add, -1),           # index was starts from 0
        map(int, [minimum, maximum]),  # cast to int
    )

    return list.count([probe[minimum], probe[maximum]], char) == 1


def process(data: Iterable[str], rule_callback: Callable) -> int:
    dataset = map(PASSWORD_PATTERN.match, data)
    dataset = map(op.methodcaller('groups'), dataset)
    return sum(it.starmap(rule_callback, dataset))


first_part = partial(process, data=read_input(), rule_callback=check_password_first_part)
second_part = partial(process, data=read_input(), rule_callback=check_password_second_part)
