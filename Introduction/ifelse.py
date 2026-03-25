#!/bin/python3

import math
import os
import random
import re
import sys

'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird'''

if __name__ == '__main__':
    n = int(input().strip())
    check = lambda n: "Not Weird" if n % 2 == 0 and (n in range(2,6) or n > 20) else  "Weird"
    print(check(n))
