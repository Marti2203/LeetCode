
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
    assert solution.Solution().findContestMatch(47) == '(((((1,47),(23,25)),((11,37),(13,35))),(((5,43),(19,29)),((7,41),(17,31)))),((((2,46),(22,26)),((10,38),(14,34))),(((4,44),(20,28)),((8,40),(16,32)))))'
