
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


def test_16():
    assert solution.Solution().subsets([79, 9, 11, 64, 31]) == [[], [79], [79, 9], [79, 9, 11], [79, 9, 11, 64], [79, 9, 11, 64, 31], [79, 9, 11, 31], [79, 9, 64], [79, 9, 64, 31], [79, 9, 31], [79, 11], [79, 11, 64], [79, 11, 64, 31], [79, 11, 31], [79, 64], [79, 64, 31], [79, 31], [9], [9, 11], [9, 11, 64], [9, 11, 64, 31], [9, 11, 31], [9, 64], [9, 64, 31], [9, 31], [11], [11, 64], [11, 64, 31], [11, 31], [64], [64, 31], [31]]
