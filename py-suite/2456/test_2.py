
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


def test_2():
    assert solution.Solution().mostPopularCreator(['BbGyRwVikz', 'NGL7MmoELG', 'SO8xXBZNTG', 'MCKj6ru7dx', 'fyHn0Rpw3U'], ['b3y8GswdFy', 'TqUH3SzY2Q', 'hvI5Mj5u4J', 'jp4jeLDl6m', 'LcTarQPKM1'], [69, 22, 81]) == [['SO8xXBZNTG', 'hvI5Mj5u4J']]
