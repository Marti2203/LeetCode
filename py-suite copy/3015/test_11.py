
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


def test_11():
    assert solution.Solution().countOfPairs(88, 57, 10) == [176, 180, 186, 192, 198, 204, 210, 216, 222, 228, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 210, 160, 154, 148, 142, 136, 130, 124, 118, 110, 102, 96, 90, 84, 78, 72, 66, 60, 54, 50, 46, 42, 38, 34, 30, 26, 22, 18, 14, 10, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
