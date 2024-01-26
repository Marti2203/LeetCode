
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


def test_7():
    assert solution.Solution()._getSubToId('H20igrZyxV', 'mUmT4bRyfx') == {'H': 0, '2': 1, '0': 2, 'i': 3, 'g': 4, 'r': 5, 'Z': 6, 'y': 7, 'x': 8, 'V': 9, 'm': 10, 'U': 11, 'T': 12, '4': 13, 'b': 14, 'R': 15, 'f': 16}
