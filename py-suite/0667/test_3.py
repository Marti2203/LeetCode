
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


def test_3():
    assert solution.Solution().constructArray(57, 87) == [57, -29, 56, -28, 55, -27, 54, -26, 53, -25, 52, -24, 51, -23, 50, -22, 49, -21, 48, -20, 47, -19, 46, -18, 45, -17, 44, -16, 43, -15, 42, -14, 41, -13, 40, -12, 39, -11, 38, -10, 37, -9, 36, -8, 35, -7, 34, -6, 33, -5, 32, -4, 31, -3, 30, -2, 29, -1, 28, 0, 27, 1, 26, 2, 25, 3, 24, 4, 23, 5, 22, 6, 21, 7, 20, 8, 19, 9, 18, 10, 17, 11, 16, 12, 15, 13, 14]
