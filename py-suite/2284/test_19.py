
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


def test_19():
    assert solution.Solution().largestWordCount(['V4lxTPNdPm', 't2T5b6Xpgy', 'Fa1cM5deud', 'eeS86Igoh8', '0bRE7puUX4', 'M3gRKrPBd7'], ['zUZUvF2mjX']) == 'zUZUvF2mjX'
