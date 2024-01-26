
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


def test_12():
    assert solution.Solution().findContestMatch(56) == '(((((1,56),(28,29)),((14,43),(15,42))),(((7,50),(22,35)),((8,49),(21,36)))),((((3,54),(26,31)),((12,45),(17,40))),(((5,52),(24,33)),((10,47),(19,38)))))'
