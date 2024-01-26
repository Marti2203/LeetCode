
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


def test_5():
    assert solution.Solution().constructArray(4, 28) == [4, -23, 3, -22, 2, -21, 1, -20, 0, -19, -1, -18, -2, -17, -3, -16, -4, -15, -5, -14, -6, -13, -7, -12, -8, -11, -9, -10]
