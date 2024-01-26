
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


def test_10():
    assert solution.Solution().findContestMatch(43) == '(((((1,43),(21,23)),((10,34),(12,32))),(((5,39),(17,27)),((6,38),(16,28)))),((((2,42),(20,24)),((9,35),(13,31))),(((4,40),(18,26)),((7,37),(15,29)))))'
