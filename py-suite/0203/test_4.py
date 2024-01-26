
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


def test_4():
    assert solution.Solution().removeElements(ListNode(5, ListNode(25, ListNode(99, ListNode(1, ListNode(48, ListNode(10, ListNode(40, ListNode(98, None)))))))), 97) == ListNode(5, ListNode(25, ListNode(99, ListNode(1, ListNode(48, ListNode(10, ListNode(40, ListNode(98, None))))))))
