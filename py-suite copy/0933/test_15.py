
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


def test_15():
    assert solution.Solution().beautifulArray(61) == [31, 47, 15, 55, 23, 39, 7, 59, 27, 43, 11, 51, 19, 35, 3, 61, 29, 45, 13, 53, 21, 37, 5, 57, 25, 41, 9, 49, 17, 33, 1, 30, 46, 14, 54, 22, 38, 6, 58, 26, 42, 10, 50, 18, 34, 2, 60, 28, 44, 12, 52, 20, 36, 4, 56, 24, 40, 8, 48, 16, 32]
