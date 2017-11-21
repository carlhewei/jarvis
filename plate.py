#!/usr/bin/env python3
import jarvis

jarvis.groundClient('git')
jarvis.jarvisFile('plate.py')

ones = jarvis.Literal([1, 2, 3])
ones.forEach()

tens = jarvis.Literal([10, 100])
tens.forEach()

@jarvis.func
def multiply(x, y):
    z = x*y
    print(z)
    return z

doMultiply = jarvis.Action(multiply, [ones, tens])
product = jarvis.Artifact('product.txt', doMultiply)

product.pull()
product.plot()