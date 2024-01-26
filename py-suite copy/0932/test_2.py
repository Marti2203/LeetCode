
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


def test_2():
    assert solution.Solution().beautifulArray(77) == [63, 31, 47, 15, 55, 23, 39, 71, 7, 59, 27, 43, 75, 11, 51, 19, 35, 67, 3, 61, 29, 45, 77, 13, 53, 21, 37, 69, 5, 57, 25, 41, 73, 9, 49, 17, 33, 65, 1, 62, 30, 46, 14, 54, 22, 38, 70, 6, 58, 26, 42, 74, 10, 50, 18, 34, 66, 2, 60, 28, 44, 76, 12, 52, 20, 36, 68, 4, 56, 24, 40, 72, 8, 48, 16, 32, 64]
