
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
    assert solution.Solution().findContestMatch(42) == '(((((1,42),(21,22)),((10,33),(12,31))),(((5,38),(17,26)),((6,37),(16,27)))),((((2,41),(20,23)),((9,34),(13,30))),(((4,39),(18,25)),((7,36),(15,28)))))'
