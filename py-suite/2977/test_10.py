
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


def test_10():
    assert solution.Solution()._getSubToId('ftoFmQ6jkZ', 'C1jqygTPXM') == {'f': 0, 't': 1, 'o': 2, 'F': 3, 'm': 4, 'Q': 5, '6': 6, 'j': 7, 'k': 8, 'Z': 9, 'C': 10, '1': 11, 'q': 12, 'y': 13, 'g': 14, 'T': 15, 'P': 16, 'X': 17, 'M': 18}
