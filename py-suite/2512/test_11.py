
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


def test_11():
    assert solution.Solution().topStudents(['bkZYqRUy0t', '5wTJQbI4qY', 'D6EKgdCKNc'], ['aI2OaEzaME', 'D7hSZu30xX'], ['tZ6sT1A8yE', 'DSOCt8bSQp', 'VKYXI4ukKj', 'pDgn4izTxY', 'LnXLhdpCdq', 'IeukBG6iun'], [35, 59, 33, 58, 81], 95) == [33, 35, 58, 59, 81]
