from enum import Enum


class CategoryName(Enum):
    cancel = 'Cancel'
    sale = 'Sale'
    x = 'X'
    m = 'M'
    eight = '8'
    seven = '7'
    five = '5'
    fore = '4'
    three = '3'
    two = '2'
    one = '1'
    z = 'z4'
    plug_in = 'PLUG-IN'
    hybrid = 'HYBRID'
    electric = 'Electric'

    @classmethod
    def as_choices(cls):
        return [(cat.value, cat.name) for cat in cls]
