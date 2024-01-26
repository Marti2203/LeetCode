
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


def test_19():
    assert solution.Solution().circularGameLosers(71, 37) == [3, 4, 5, 7, 8, 11, 13, 14, 15, 17, 18, 19, 20, 21, 22, 30, 34, 36, 37, 40, 44, 45, 46, 49, 51, 54, 56, 57, 58, 62, 64, 65, 67, 69, 70]
