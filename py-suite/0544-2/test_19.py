
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
    assert solution.Solution().findContestMatch(57) == '(((((1,57),(28,30)),((14,44),(15,43))),(((7,51),(22,36)),((8,50),(21,37)))),((((3,55),(26,32)),((12,46),(17,41))),(((5,53),(24,34)),((10,48),(19,39)))))'
