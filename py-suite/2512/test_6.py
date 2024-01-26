
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


def test_6():
    assert solution.Solution().topStudents(['x0LDyoim6g', 'b02brZ0Hzs', 'JZ6e6yxSTg', 'EdKuSp4pgB', '2pqRUy0tjk'], ['asX7iukDA9', 'YEZH4Ce55G', 'lVr6Os4gUy'], ['Sohr3g1tZE', '53nuZEADyg', 'noUEDoSDAz', 'kg6ZU3jIdQ', '3jU7iqDDXi', 'plaNJYZAH2'], [9, 93, 49], 73) == [9, 49, 93]
