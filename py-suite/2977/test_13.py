
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


def test_13():
    assert solution.Solution()._getSubToId('e61gqzVEDH', 'CcsxMDM8jC') == {'e': 0, '6': 1, '1': 2, 'g': 3, 'q': 4, 'z': 5, 'V': 6, 'E': 7, 'D': 8, 'H': 9, 'C': 10, 'c': 11, 's': 12, 'x': 13, 'M': 14, '8': 15, 'j': 16}
