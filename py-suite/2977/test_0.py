
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


def test_0():
    assert solution.Solution()._getSubToId('n5qZ1a9NwM', 'NvLTfwMA77') == {'n': 0, '5': 1, 'q': 2, 'Z': 3, '1': 4, 'a': 5, '9': 6, 'N': 7, 'w': 8, 'M': 9, 'v': 10, 'L': 11, 'T': 12, 'f': 13, 'A': 14, '7': 15}
