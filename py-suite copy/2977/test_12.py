
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
    assert solution.Solution()._getSubToId('ovRI8gsyke', 'bs2xHptsQc') == {'o': 0, 'v': 1, 'R': 2, 'I': 3, '8': 4, 'g': 5, 's': 6, 'y': 7, 'k': 8, 'e': 9, 'b': 10, '2': 11, 'x': 12, 'H': 13, 'p': 14, 't': 15, 'Q': 16, 'c': 17}
