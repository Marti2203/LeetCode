
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


def test_9():
    assert solution.Solution().subsets([55, 66, 40, 22, 63]) == [[], [55], [55, 66], [55, 66, 40], [55, 66, 40, 22], [55, 66, 40, 22, 63], [55, 66, 40, 63], [55, 66, 22], [55, 66, 22, 63], [55, 66, 63], [55, 40], [55, 40, 22], [55, 40, 22, 63], [55, 40, 63], [55, 22], [55, 22, 63], [55, 63], [66], [66, 40], [66, 40, 22], [66, 40, 22, 63], [66, 40, 63], [66, 22], [66, 22, 63], [66, 63], [40], [40, 22], [40, 22, 63], [40, 63], [22], [22, 63], [63]]
