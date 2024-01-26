
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


def test_13():
    assert solution.Solution().constructArray(68, 80) == [68, -11, 67, -10, 66, -9, 65, -8, 64, -7, 63, -6, 62, -5, 61, -4, 60, -3, 59, -2, 58, -1, 57, 0, 56, 1, 55, 2, 54, 3, 53, 4, 52, 5, 51, 6, 50, 7, 49, 8, 48, 9, 47, 10, 46, 11, 45, 12, 44, 13, 43, 14, 42, 15, 41, 16, 40, 17, 39, 18, 38, 19, 37, 20, 36, 21, 35, 22, 34, 23, 33, 24, 32, 25, 31, 26, 30, 27, 29, 28]
