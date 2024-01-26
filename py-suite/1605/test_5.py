
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
    assert solution.Solution().restoreMatrix([79, 48, 53, 57, 72], [87, 90, 92, 68, 13]) == [[79, 0, 0, 0, 0], [8, 40, 0, 0, 0], [0, 50, 3, 0, 0], [0, 0, 57, 0, 0], [0, 0, 32, 40, 0]]
