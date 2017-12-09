#!/usr/bin/env python


import sympy
from sympy import pprint

def main():
    a = sympy.Symbol('a')
    b = sympy.Symbol('b')
    e = (a + 8*b)**9

    print "\nExpression : "
    print
    pprint(e)
    print "\n\nDifferentiating with respect to a:"
    print
    pprint(e.diff(a))
    print "\n\nDifferentiating with respect to b:"
    print
    pprint(e.diff(b))
    print "\n\nSecond derivative of the above result with respect to a:"
    print
    pprint(e.diff(b).diff(a, 8))
    print "\n\nExpanding the above result:"
    print
    pprint(e.expand().diff(b).diff(a, 8))
    print

 main()
