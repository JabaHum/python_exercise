'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(raw_input())
print fact(x)
#----------------------------------------#
'''
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys 

def fact (x):
	if x == 0 :
		return 1 #if a number is 1 return 1
	return x * fact (x-1) # if its not 1 then use the following to find the factorial of that number

x = int(raw_input())

print fact (x)
