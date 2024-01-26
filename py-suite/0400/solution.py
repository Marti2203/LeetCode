
import random
import typing
from typing import *
import collections
from collections import *
import functools
from functools import *
import math
from math import *
import string
from string import *
import bisect
import heapq
from heapq import *
import itertools
from itertools import *
import re
from re import *
import operator
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if other is None:
            return False
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if other is None:
            return False
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"




class Solution:
    def findNthDigit(self, n: int) -> int:
        # Find the number that contains the nth digit
        num_digits = 1
        current_num = 9
        while n > num_digits * current_num:
            n -= num_digits * current_num
            num_digits += 1
            current_num *= 10
        
        # Find the digit within the number
        digit = n // num_digits
        if digit == 0:
            return n % num_digits
        else:
            return int(str(current_num)[digit - 1])
