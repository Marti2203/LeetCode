
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
    assert solution.Solution().getRow(45) == [1, 45, 990, 14190, 148995, 1221759, 8145060, 45379620, 215553195, 886163135, 3190187286, 10150595910, 28760021745, 73006209045, 166871334960, 344867425584, 646626422970, 1103068603890, 1715884494940, 2438362177020, 3169870830126, 3773655750150, 4116715363800, 4116715363800, 3773655750150, 3169870830126, 2438362177020, 1715884494940, 1103068603890, 646626422970, 344867425584, 166871334960, 73006209045, 28760021745, 10150595910, 3190187286, 886163135, 215553195, 45379620, 8145060, 1221759, 148995, 14190, 990, 45, 1]
