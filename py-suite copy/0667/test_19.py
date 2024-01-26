
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


def test_19():
    assert solution.Solution().constructArray(29, 70) == [29, -40, 28, -39, 27, -38, 26, -37, 25, -36, 24, -35, 23, -34, 22, -33, 21, -32, 20, -31, 19, -30, 18, -29, 17, -28, 16, -27, 15, -26, 14, -25, 13, -24, 12, -23, 11, -22, 10, -21, 9, -20, 8, -19, 7, -18, 6, -17, 5, -16, 4, -15, 3, -14, 2, -13, 1, -12, 0, -11, -1, -10, -2, -9, -3, -8, -4, -7, -5, -6]
