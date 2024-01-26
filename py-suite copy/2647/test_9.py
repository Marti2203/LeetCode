
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


def test_9():
    assert solution.Solution().colorRed(12) == [[1, 1], [2, 3], [3, 2], [4, 1], [4, 3], [4, 5], [4, 7], [5, 1], [6, 3], [6, 5], [6, 7], [6, 9], [6, 11], [7, 2], [8, 1], [8, 3], [8, 5], [8, 7], [8, 9], [8, 11], [8, 13], [8, 15], [9, 1], [10, 3], [10, 5], [10, 7], [10, 9], [10, 11], [10, 13], [10, 15], [10, 17], [10, 19], [11, 2], [12, 1], [12, 3], [12, 5], [12, 7], [12, 9], [12, 11], [12, 13], [12, 15], [12, 17], [12, 19], [12, 21], [12, 23]]
