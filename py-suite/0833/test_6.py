
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


def test_6():
    assert solution.Solution().findReplaceString('QN7VKuri0p', [100, 14, 48, 71], ['Yd4DOU4PYN', 'A4EiFBSFfO', 's1Y5TfucDY', 'RBosNDtO7V', 'nAfH79aPUh', 'VcnIc7FGBq'], ['8V6hKvgSz5', 'EY3AFKHyhY', 'sVBJkBcIVj']) == 'QN7VKuri0p'
