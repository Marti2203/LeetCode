
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
    assert solution.Solution().numSmallerByFrequency(['Tybhm1FsH6', '88ZxDB5RSw', 'LGnuk8KivZ', 'NEkaUHXiqf', '7jEmYfA9vb'], ['ncw5hoJqBA', 'P7rCL8IkB0', 'JhLgDrxCzk', 'cEuvBl4Zpx', '3Zd2h0hzKO', 'AR8j2jofFQ']) == [0, 0, 0, 0, 0]
