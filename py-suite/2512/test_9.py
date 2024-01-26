
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
    assert solution.Solution().topStudents(['i28exdwVI0', 'NFlDqr6mfH', 'l3FfXtj7FH', 'EI8Twb4k3J', 'p0ZiEZJ4Nk'], ['nKD51jXB8R', 'w9AYQ8bcxD', 'cM1ZPyP0ss', 'ZIdJ5uiC6Y', 'oKTgYcQBub', 'PSBPZhwfn8'], ['cICQdrnSj6'], [59, 15, 48, 23, 75], 64) == [59]
