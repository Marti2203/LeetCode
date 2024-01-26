
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


def test_7():
    assert solution.Solution()._changeSuffix(['zTUHLy8kuU', 'QPX0lGj0zQ', '36plDmUReP', '0IIbU5yCCU', '6C3Mvz0KF1', 'Xbnl29iF9H'], 16) == 'zTUHLy8kuUQPX0lGj0zQ36plDmUReP0IIbU5yCCU6C3Mvz0KF1Xbnl29iF9H'
