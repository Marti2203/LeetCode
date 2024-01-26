
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


def test_15():
    assert solution.Solution()._getSubToId('Ikz2Se8VLw', 'q9xHPIsuBI') == {'I': 0, 'k': 1, 'z': 2, '2': 3, 'S': 4, 'e': 5, '8': 6, 'V': 7, 'L': 8, 'w': 9, 'q': 10, '9': 11, 'x': 12, 'H': 13, 'P': 14, 's': 15, 'u': 16, 'B': 17}
