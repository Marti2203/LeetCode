
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


def test_14():
    assert solution.Solution().topStudents(['DyvXxIp86T', 'asDDMQc8Cb', 'i1jCa4yKA9', 'svcV2oNvbu', 'C9F4rS7w4C'], ['tpwro5A3uR', '7RsMNhGA58'], ['Hw7XJKVBvV', 'niSzeB2CFI', 'f7xkn1t0Kr', 'uZOyEfyXtu', 'adgPDcARNs', '80e4Dfr6Pf'], [17], 86) == [17]
