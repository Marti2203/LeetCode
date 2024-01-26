
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


def test_3():
    assert solution.Solution().mostPopularCreator(['X8iCMMHlq2', 'hpv5GyO7sj', 'mQ9O9IuY5X', 'wP7ZvmOQT3', 'qrXaibTnwi', 'ToD3m6U4Af'], ['tTvssDthpp', 'cEn17xi7zc', 'gUT5fMhG5y', 'Cr8aMPe4An', 'MzhvukjL7x'], [16, 54, 65, 99]) == [['wP7ZvmOQT3', 'Cr8aMPe4An']]
