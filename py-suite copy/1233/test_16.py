
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


def test_16():
    assert solution.Solution().removeSubfolders(['3PV9jDK9Go', 'XxU94AIUEn', 'O0YI3baLff', 'Gb6z0NTYoH', 'waaRsz4Yp8', 'h8gfCXX4N9']) == ['3PV9jDK9Go', 'Gb6z0NTYoH', 'O0YI3baLff', 'XxU94AIUEn', 'h8gfCXX4N9', 'waaRsz4Yp8']
