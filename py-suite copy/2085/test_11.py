
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


def test_11():
    assert solution.Solution().countWords(['r4l8jfqxO4', 'aMg0sCl71H', 'MY9lkhhDv6', '6gusfcp9wY', 'Rb21PjIgE8'], ['MY35l3AaeL', 'opZbo5zuvz', 'gMBsCr6XXD', 'NtxCLAn9jJ', '6kBrqeoJIx']) == 0
