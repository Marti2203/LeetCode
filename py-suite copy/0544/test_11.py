
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
    assert solution.Solution().findContestMatch(40) == '(((((1,40),(20,21)),((10,31),(11,30))),(((5,36),(16,25)),((6,35),(15,26)))),((((2,39),(19,22)),((9,32),(12,29))),(((4,37),(17,24)),((7,34),(14,27)))))'
