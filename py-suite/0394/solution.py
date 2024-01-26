
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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if other is None:
            return False
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"




import re

def decodeString(s):
    def decode(s):
        result = []
        while s:
            if s[0].isdigit():
                num = int(s[0])
                s = s[1:]
                result.append(decode(s[:num]))
                s = s[num:]
            elif s[0] == '[':
                result.append(decode(s[1:s.find(']')]))
                s = s[s.find(']') + 1:]
            else:
                result.append(s[0])
                s = s[1:]
        return ''.join(result)
    return decode(s)
