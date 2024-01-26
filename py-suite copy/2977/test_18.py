
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


def test_18():
    assert solution.Solution()._getSubToId('RIpEGUXr63', 'f6XRDHb9JM') == {'R': 0, 'I': 1, 'p': 2, 'E': 3, 'G': 4, 'U': 5, 'X': 6, 'r': 7, '6': 8, '3': 9, 'f': 10, 'D': 11, 'H': 12, 'b': 13, '9': 14, 'J': 15, 'M': 16}
