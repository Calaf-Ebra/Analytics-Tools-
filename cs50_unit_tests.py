# -*- coding: utf-8 -*-
"""CS50 Unit Tests.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zzSjTPohXZZ2_Ug9zvsX4VOv7ftw82js
"""

def main():
    x = int(input('Waht is X'))
    print("X is ", sg(x))


def sg(t):
   return t * t

main()

#Create another file and use assertions.. from f1 import sg

def test():
    assert sg(2) == 4
    assert sg(7) === 5

def test_negative():
     #To make test catogires so that we can easily logically find bugs..all parts will work
     assert sg(-2) == 4
     assert sg(-3) ==  9
def test_zero():
    assert sg(0) == 0
def test_str():
    with pytest.raises(TypeError):
        sg("cat")


    #now import pytest and use it,, in new craeted file

"""Testing Strings"""

def main():
    name = input('Your name ')
    print(hello(name))
def hello(x):
    print(f"Hello, {x}")

if __name__ == __main__:
    main()

###Test Units in other file as below
from file import hello
def test_hello():
    assert hello('Ca') == 'Hello, ca'
    #test working of function
    assert hello() == 'hello,x'

###again better to make them in parts also to keep tests nice and simple
def test_fuc():
    assert hello() == 'hello,x'

def test_arg():
    assert hello('Ca') == 'Hello, ca'