#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
items=[x for x in raw_input().split(',')]
items.sort()
print ','.join(items)
#----------------------------------------#
'''
import sys
#For loop for looping in the s
items=[x for x in raw_input().split(',')]
#items = x
#for i in x in raw_input().split(',')
 #this just arranges in ascending order of the alphabet
items.sort()
print ','.join(items)

