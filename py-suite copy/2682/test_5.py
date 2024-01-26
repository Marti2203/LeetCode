
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
    assert solution.Solution().circularGameLosers(67, 39) == [4, 6, 7, 8, 10, 11, 18, 20, 25, 26, 27, 30, 31, 33, 35, 36, 39, 42, 44, 47, 48, 52, 53, 54, 55, 57, 59, 60, 61, 62, 63, 64, 67]
