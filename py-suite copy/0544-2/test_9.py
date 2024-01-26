
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


def test_9():
    assert solution.Solution().findContestMatch(79) == '((((((1,79),(39,41)),((19,61),(21,59))),(((9,71),(31,49)),((11,69),(29,51)))),((((4,76),(36,44)),((16,64),(24,56))),(((6,74),(34,46)),((14,66),(26,54))))),(((((2,78),(38,42)),((18,62),(22,58))),(((8,72),(32,48)),((12,68),(28,52)))),((((3,77),(37,43)),((17,63),(23,57))),(((7,73),(33,47)),((13,67),(27,53))))))'
