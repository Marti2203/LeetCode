
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
    assert solution.Solution().findReplaceString('xF5amxNN8f', [68, 68, 78, 61, 31], ['dBUjNKkHEV', 'tNB287cwzM', 'lZkYahzBjc', 'hFI3YimIJJ', 'kzJMLQAaJe'], ['cplU6hEBAs', 'A0Sq5bcRgp', 'PDOTPQ6yjs', 'M5KpxCQaoA', 'DNMiHzIyBs', 'oGSmK7K6Gw']) == 'xF5amxNN8f'
