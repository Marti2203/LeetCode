
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
    assert solution.Solution().mostPopularCreator(['fxfTJgCKkX', 'K68IZdjHlm', 'JuGCssBltN', 'E4MjfzRg0n'], ['JA2Cvt72OD', 'G9iwp4w7bj'], [14, 4, 5, 62]) == [['fxfTJgCKkX', 'JA2Cvt72OD']]
