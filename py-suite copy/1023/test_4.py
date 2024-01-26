
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


def test_4():
    assert solution.Solution().camelMatch(['r0BVi5Fsyp', 'IQV7LaUqC7', 'rKrQY7Lb9Y', 'vpHMwx4Rvt', '9ZjewYk9Hf', '9sl6Blih95'], 'zmHzO3BUPt') == [False, False, False, False, False, False]
