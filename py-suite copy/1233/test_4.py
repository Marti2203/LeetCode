
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


def test_4():
    assert solution.Solution().removeSubfolders(['nkK8eSYirP', 'CCfXqNFbQe', 'B2Q1h3i8rj', 'Q7OdY8VhFi', 'p30wjupNzB', 'XYEmvhOh4M']) == ['B2Q1h3i8rj', 'CCfXqNFbQe', 'Q7OdY8VhFi', 'XYEmvhOh4M', 'nkK8eSYirP', 'p30wjupNzB']
