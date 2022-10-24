from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn

def check_greater_than(
    a: float,
    a_name: str,
    b: float,
    b_name: str,
) -> NoReturn:
    if a > b:
        raise ValueError(f"{a_name} is greater than {b_name}!")


def check_between(
    a: float,
    min: float,
    max: float,
    name: str,
) -> NoReturn:
    if a < min or a > max:
        raise ValueError(f"{name} must be between {min} and {max}!")
    