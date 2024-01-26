
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


def test_1():
    assert solution.Solution()._changeSuffix(['7tSY25OazY', 'R3QbCQ55d6', '8Ajq5Xbv4S', 'kXmGXqaT6Z', 'Tvr4N2iVko', '4aqUmtx5Ba'], 39) == '7tSY25OazYR3QbCQ55d68Ajq5Xbv4SkXmGXqaT6ZTvr4N2iVko4aqUmtx5Ba'
