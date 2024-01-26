
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


def test_13():
    assert solution.Solution().findContestMatch(45) == '(((((1,45),(22,24)),((11,35),(12,34))),(((5,41),(18,28)),((7,39),(16,30)))),((((2,44),(21,25)),((10,36),(13,33))),(((4,42),(19,27)),((8,38),(15,31)))))'
