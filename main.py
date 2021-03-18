#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jaquille Hinkson
"""

import math

def basic():
    # =============================================================================
    #     +     for a + b
    #     -     for a - b
    #     /     for a / b
    #     *     for a * b
    # =============================================================================

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')

    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))

    if op == '+':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b)
    elif op == '-':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b)
    elif op == '*':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b)
    elif op == '/':
        if b == 0:
            return 'Error: Cannot be divided by 0'
        else:
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b)
    else:
        return "Incorrect operator! Please select from the given options!"


def scientific():
    # =============================================================================
    #     ^     for a ^ b
    #     %     for a mod b
    #     r     for the bth root of a (a ^ (1/b))
    #     !     for a factorial
    #     sin   for sin(a) in radians
    #     cos   for cos(a) in radians
    #     tan   for tan(a) in radians
    #     ln    for ln(a) (log base e of a)
    # =============================================================================

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "^, r, %, !, sin, cos, tan, ln" : ')

    if op in '^,r,%':
        a = int(input('Please type the first number: '))
        b = int(input('Please type the second number: '))
    elif op in '!,sin,cos,tan,ln':
        a = float(input('Please type the number: '))

        # Your solution here
        # power
    if op == '^':
        print(a, "^", b, "=", a ** b)
        # root
    elif op == 'r':
        print(a, "root", b, "=", b ** (1 / a))
        #modulus
    elif op == '%':
        print(a, "%", b, "=", a % b)
        # factorial
    elif op == '!':
        print("!(", a, ")", "=", math.factorial(a))
        # sine (Trigonometry)
    elif op == 'sin':
        print("sin(", a, ")", "=", math.sin(a))
        # cosine (Trigonometry)
    elif op == 'cos':
        print("cos(", a, ")", "=", math.cos(a))
        # tangent (Trigonometry)
    #elif op == 'tan':
    #    print("tan(", a, ")", "=", math.tan(a))
    #    # ln
    #elif op == 'ln':
    #    print("ln(", a, ")", "=", math.log(a))

    print("Choose a calculator")
    print("\t1. Basic Calculator")
    print("\t2. Scientific Calculator\n")
    ch = int(input("Please choose as 1 or 2: "))

    if ch == 1:
        print(basic())
    elif ch == 2:
        print(scientific())


def main():  # Wrapper function

    print("""Choose a calculator
    1. Basic Calculator
    2. Scientific Calculator""")
    choice = int(input('Please choose as 1 or 2: '))

    if choice == 1:
        print(basic())
    elif choice == 2:
        print(scientific())
    else:
        print('Invalid choice! Please select between 1 and 2:')


if __name__ == '__main__':
    main()