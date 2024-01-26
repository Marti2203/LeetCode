
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


def test_1():
    assert solution.Solution().topStudents(['feBYpk7R4i', 'klg8MmY61u', 'y0wzLGDxR1'], ['Lk7ftBUxpG', 'MLQ7Bo7uiF', 'yUuGYvp0Hk', 'ZufknPN5xT'], ['6AJZsJNOuq', '85lkfvlexf'], [68, 35], 2) == [35, 68]
