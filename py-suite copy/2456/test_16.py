
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


def test_16():
    assert solution.Solution().mostPopularCreator(['G4VxHaQMig', '5ZmCsSqpLk', 'VysD8TnrBG', 'lKL8rR240a'], ['8EPpIAV0rL', 'e699AlCMVt', 'VnM3nSRtb3', 'mZ6DYUuSAP', 'tJzRw640KQ', 'lARzP2OUcH'], [79, 100, 48, 94, 60]) == [['5ZmCsSqpLk', 'e699AlCMVt']]
