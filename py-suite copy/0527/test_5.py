
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


def test_5():
    assert solution.Solution().wordsAbbreviation(['TUic3VqXMt', 'Qvb5SGFEm5', 'N2N6LZ56EU', 'Xv45lQTpAT', '1r0ZHbOtla', 'Q3bT7z1Had']) == ['T8t', 'Q85', 'N8U', 'X8T', '18a', 'Q8d']
