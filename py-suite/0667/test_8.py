
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


def test_8():
    assert solution.Solution().constructArray(62, 87) == [62, -24, 61, -23, 60, -22, 59, -21, 58, -20, 57, -19, 56, -18, 55, -17, 54, -16, 53, -15, 52, -14, 51, -13, 50, -12, 49, -11, 48, -10, 47, -9, 46, -8, 45, -7, 44, -6, 43, -5, 42, -4, 41, -3, 40, -2, 39, -1, 38, 0, 37, 1, 36, 2, 35, 3, 34, 4, 33, 5, 32, 6, 31, 7, 30, 8, 29, 9, 28, 10, 27, 11, 26, 12, 25, 13, 24, 14, 23, 15, 22, 16, 21, 17, 20, 18, 19]
