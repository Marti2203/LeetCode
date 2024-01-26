
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
    assert solution.Solution().subsetsWithDup([63, 46, 68, 45, 48]) == [[], [45], [45, 46], [45, 46, 48], [45, 46, 48, 63], [45, 46, 48, 63, 68], [45, 46, 48, 68], [45, 46, 63], [45, 46, 63, 68], [45, 46, 68], [45, 48], [45, 48, 63], [45, 48, 63, 68], [45, 48, 68], [45, 63], [45, 63, 68], [45, 68], [46], [46, 48], [46, 48, 63], [46, 48, 63, 68], [46, 48, 68], [46, 63], [46, 63, 68], [46, 68], [48], [48, 63], [48, 63, 68], [48, 68], [63], [63, 68], [68]]
