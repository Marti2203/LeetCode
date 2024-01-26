
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
    assert solution.Solution()._getSubToId('G6f31YccLF', 'hqYnviv5Ez') == {'G': 0, '6': 1, 'f': 2, '3': 3, '1': 4, 'Y': 5, 'c': 6, 'L': 7, 'F': 8, 'h': 9, 'q': 10, 'n': 11, 'v': 12, 'i': 13, '5': 14, 'E': 15, 'z': 16}
