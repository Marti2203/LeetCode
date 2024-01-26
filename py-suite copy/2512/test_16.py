
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
    assert solution.Solution().topStudents(['Oac346T7MJ', 'pR4DK7R4O2'], ['Ya70YjdH8N', 'DyosFZahTP', 'QVkv5qe797', 'My4ezrn2mT'], ['hKQsXPTzP9', '6e6dSkhnXI'], [76, 26, 4], 23) == [26, 76]
