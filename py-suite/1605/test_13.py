
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


def test_13():
    assert solution.Solution().restoreMatrix([59, 22, 68, 16, 46, 26], [76, 79, 55, 57, 74, 25]) == [[59, 0, 0, 0, 0, 0], [17, 5, 0, 0, 0, 0], [0, 68, 0, 0, 0, 0], [0, 6, 10, 0, 0, 0], [0, 0, 45, 1, 0, 0], [0, 0, 0, 26, 0, 0]]
