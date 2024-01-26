
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


def test_12():
    assert solution.Solution().mostPopularCreator(['JsXs0Ri1Qo', 'ZBGcrphY6V', 'ILFJh5DbNs', 'DQ1bYs45Si'], ['k5fe3Jz3yi', 'l3z6OcAoa7', 'lN32HouKko', '7crAGktmLC', 'ZOFM73bb6A', '3wPd7CGA1t'], [35, 42]) == [['ZBGcrphY6V', 'l3z6OcAoa7']]
