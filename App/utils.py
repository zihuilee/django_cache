import random
from random import randrange


def getcolor():
    return randrange(256)


def gendratecode():
    source = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    code = ''
    for i in range(4):
        code += random.choice(source)
    return code