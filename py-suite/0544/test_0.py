
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


def test_0():
    assert solution.Solution().findContestMatch(49) == '(((((1,49),(24,26)),((12,38),(13,37))),(((6,44),(19,31)),((7,43),(18,32)))),((((3,47),(22,28)),((10,40),(15,35))),(((4,46),(21,29)),((9,41),(16,34)))))'
