
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
    assert solution.Solution().groupAnagrams(['LJLmvlrgsj', 'MEU9l95TxY', 'mnP7G65Qiq', '8CHFhyhI3o', 'Vh3u49EhEI', 'C6nw66Bw4V']) == dict_values([['LJLmvlrgsj'], ['MEU9l95TxY'], ['mnP7G65Qiq'], ['8CHFhyhI3o'], ['Vh3u49EhEI'], ['C6nw66Bw4V']])
