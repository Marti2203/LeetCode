
import solution

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


def test_16():
    assert solution.Solution().constructArray(64, 94) == [64, -29, 63, -28, 62, -27, 61, -26, 60, -25, 59, -24, 58, -23, 57, -22, 56, -21, 55, -20, 54, -19, 53, -18, 52, -17, 51, -16, 50, -15, 49, -14, 48, -13, 47, -12, 46, -11, 45, -10, 44, -9, 43, -8, 42, -7, 41, -6, 40, -5, 39, -4, 38, -3, 37, -2, 36, -1, 35, 0, 34, 1, 33, 2, 32, 3, 31, 4, 30, 5, 29, 6, 28, 7, 27, 8, 26, 9, 25, 10, 24, 11, 23, 12, 22, 13, 21, 14, 20, 15, 19, 16, 18, 17]
