
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


def test_8():
    assert solution.Solution()._getSubToId('FqzZ5F7aGR', 'SqRxXXZYGJ') == {'F': 0, 'q': 1, 'z': 2, 'Z': 3, '5': 4, '7': 5, 'a': 6, 'G': 7, 'R': 8, 'S': 9, 'x': 10, 'X': 11, 'Y': 12, 'J': 13}
