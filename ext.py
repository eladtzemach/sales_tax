import math


def round_tax(tax):
    return "{:0.2f}".format(math.ceil(tax * 20) / 20)
