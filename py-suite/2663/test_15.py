
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


def test_15():
    assert solution.Solution()._changeSuffix(['9556i67zlY', 'HtBMLdbhkk', 'cnT1ss5TCx', 't4kz56Pddl', 'X5o2MA5ENb', '8cHkd2Vaff'], 48) == '9556i67zlYHtBMLdbhkkcnT1ss5TCxt4kz56PddlX5o2MA5ENb8cHkd2Vaff'
