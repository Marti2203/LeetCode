
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


def test_5():
    assert solution.Solution().findRestaurant(['DC5LmSfed6', 'UPip5rm53z', 'takdRszVXR', 'aIb2XV42Nk', 'qFr8vBDhiz', 'UB9Kre5hNu'], ['A0P8kxqrpa', '1rVCtu727m', 'Uk1T9Y2Iuz', 'Gt51L3gJ5g', 'ozenvobJCy', 'strNizetv6']) == []
