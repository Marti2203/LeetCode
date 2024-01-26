
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


def test_8():
    assert solution.Solution().mostPopularCreator(['N8JpY8Pp5N', 'R6UwyNmAMU', '4NKKMoxSbM', '64iwmOf2HV'], ['zHqdruo1YR', 'T9fj8EI1PN', 'MPkYnGrg79', 'Gn0w8IqZ7R', 'ZNblKLjPKf'], [55, 45, 16, 11, 5, 54]) == [['N8JpY8Pp5N', 'zHqdruo1YR']]
