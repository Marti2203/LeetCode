
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
    assert solution.Solution().circularGameLosers(61, 94) == [2, 3, 4, 5, 6, 7, 9, 11, 12, 14, 17, 18, 24, 25, 27, 28, 29, 33, 37, 41, 42, 43, 45, 46, 52, 53, 56, 58, 59, 61]
