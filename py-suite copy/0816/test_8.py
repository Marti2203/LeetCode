
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


def test_8():
    assert solution.Solution().ambiguousCoordinates('EfJn9l6qnR') == ['(f, Jn9l6qn)', '(f, J.n9l6qn)', '(f, Jn.9l6qn)', '(f, Jn9.l6qn)', '(f, Jn9l.6qn)', '(f, Jn9l6.qn)', '(f, Jn9l6q.n)', '(fJ, n9l6qn)', '(fJ, n.9l6qn)', '(fJ, n9.l6qn)', '(fJ, n9l.6qn)', '(fJ, n9l6.qn)', '(fJ, n9l6q.n)', '(f.J, n9l6qn)', '(f.J, n.9l6qn)', '(f.J, n9.l6qn)', '(f.J, n9l.6qn)', '(f.J, n9l6.qn)', '(f.J, n9l6q.n)', '(fJn, 9l6qn)', '(fJn, 9.l6qn)', '(fJn, 9l.6qn)', '(fJn, 9l6.qn)', '(fJn, 9l6q.n)', '(f.Jn, 9l6qn)', '(f.Jn, 9.l6qn)', '(f.Jn, 9l.6qn)', '(f.Jn, 9l6.qn)', '(f.Jn, 9l6q.n)', '(fJ.n, 9l6qn)', '(fJ.n, 9.l6qn)', '(fJ.n, 9l.6qn)', '(fJ.n, 9l6.qn)', '(fJ.n, 9l6q.n)', '(fJn9, l6qn)', '(fJn9, l.6qn)', '(fJn9, l6.qn)', '(fJn9, l6q.n)', '(f.Jn9, l6qn)', '(f.Jn9, l.6qn)', '(f.Jn9, l6.qn)', '(f.Jn9, l6q.n)', '(fJ.n9, l6qn)', '(fJ.n9, l.6qn)', '(fJ.n9, l6.qn)', '(fJ.n9, l6q.n)', '(fJn.9, l6qn)', '(fJn.9, l.6qn)', '(fJn.9, l6.qn)', '(fJn.9, l6q.n)', '(fJn9l, 6qn)', '(fJn9l, 6.qn)', '(fJn9l, 6q.n)', '(f.Jn9l, 6qn)', '(f.Jn9l, 6.qn)', '(f.Jn9l, 6q.n)', '(fJ.n9l, 6qn)', '(fJ.n9l, 6.qn)', '(fJ.n9l, 6q.n)', '(fJn.9l, 6qn)', '(fJn.9l, 6.qn)', '(fJn.9l, 6q.n)', '(fJn9.l, 6qn)', '(fJn9.l, 6.qn)', '(fJn9.l, 6q.n)', '(fJn9l6, qn)', '(fJn9l6, q.n)', '(f.Jn9l6, qn)', '(f.Jn9l6, q.n)', '(fJ.n9l6, qn)', '(fJ.n9l6, q.n)', '(fJn.9l6, qn)', '(fJn.9l6, q.n)', '(fJn9.l6, qn)', '(fJn9.l6, q.n)', '(fJn9l.6, qn)', '(fJn9l.6, q.n)', '(fJn9l6q, n)', '(f.Jn9l6q, n)', '(fJ.n9l6q, n)', '(fJn.9l6q, n)', '(fJn9.l6q, n)', '(fJn9l.6q, n)', '(fJn9l6.q, n)']
