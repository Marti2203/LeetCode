
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
    assert solution.Solution().subsetsWithDup([47, 44, 10, 46, 72]) == [[], [10], [10, 44], [10, 44, 46], [10, 44, 46, 47], [10, 44, 46, 47, 72], [10, 44, 46, 72], [10, 44, 47], [10, 44, 47, 72], [10, 44, 72], [10, 46], [10, 46, 47], [10, 46, 47, 72], [10, 46, 72], [10, 47], [10, 47, 72], [10, 72], [44], [44, 46], [44, 46, 47], [44, 46, 47, 72], [44, 46, 72], [44, 47], [44, 47, 72], [44, 72], [46], [46, 47], [46, 47, 72], [46, 72], [47], [47, 72], [72]]
