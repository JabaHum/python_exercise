#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

Solution:
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input()

    def printString(self):
        print self.s.upper()

strObj = InputOutString()
strObj.getString()
strObj.printString()
#----------------------------------------#
'''
import sys
class InputOutString(object):
    def __init__(self):
        self.s = ""		# this function calls the class

    def getString(self):
        self.s = raw_input() # this function asks for input

    def printString(self):
        print self.s.upper() #this function changes to upper case

strObj = InputOutString() # this initialises the class 
strObj.getString() # this asks for a string 
strObj.printString() #this prints the string in upper case 

