
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


def test_12():
    assert solution.Solution().constructArray(65, 80) == [65, -14, 64, -13, 63, -12, 62, -11, 61, -10, 60, -9, 59, -8, 58, -7, 57, -6, 56, -5, 55, -4, 54, -3, 53, -2, 52, -1, 51, 0, 50, 1, 49, 2, 48, 3, 47, 4, 46, 5, 45, 6, 44, 7, 43, 8, 42, 9, 41, 10, 40, 11, 39, 12, 38, 13, 37, 14, 36, 15, 35, 16, 34, 17, 33, 18, 32, 19, 31, 20, 30, 21, 29, 22, 28, 23, 27, 24, 26, 25]
