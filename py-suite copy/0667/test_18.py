
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


def test_18():
    assert solution.Solution().constructArray(60, 79) == [60, -18, 59, -17, 58, -16, 57, -15, 56, -14, 55, -13, 54, -12, 53, -11, 52, -10, 51, -9, 50, -8, 49, -7, 48, -6, 47, -5, 46, -4, 45, -3, 44, -2, 43, -1, 42, 0, 41, 1, 40, 2, 39, 3, 38, 4, 37, 5, 36, 6, 35, 7, 34, 8, 33, 9, 32, 10, 31, 11, 30, 12, 29, 13, 28, 14, 27, 15, 26, 16, 25, 17, 24, 18, 23, 19, 22, 20, 21]
