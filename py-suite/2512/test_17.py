
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
    assert solution.Solution().topStudents(['cs4PRVOALL'], ['ddZ1sACyIG'], ['XdhiNFm8iu', 'keC0cVYt7g', 'OYfG68yass', 'UHXdTvy9yb', 'hj5h1MYBfz', 'hCiSk0I3g7'], [30], 61) == [30]
