import itertools as it

from functools import partial
from pathlib import Path
from typing import Callable, Iterable


input_data: str = Path(__file__).parent.joinpath('input.txt').read_text()


def read_input(t: str = input_data) -> Iterable[int]:
    yield from map(int, filter(bool, t.split('\n')))


def solutions(seq: Iterable[int], n: int, r: int) -> int:
    # get all combinations w/o repeats
    args = it.combinations(seq, r)

    # sum of parts must be equal to `n`
    args = filter(lambda x: sum(x) == n, args)

    for result, *parts in args:
        # result is first multiplier
        for multiplier in parts:
            result *= multiplier
        return result


SolutionTypeHint = Callable[[Iterable[int], int], int]

solutions_first_part: SolutionTypeHint = partial(solutions, r=2)
solutions_second_part: SolutionTypeHint = partial(solutions, r=3)
