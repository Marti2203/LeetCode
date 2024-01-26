
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


def test_17():
    assert solution.Solution().isPrefixString('0QJwuwmREi', ['frIKPMUQ0T', 'Uaq19CJ6lq', 'I8ZiuH5DB0', 'ckdV4z4oT1', 'nwaq1Gta9R', 'OsVgJmFcw9']) == False
