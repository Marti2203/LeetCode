
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
    assert solution.Solution().findReplaceString('A0BpiNBIBU', [73, 22, 60, 56, 45, 20], ['uHLygaIidY', 'xUma3BC7eg', 'VxwYqeEFnG', '835qvhLZiO'], ['vBjCyGmXvX', 'TF1ULC5UFD', 'CTVmKxhbgT']) == 'A0BpiNBIBU'
