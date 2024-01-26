
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
    assert solution.Solution().topStudents(['xVYAhvgkog', '2jICg6Colp', 'GidBi5sTzi', 'nmQMgabrT3'], ['ZNVkI4GnRR', '8AVqGQIszm', 'U4uzeDiyxJ', 'ktG8n4Hb1j', 'wmOw1w2qyj', 'NrjVFmDO7Y'], ['a2aiEpMzuD', '6avXh2ZS8e', 'NPqhLTjgo1'], [51], 29) == [51]
