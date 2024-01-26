
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


def test_11():
    assert solution.Solution()._getSubToId('qKQyJC8L4V', 'Gzbx3MfJY1') == {'q': 0, 'K': 1, 'Q': 2, 'y': 3, 'J': 4, 'C': 5, '8': 6, 'L': 7, '4': 8, 'V': 9, 'G': 10, 'z': 11, 'b': 12, 'x': 13, '3': 14, 'M': 15, 'f': 16, 'Y': 17, '1': 18}
