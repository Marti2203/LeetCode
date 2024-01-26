
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
    assert solution.Solution().permuteUnique([53, 64, 54, 12, 93, 100]) == [[12, 53, 54, 64, 93, 100], [12, 53, 54, 64, 100, 93], [12, 53, 54, 93, 64, 100], [12, 53, 54, 93, 100, 64], [12, 53, 54, 100, 64, 93], [12, 53, 54, 100, 93, 64], [12, 53, 64, 54, 93, 100], [12, 53, 64, 54, 100, 93], [12, 53, 64, 93, 54, 100], [12, 53, 64, 93, 100, 54], [12, 53, 64, 100, 54, 93], [12, 53, 64, 100, 93, 54], [12, 53, 93, 54, 64, 100], [12, 53, 93, 54, 100, 64], [12, 53, 93, 64, 54, 100], [12, 53, 93, 64, 100, 54], [12, 53, 93, 100, 54, 64], [12, 53, 93, 100, 64, 54], [12, 53, 100, 54, 64, 93], [12, 53, 100, 54, 93, 64], [12, 53, 100, 64, 54, 93], [12, 53, 100, 64, 93, 54], [12, 53, 100, 93, 54, 64], [12, 53, 100, 93, 64, 54], [12, 54, 53, 64, 93, 100], [12, 54, 53, 64, 100, 93], [12, 54, 53, 93, 64, 100], [12, 54, 53, 93, 100, 64], [12, 54, 53, 100, 64, 93], [12, 54, 53, 100, 93, 64], [12, 54, 64, 53, 93, 100], [12, 54, 64, 53, 100, 93], [12, 54, 64, 93, 53, 100], [12, 54, 64, 93, 100, 53], [12, 54, 64, 100, 53, 93], [12, 54, 64, 100, 93, 53], [12, 54, 93, 53, 64, 100], [12, 54, 93, 53, 100, 64], [12, 54, 93, 64, 53, 100], [12, 54, 93, 64, 100, 53], [12, 54, 93, 100, 53, 64], [12, 54, 93, 100, 64, 53], [12, 54, 100, 53, 64, 93], [12, 54, 100, 53, 93, 64], [12, 54, 100, 64, 53, 93], [12, 54, 100, 64, 93, 53], [12, 54, 100, 93, 53, 64], [12, 54, 100, 93, 64, 53], [12, 64, 53, 54, 93, 100], [12, 64, 53, 54, 100, 93], [12, 64, 53, 93, 54, 100], [12, 64, 53, 93, 100, 54], [12, 64, 53, 100, 54, 93], [12, 64, 53, 100, 93, 54], [12, 64, 54, 53, 93, 100], [12, 64, 54, 53, 100, 93], [12, 64, 54, 93, 53, 100], [12, 64, 54, 93, 100, 53], [12, 64, 54, 100, 53, 93], [12, 64, 54, 100, 93, 53], [12, 64, 93, 53, 54, 100], [12, 64, 93, 53, 100, 54], [12, 64, 93, 54, 53, 100], [12, 64, 93, 54, 100, 53], [12, 64, 93, 100, 53, 54], [12, 64, 93, 100, 54, 53], [12, 64, 100, 53, 54, 93], [12, 64, 100, 53, 93, 54], [12, 64, 100, 54, 53, 93], [12, 64, 100, 54, 93, 53], [12, 64, 100, 93, 53, 54], [12, 64, 100, 93, 54, 53], [12, 93, 53, 54, 64, 100], [12, 93, 53, 54, 100, 64], [12, 93, 53, 64, 54, 100], [12, 93, 53, 64, 100, 54], [12, 93, 53, 100, 54, 64], [12, 93, 53, 100, 64, 54], [12, 93, 54, 53, 64, 100], [12, 93, 54, 53, 100, 64], [12, 93, 54, 64, 53, 100], [12, 93, 54, 64, 100, 53], [12, 93, 54, 100, 53, 64], [12, 93, 54, 100, 64, 53], [12, 93, 64, 53, 54, 100], [12, 93, 64, 53, 100, 54], [12, 93, 64, 54, 53, 100], [12, 93, 64, 54, 100, 53], [12, 93, 64, 100, 53, 54], [12, 93, 64, 100, 54, 53], [12, 93, 100, 53, 54, 64], [12, 93, 100, 53, 64, 54], [12, 93, 100, 54, 53, 64], [12, 93, 100, 54, 64, 53], [12, 93, 100, 64, 53, 54], [12, 93, 100, 64, 54, 53], [12, 100, 53, 54, 64, 93], [12, 100, 53, 54, 93, 64], [12, 100, 53, 64, 54, 93], [12, 100, 53, 64, 93, 54], [12, 100, 53, 93, 54, 64], [12, 100, 53, 93, 64, 54], [12, 100, 54, 53, 64, 93], [12, 100, 54, 53, 93, 64], [12, 100, 54, 64, 53, 93], [12, 100, 54, 64, 93, 53], [12, 100, 54, 93, 53, 64], [12, 100, 54, 93, 64, 53], [12, 100, 64, 53, 54, 93], [12, 100, 64, 53, 93, 54], [12, 100, 64, 54, 53, 93], [12, 100, 64, 54, 93, 53], [12, 100, 64, 93, 53, 54], [12, 100, 64, 93, 54, 53], [12, 100, 93, 53, 54, 64], [12, 100, 93, 53, 64, 54], [12, 100, 93, 54, 53, 64], [12, 100, 93, 54, 64, 53], [12, 100, 93, 64, 53, 54], [12, 100, 93, 64, 54, 53], [53, 12, 54, 64, 93, 100], [53, 12, 54, 64, 100, 93], [53, 12, 54, 93, 64, 100], [53, 12, 54, 93, 100, 64], [53, 12, 54, 100, 64, 93], [53, 12, 54, 100, 93, 64], [53, 12, 64, 54, 93, 100], [53, 12, 64, 54, 100, 93], [53, 12, 64, 93, 54, 100], [53, 12, 64, 93, 100, 54], [53, 12, 64, 100, 54, 93], [53, 12, 64, 100, 93, 54], [53, 12, 93, 54, 64, 100], [53, 12, 93, 54, 100, 64], [53, 12, 93, 64, 54, 100], [53, 12, 93, 64, 100, 54], [53, 12, 93, 100, 54, 64], [53, 12, 93, 100, 64, 54], [53, 12, 100, 54, 64, 93], [53, 12, 100, 54, 93, 64], [53, 12, 100, 64, 54, 93], [53, 12, 100, 64, 93, 54], [53, 12, 100, 93, 54, 64], [53, 12, 100, 93, 64, 54], [53, 54, 12, 64, 93, 100], [53, 54, 12, 64, 100, 93], [53, 54, 12, 93, 64, 100], [53, 54, 12, 93, 100, 64], [53, 54, 12, 100, 64, 93], [53, 54, 12, 100, 93, 64], [53, 54, 64, 12, 93, 100], [53, 54, 64, 12, 100, 93], [53, 54, 64, 93, 12, 100], [53, 54, 64, 93, 100, 12], [53, 54, 64, 100, 12, 93], [53, 54, 64, 100, 93, 12], [53, 54, 93, 12, 64, 100], [53, 54, 93, 12, 100, 64], [53, 54, 93, 64, 12, 100], [53, 54, 93, 64, 100, 12], [53, 54, 93, 100, 12, 64], [53, 54, 93, 100, 64, 12], [53, 54, 100, 12, 64, 93], [53, 54, 100, 12, 93, 64], [53, 54, 100, 64, 12, 93], [53, 54, 100, 64, 93, 12], [53, 54, 100, 93, 12, 64], [53, 54, 100, 93, 64, 12], [53, 64, 12, 54, 93, 100], [53, 64, 12, 54, 100, 93], [53, 64, 12, 93, 54, 100], [53, 64, 12, 93, 100, 54], [53, 64, 12, 100, 54, 93], [53, 64, 12, 100, 93, 54], [53, 64, 54, 12, 93, 100], [53, 64, 54, 12, 100, 93], [53, 64, 54, 93, 12, 100], [53, 64, 54, 93, 100, 12], [53, 64, 54, 100, 12, 93], [53, 64, 54, 100, 93, 12], [53, 64, 93, 12, 54, 100], [53, 64, 93, 12, 100, 54], [53, 64, 93, 54, 12, 100], [53, 64, 93, 54, 100, 12], [53, 64, 93, 100, 12, 54], [53, 64, 93, 100, 54, 12], [53, 64, 100, 12, 54, 93], [53, 64, 100, 12, 93, 54], [53, 64, 100, 54, 12, 93], [53, 64, 100, 54, 93, 12], [53, 64, 100, 93, 12, 54], [53, 64, 100, 93, 54, 12], [53, 93, 12, 54, 64, 100], [53, 93, 12, 54, 100, 64], [53, 93, 12, 64, 54, 100], [53, 93, 12, 64, 100, 54], [53, 93, 12, 100, 54, 64], [53, 93, 12, 100, 64, 54], [53, 93, 54, 12, 64, 100], [53, 93, 54, 12, 100, 64], [53, 93, 54, 64, 12, 100], [53, 93, 54, 64, 100, 12], [53, 93, 54, 100, 12, 64], [53, 93, 54, 100, 64, 12], [53, 93, 64, 12, 54, 100], [53, 93, 64, 12, 100, 54], [53, 93, 64, 54, 12, 100], [53, 93, 64, 54, 100, 12], [53, 93, 64, 100, 12, 54], [53, 93, 64, 100, 54, 12], [53, 93, 100, 12, 54, 64], [53, 93, 100, 12, 64, 54], [53, 93, 100, 54, 12, 64], [53, 93, 100, 54, 64, 12], [53, 93, 100, 64, 12, 54], [53, 93, 100, 64, 54, 12], [53, 100, 12, 54, 64, 93], [53, 100, 12, 54, 93, 64], [53, 100, 12, 64, 54, 93], [53, 100, 12, 64, 93, 54], [53, 100, 12, 93, 54, 64], [53, 100, 12, 93, 64, 54], [53, 100, 54, 12, 64, 93], [53, 100, 54, 12, 93, 64], [53, 100, 54, 64, 12, 93], [53, 100, 54, 64, 93, 12], [53, 100, 54, 93, 12, 64], [53, 100, 54, 93, 64, 12], [53, 100, 64, 12, 54, 93], [53, 100, 64, 12, 93, 54], [53, 100, 64, 54, 12, 93], [53, 100, 64, 54, 93, 12], [53, 100, 64, 93, 12, 54], [53, 100, 64, 93, 54, 12], [53, 100, 93, 12, 54, 64], [53, 100, 93, 12, 64, 54], [53, 100, 93, 54, 12, 64], [53, 100, 93, 54, 64, 12], [53, 100, 93, 64, 12, 54], [53, 100, 93, 64, 54, 12], [54, 12, 53, 64, 93, 100], [54, 12, 53, 64, 100, 93], [54, 12, 53, 93, 64, 100], [54, 12, 53, 93, 100, 64], [54, 12, 53, 100, 64, 93], [54, 12, 53, 100, 93, 64], [54, 12, 64, 53, 93, 100], [54, 12, 64, 53, 100, 93], [54, 12, 64, 93, 53, 100], [54, 12, 64, 93, 100, 53], [54, 12, 64, 100, 53, 93], [54, 12, 64, 100, 93, 53], [54, 12, 93, 53, 64, 100], [54, 12, 93, 53, 100, 64], [54, 12, 93, 64, 53, 100], [54, 12, 93, 64, 100, 53], [54, 12, 93, 100, 53, 64], [54, 12, 93, 100, 64, 53], [54, 12, 100, 53, 64, 93], [54, 12, 100, 53, 93, 64], [54, 12, 100, 64, 53, 93], [54, 12, 100, 64, 93, 53], [54, 12, 100, 93, 53, 64], [54, 12, 100, 93, 64, 53], [54, 53, 12, 64, 93, 100], [54, 53, 12, 64, 100, 93], [54, 53, 12, 93, 64, 100], [54, 53, 12, 93, 100, 64], [54, 53, 12, 100, 64, 93], [54, 53, 12, 100, 93, 64], [54, 53, 64, 12, 93, 100], [54, 53, 64, 12, 100, 93], [54, 53, 64, 93, 12, 100], [54, 53, 64, 93, 100, 12], [54, 53, 64, 100, 12, 93], [54, 53, 64, 100, 93, 12], [54, 53, 93, 12, 64, 100], [54, 53, 93, 12, 100, 64], [54, 53, 93, 64, 12, 100], [54, 53, 93, 64, 100, 12], [54, 53, 93, 100, 12, 64], [54, 53, 93, 100, 64, 12], [54, 53, 100, 12, 64, 93], [54, 53, 100, 12, 93, 64], [54, 53, 100, 64, 12, 93], [54, 53, 100, 64, 93, 12], [54, 53, 100, 93, 12, 64], [54, 53, 100, 93, 64, 12], [54, 64, 12, 53, 93, 100], [54, 64, 12, 53, 100, 93], [54, 64, 12, 93, 53, 100], [54, 64, 12, 93, 100, 53], [54, 64, 12, 100, 53, 93], [54, 64, 12, 100, 93, 53], [54, 64, 53, 12, 93, 100], [54, 64, 53, 12, 100, 93], [54, 64, 53, 93, 12, 100], [54, 64, 53, 93, 100, 12], [54, 64, 53, 100, 12, 93], [54, 64, 53, 100, 93, 12], [54, 64, 93, 12, 53, 100], [54, 64, 93, 12, 100, 53], [54, 64, 93, 53, 12, 100], [54, 64, 93, 53, 100, 12], [54, 64, 93, 100, 12, 53], [54, 64, 93, 100, 53, 12], [54, 64, 100, 12, 53, 93], [54, 64, 100, 12, 93, 53], [54, 64, 100, 53, 12, 93], [54, 64, 100, 53, 93, 12], [54, 64, 100, 93, 12, 53], [54, 64, 100, 93, 53, 12], [54, 93, 12, 53, 64, 100], [54, 93, 12, 53, 100, 64], [54, 93, 12, 64, 53, 100], [54, 93, 12, 64, 100, 53], [54, 93, 12, 100, 53, 64], [54, 93, 12, 100, 64, 53], [54, 93, 53, 12, 64, 100], [54, 93, 53, 12, 100, 64], [54, 93, 53, 64, 12, 100], [54, 93, 53, 64, 100, 12], [54, 93, 53, 100, 12, 64], [54, 93, 53, 100, 64, 12], [54, 93, 64, 12, 53, 100], [54, 93, 64, 12, 100, 53], [54, 93, 64, 53, 12, 100], [54, 93, 64, 53, 100, 12], [54, 93, 64, 100, 12, 53], [54, 93, 64, 100, 53, 12], [54, 93, 100, 12, 53, 64], [54, 93, 100, 12, 64, 53], [54, 93, 100, 53, 12, 64], [54, 93, 100, 53, 64, 12], [54, 93, 100, 64, 12, 53], [54, 93, 100, 64, 53, 12], [54, 100, 12, 53, 64, 93], [54, 100, 12, 53, 93, 64], [54, 100, 12, 64, 53, 93], [54, 100, 12, 64, 93, 53], [54, 100, 12, 93, 53, 64], [54, 100, 12, 93, 64, 53], [54, 100, 53, 12, 64, 93], [54, 100, 53, 12, 93, 64], [54, 100, 53, 64, 12, 93], [54, 100, 53, 64, 93, 12], [54, 100, 53, 93, 12, 64], [54, 100, 53, 93, 64, 12], [54, 100, 64, 12, 53, 93], [54, 100, 64, 12, 93, 53], [54, 100, 64, 53, 12, 93], [54, 100, 64, 53, 93, 12], [54, 100, 64, 93, 12, 53], [54, 100, 64, 93, 53, 12], [54, 100, 93, 12, 53, 64], [54, 100, 93, 12, 64, 53], [54, 100, 93, 53, 12, 64], [54, 100, 93, 53, 64, 12], [54, 100, 93, 64, 12, 53], [54, 100, 93, 64, 53, 12], [64, 12, 53, 54, 93, 100], [64, 12, 53, 54, 100, 93], [64, 12, 53, 93, 54, 100], [64, 12, 53, 93, 100, 54], [64, 12, 53, 100, 54, 93], [64, 12, 53, 100, 93, 54], [64, 12, 54, 53, 93, 100], [64, 12, 54, 53, 100, 93], [64, 12, 54, 93, 53, 100], [64, 12, 54, 93, 100, 53], [64, 12, 54, 100, 53, 93], [64, 12, 54, 100, 93, 53], [64, 12, 93, 53, 54, 100], [64, 12, 93, 53, 100, 54], [64, 12, 93, 54, 53, 100], [64, 12, 93, 54, 100, 53], [64, 12, 93, 100, 53, 54], [64, 12, 93, 100, 54, 53], [64, 12, 100, 53, 54, 93], [64, 12, 100, 53, 93, 54], [64, 12, 100, 54, 53, 93], [64, 12, 100, 54, 93, 53], [64, 12, 100, 93, 53, 54], [64, 12, 100, 93, 54, 53], [64, 53, 12, 54, 93, 100], [64, 53, 12, 54, 100, 93], [64, 53, 12, 93, 54, 100], [64, 53, 12, 93, 100, 54], [64, 53, 12, 100, 54, 93], [64, 53, 12, 100, 93, 54], [64, 53, 54, 12, 93, 100], [64, 53, 54, 12, 100, 93], [64, 53, 54, 93, 12, 100], [64, 53, 54, 93, 100, 12], [64, 53, 54, 100, 12, 93], [64, 53, 54, 100, 93, 12], [64, 53, 93, 12, 54, 100], [64, 53, 93, 12, 100, 54], [64, 53, 93, 54, 12, 100], [64, 53, 93, 54, 100, 12], [64, 53, 93, 100, 12, 54], [64, 53, 93, 100, 54, 12], [64, 53, 100, 12, 54, 93], [64, 53, 100, 12, 93, 54], [64, 53, 100, 54, 12, 93], [64, 53, 100, 54, 93, 12], [64, 53, 100, 93, 12, 54], [64, 53, 100, 93, 54, 12], [64, 54, 12, 53, 93, 100], [64, 54, 12, 53, 100, 93], [64, 54, 12, 93, 53, 100], [64, 54, 12, 93, 100, 53], [64, 54, 12, 100, 53, 93], [64, 54, 12, 100, 93, 53], [64, 54, 53, 12, 93, 100], [64, 54, 53, 12, 100, 93], [64, 54, 53, 93, 12, 100], [64, 54, 53, 93, 100, 12], [64, 54, 53, 100, 12, 93], [64, 54, 53, 100, 93, 12], [64, 54, 93, 12, 53, 100], [64, 54, 93, 12, 100, 53], [64, 54, 93, 53, 12, 100], [64, 54, 93, 53, 100, 12], [64, 54, 93, 100, 12, 53], [64, 54, 93, 100, 53, 12], [64, 54, 100, 12, 53, 93], [64, 54, 100, 12, 93, 53], [64, 54, 100, 53, 12, 93], [64, 54, 100, 53, 93, 12], [64, 54, 100, 93, 12, 53], [64, 54, 100, 93, 53, 12], [64, 93, 12, 53, 54, 100], [64, 93, 12, 53, 100, 54], [64, 93, 12, 54, 53, 100], [64, 93, 12, 54, 100, 53], [64, 93, 12, 100, 53, 54], [64, 93, 12, 100, 54, 53], [64, 93, 53, 12, 54, 100], [64, 93, 53, 12, 100, 54], [64, 93, 53, 54, 12, 100], [64, 93, 53, 54, 100, 12], [64, 93, 53, 100, 12, 54], [64, 93, 53, 100, 54, 12], [64, 93, 54, 12, 53, 100], [64, 93, 54, 12, 100, 53], [64, 93, 54, 53, 12, 100], [64, 93, 54, 53, 100, 12], [64, 93, 54, 100, 12, 53], [64, 93, 54, 100, 53, 12], [64, 93, 100, 12, 53, 54], [64, 93, 100, 12, 54, 53], [64, 93, 100, 53, 12, 54], [64, 93, 100, 53, 54, 12], [64, 93, 100, 54, 12, 53], [64, 93, 100, 54, 53, 12], [64, 100, 12, 53, 54, 93], [64, 100, 12, 53, 93, 54], [64, 100, 12, 54, 53, 93], [64, 100, 12, 54, 93, 53], [64, 100, 12, 93, 53, 54], [64, 100, 12, 93, 54, 53], [64, 100, 53, 12, 54, 93], [64, 100, 53, 12, 93, 54], [64, 100, 53, 54, 12, 93], [64, 100, 53, 54, 93, 12], [64, 100, 53, 93, 12, 54], [64, 100, 53, 93, 54, 12], [64, 100, 54, 12, 53, 93], [64, 100, 54, 12, 93, 53], [64, 100, 54, 53, 12, 93], [64, 100, 54, 53, 93, 12], [64, 100, 54, 93, 12, 53], [64, 100, 54, 93, 53, 12], [64, 100, 93, 12, 53, 54], [64, 100, 93, 12, 54, 53], [64, 100, 93, 53, 12, 54], [64, 100, 93, 53, 54, 12], [64, 100, 93, 54, 12, 53], [64, 100, 93, 54, 53, 12], [93, 12, 53, 54, 64, 100], [93, 12, 53, 54, 100, 64], [93, 12, 53, 64, 54, 100], [93, 12, 53, 64, 100, 54], [93, 12, 53, 100, 54, 64], [93, 12, 53, 100, 64, 54], [93, 12, 54, 53, 64, 100], [93, 12, 54, 53, 100, 64], [93, 12, 54, 64, 53, 100], [93, 12, 54, 64, 100, 53], [93, 12, 54, 100, 53, 64], [93, 12, 54, 100, 64, 53], [93, 12, 64, 53, 54, 100], [93, 12, 64, 53, 100, 54], [93, 12, 64, 54, 53, 100], [93, 12, 64, 54, 100, 53], [93, 12, 64, 100, 53, 54], [93, 12, 64, 100, 54, 53], [93, 12, 100, 53, 54, 64], [93, 12, 100, 53, 64, 54], [93, 12, 100, 54, 53, 64], [93, 12, 100, 54, 64, 53], [93, 12, 100, 64, 53, 54], [93, 12, 100, 64, 54, 53], [93, 53, 12, 54, 64, 100], [93, 53, 12, 54, 100, 64], [93, 53, 12, 64, 54, 100], [93, 53, 12, 64, 100, 54], [93, 53, 12, 100, 54, 64], [93, 53, 12, 100, 64, 54], [93, 53, 54, 12, 64, 100], [93, 53, 54, 12, 100, 64], [93, 53, 54, 64, 12, 100], [93, 53, 54, 64, 100, 12], [93, 53, 54, 100, 12, 64], [93, 53, 54, 100, 64, 12], [93, 53, 64, 12, 54, 100], [93, 53, 64, 12, 100, 54], [93, 53, 64, 54, 12, 100], [93, 53, 64, 54, 100, 12], [93, 53, 64, 100, 12, 54], [93, 53, 64, 100, 54, 12], [93, 53, 100, 12, 54, 64], [93, 53, 100, 12, 64, 54], [93, 53, 100, 54, 12, 64], [93, 53, 100, 54, 64, 12], [93, 53, 100, 64, 12, 54], [93, 53, 100, 64, 54, 12], [93, 54, 12, 53, 64, 100], [93, 54, 12, 53, 100, 64], [93, 54, 12, 64, 53, 100], [93, 54, 12, 64, 100, 53], [93, 54, 12, 100, 53, 64], [93, 54, 12, 100, 64, 53], [93, 54, 53, 12, 64, 100], [93, 54, 53, 12, 100, 64], [93, 54, 53, 64, 12, 100], [93, 54, 53, 64, 100, 12], [93, 54, 53, 100, 12, 64], [93, 54, 53, 100, 64, 12], [93, 54, 64, 12, 53, 100], [93, 54, 64, 12, 100, 53], [93, 54, 64, 53, 12, 100], [93, 54, 64, 53, 100, 12], [93, 54, 64, 100, 12, 53], [93, 54, 64, 100, 53, 12], [93, 54, 100, 12, 53, 64], [93, 54, 100, 12, 64, 53], [93, 54, 100, 53, 12, 64], [93, 54, 100, 53, 64, 12], [93, 54, 100, 64, 12, 53], [93, 54, 100, 64, 53, 12], [93, 64, 12, 53, 54, 100], [93, 64, 12, 53, 100, 54], [93, 64, 12, 54, 53, 100], [93, 64, 12, 54, 100, 53], [93, 64, 12, 100, 53, 54], [93, 64, 12, 100, 54, 53], [93, 64, 53, 12, 54, 100], [93, 64, 53, 12, 100, 54], [93, 64, 53, 54, 12, 100], [93, 64, 53, 54, 100, 12], [93, 64, 53, 100, 12, 54], [93, 64, 53, 100, 54, 12], [93, 64, 54, 12, 53, 100], [93, 64, 54, 12, 100, 53], [93, 64, 54, 53, 12, 100], [93, 64, 54, 53, 100, 12], [93, 64, 54, 100, 12, 53], [93, 64, 54, 100, 53, 12], [93, 64, 100, 12, 53, 54], [93, 64, 100, 12, 54, 53], [93, 64, 100, 53, 12, 54], [93, 64, 100, 53, 54, 12], [93, 64, 100, 54, 12, 53], [93, 64, 100, 54, 53, 12], [93, 100, 12, 53, 54, 64], [93, 100, 12, 53, 64, 54], [93, 100, 12, 54, 53, 64], [93, 100, 12, 54, 64, 53], [93, 100, 12, 64, 53, 54], [93, 100, 12, 64, 54, 53], [93, 100, 53, 12, 54, 64], [93, 100, 53, 12, 64, 54], [93, 100, 53, 54, 12, 64], [93, 100, 53, 54, 64, 12], [93, 100, 53, 64, 12, 54], [93, 100, 53, 64, 54, 12], [93, 100, 54, 12, 53, 64], [93, 100, 54, 12, 64, 53], [93, 100, 54, 53, 12, 64], [93, 100, 54, 53, 64, 12], [93, 100, 54, 64, 12, 53], [93, 100, 54, 64, 53, 12], [93, 100, 64, 12, 53, 54], [93, 100, 64, 12, 54, 53], [93, 100, 64, 53, 12, 54], [93, 100, 64, 53, 54, 12], [93, 100, 64, 54, 12, 53], [93, 100, 64, 54, 53, 12], [100, 12, 53, 54, 64, 93], [100, 12, 53, 54, 93, 64], [100, 12, 53, 64, 54, 93], [100, 12, 53, 64, 93, 54], [100, 12, 53, 93, 54, 64], [100, 12, 53, 93, 64, 54], [100, 12, 54, 53, 64, 93], [100, 12, 54, 53, 93, 64], [100, 12, 54, 64, 53, 93], [100, 12, 54, 64, 93, 53], [100, 12, 54, 93, 53, 64], [100, 12, 54, 93, 64, 53], [100, 12, 64, 53, 54, 93], [100, 12, 64, 53, 93, 54], [100, 12, 64, 54, 53, 93], [100, 12, 64, 54, 93, 53], [100, 12, 64, 93, 53, 54], [100, 12, 64, 93, 54, 53], [100, 12, 93, 53, 54, 64], [100, 12, 93, 53, 64, 54], [100, 12, 93, 54, 53, 64], [100, 12, 93, 54, 64, 53], [100, 12, 93, 64, 53, 54], [100, 12, 93, 64, 54, 53], [100, 53, 12, 54, 64, 93], [100, 53, 12, 54, 93, 64], [100, 53, 12, 64, 54, 93], [100, 53, 12, 64, 93, 54], [100, 53, 12, 93, 54, 64], [100, 53, 12, 93, 64, 54], [100, 53, 54, 12, 64, 93], [100, 53, 54, 12, 93, 64], [100, 53, 54, 64, 12, 93], [100, 53, 54, 64, 93, 12], [100, 53, 54, 93, 12, 64], [100, 53, 54, 93, 64, 12], [100, 53, 64, 12, 54, 93], [100, 53, 64, 12, 93, 54], [100, 53, 64, 54, 12, 93], [100, 53, 64, 54, 93, 12], [100, 53, 64, 93, 12, 54], [100, 53, 64, 93, 54, 12], [100, 53, 93, 12, 54, 64], [100, 53, 93, 12, 64, 54], [100, 53, 93, 54, 12, 64], [100, 53, 93, 54, 64, 12], [100, 53, 93, 64, 12, 54], [100, 53, 93, 64, 54, 12], [100, 54, 12, 53, 64, 93], [100, 54, 12, 53, 93, 64], [100, 54, 12, 64, 53, 93], [100, 54, 12, 64, 93, 53], [100, 54, 12, 93, 53, 64], [100, 54, 12, 93, 64, 53], [100, 54, 53, 12, 64, 93], [100, 54, 53, 12, 93, 64], [100, 54, 53, 64, 12, 93], [100, 54, 53, 64, 93, 12], [100, 54, 53, 93, 12, 64], [100, 54, 53, 93, 64, 12], [100, 54, 64, 12, 53, 93], [100, 54, 64, 12, 93, 53], [100, 54, 64, 53, 12, 93], [100, 54, 64, 53, 93, 12], [100, 54, 64, 93, 12, 53], [100, 54, 64, 93, 53, 12], [100, 54, 93, 12, 53, 64], [100, 54, 93, 12, 64, 53], [100, 54, 93, 53, 12, 64], [100, 54, 93, 53, 64, 12], [100, 54, 93, 64, 12, 53], [100, 54, 93, 64, 53, 12], [100, 64, 12, 53, 54, 93], [100, 64, 12, 53, 93, 54], [100, 64, 12, 54, 53, 93], [100, 64, 12, 54, 93, 53], [100, 64, 12, 93, 53, 54], [100, 64, 12, 93, 54, 53], [100, 64, 53, 12, 54, 93], [100, 64, 53, 12, 93, 54], [100, 64, 53, 54, 12, 93], [100, 64, 53, 54, 93, 12], [100, 64, 53, 93, 12, 54], [100, 64, 53, 93, 54, 12], [100, 64, 54, 12, 53, 93], [100, 64, 54, 12, 93, 53], [100, 64, 54, 53, 12, 93], [100, 64, 54, 53, 93, 12], [100, 64, 54, 93, 12, 53], [100, 64, 54, 93, 53, 12], [100, 64, 93, 12, 53, 54], [100, 64, 93, 12, 54, 53], [100, 64, 93, 53, 12, 54], [100, 64, 93, 53, 54, 12], [100, 64, 93, 54, 12, 53], [100, 64, 93, 54, 53, 12], [100, 93, 12, 53, 54, 64], [100, 93, 12, 53, 64, 54], [100, 93, 12, 54, 53, 64], [100, 93, 12, 54, 64, 53], [100, 93, 12, 64, 53, 54], [100, 93, 12, 64, 54, 53], [100, 93, 53, 12, 54, 64], [100, 93, 53, 12, 64, 54], [100, 93, 53, 54, 12, 64], [100, 93, 53, 54, 64, 12], [100, 93, 53, 64, 12, 54], [100, 93, 53, 64, 54, 12], [100, 93, 54, 12, 53, 64], [100, 93, 54, 12, 64, 53], [100, 93, 54, 53, 12, 64], [100, 93, 54, 53, 64, 12], [100, 93, 54, 64, 12, 53], [100, 93, 54, 64, 53, 12], [100, 93, 64, 12, 53, 54], [100, 93, 64, 12, 54, 53], [100, 93, 64, 53, 12, 54], [100, 93, 64, 53, 54, 12], [100, 93, 64, 54, 12, 53], [100, 93, 64, 54, 53, 12]]
