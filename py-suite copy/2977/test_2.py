
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
    assert solution.Solution()._getSubToId('MRmUlMyYD9', 'JLpqzl1AQB') == {'M': 0, 'R': 1, 'm': 2, 'U': 3, 'l': 4, 'y': 5, 'Y': 6, 'D': 7, '9': 8, 'J': 9, 'L': 10, 'p': 11, 'q': 12, 'z': 13, '1': 14, 'A': 15, 'Q': 16, 'B': 17}
