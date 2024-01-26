
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


def test_14():
    assert solution.Solution().mostPopularCreator(['mdq9inJrN0', 'Kxkv6wSC0f', 'iXyqEDxu7J', 'Oq9T7oQBMx', 'vSq2rplioS'], ['Qt8wNdytDZ', 'pc9paYkyAT', 'OTOf1B68db', 'vA66tuHXjs', 'nMCVEKG5oF', 'O4M4uc62rX'], [34, 12]) == [['mdq9inJrN0', 'Qt8wNdytDZ']]
