
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


def test_7():
    assert solution.Solution().topStudents(['CGuqo8M2TI', 'FHfNSqIBox', '7aucJhA36M', 'VVVYFqjHIe', 'A8mVZP6a1C'], ['ynv8Q4gL0m', 'dT70AMJvzb', 'z5nJrfn7nv'], ['8qRaIqZJCz', 'ohJfg6y1mf', 'azH3CHRaMx', 'ICA3snl1j9'], [21, 78, 72, 92, 79, 52], 9) == [21, 72, 78, 92]
