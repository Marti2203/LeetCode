
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
    assert solution.Solution().topKFrequent(['cnEyNVk1dU', 'My9F1nx9jY', '1vTd2onvRB', 'eMpgfY3mnb', 'dVShXKpsX9'], 58) == ['1vTd2onvRB', 'My9F1nx9jY', 'cnEyNVk1dU', 'dVShXKpsX9', 'eMpgfY3mnb']
