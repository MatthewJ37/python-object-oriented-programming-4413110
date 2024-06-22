# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str
    author: str
    pages: int
    price: float

    # you can define default values for attributes that are not required
    # by using the "default" keyword argument
    