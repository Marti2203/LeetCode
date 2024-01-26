
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


def test_0():
    assert solution.Solution().constructArray(66, 96) == [66, -29, 65, -28, 64, -27, 63, -26, 62, -25, 61, -24, 60, -23, 59, -22, 58, -21, 57, -20, 56, -19, 55, -18, 54, -17, 53, -16, 52, -15, 51, -14, 50, -13, 49, -12, 48, -11, 47, -10, 46, -9, 45, -8, 44, -7, 43, -6, 42, -5, 41, -4, 40, -3, 39, -2, 38, -1, 37, 0, 36, 1, 35, 2, 34, 3, 33, 4, 32, 5, 31, 6, 30, 7, 29, 8, 28, 9, 27, 10, 26, 11, 25, 12, 24, 13, 23, 14, 22, 15, 21, 16, 20, 17, 19, 18]
