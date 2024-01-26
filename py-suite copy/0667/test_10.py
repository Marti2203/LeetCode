
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


def test_10():
    assert solution.Solution().constructArray(75, 68) == [1, 2, 3, 4, 5, 6, 7, 75, 8, 74, 9, 73, 10, 72, 11, 71, 12, 70, 13, 69, 14, 68, 15, 67, 16, 66, 17, 65, 18, 64, 19, 63, 20, 62, 21, 61, 22, 60, 23, 59, 24, 58, 25, 57, 26, 56, 27, 55, 28, 54, 29, 53, 30, 52, 31, 51, 32, 50, 33, 49, 34, 48, 35, 47, 36, 46, 37, 45, 38, 44, 39, 43, 40, 42, 41]
