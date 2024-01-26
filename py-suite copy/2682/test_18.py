
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


def test_18():
    assert solution.Solution().circularGameLosers(79, 38) == [3, 5, 6, 7, 8, 11, 12, 14, 15, 19, 22, 23, 28, 30, 31, 33, 40, 43, 44, 45, 46, 49, 50, 51, 53, 55, 57, 59, 63, 64, 69, 70, 72, 73, 74, 75, 76, 77, 79]
