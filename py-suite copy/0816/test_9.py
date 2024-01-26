
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


def test_9():
    assert solution.Solution().ambiguousCoordinates('RIMFe87hMT') == ['(I, MFe87hM)', '(I, M.Fe87hM)', '(I, MF.e87hM)', '(I, MFe.87hM)', '(I, MFe8.7hM)', '(I, MFe87.hM)', '(I, MFe87h.M)', '(IM, Fe87hM)', '(IM, F.e87hM)', '(IM, Fe.87hM)', '(IM, Fe8.7hM)', '(IM, Fe87.hM)', '(IM, Fe87h.M)', '(I.M, Fe87hM)', '(I.M, F.e87hM)', '(I.M, Fe.87hM)', '(I.M, Fe8.7hM)', '(I.M, Fe87.hM)', '(I.M, Fe87h.M)', '(IMF, e87hM)', '(IMF, e.87hM)', '(IMF, e8.7hM)', '(IMF, e87.hM)', '(IMF, e87h.M)', '(I.MF, e87hM)', '(I.MF, e.87hM)', '(I.MF, e8.7hM)', '(I.MF, e87.hM)', '(I.MF, e87h.M)', '(IM.F, e87hM)', '(IM.F, e.87hM)', '(IM.F, e8.7hM)', '(IM.F, e87.hM)', '(IM.F, e87h.M)', '(IMFe, 87hM)', '(IMFe, 8.7hM)', '(IMFe, 87.hM)', '(IMFe, 87h.M)', '(I.MFe, 87hM)', '(I.MFe, 8.7hM)', '(I.MFe, 87.hM)', '(I.MFe, 87h.M)', '(IM.Fe, 87hM)', '(IM.Fe, 8.7hM)', '(IM.Fe, 87.hM)', '(IM.Fe, 87h.M)', '(IMF.e, 87hM)', '(IMF.e, 8.7hM)', '(IMF.e, 87.hM)', '(IMF.e, 87h.M)', '(IMFe8, 7hM)', '(IMFe8, 7.hM)', '(IMFe8, 7h.M)', '(I.MFe8, 7hM)', '(I.MFe8, 7.hM)', '(I.MFe8, 7h.M)', '(IM.Fe8, 7hM)', '(IM.Fe8, 7.hM)', '(IM.Fe8, 7h.M)', '(IMF.e8, 7hM)', '(IMF.e8, 7.hM)', '(IMF.e8, 7h.M)', '(IMFe.8, 7hM)', '(IMFe.8, 7.hM)', '(IMFe.8, 7h.M)', '(IMFe87, hM)', '(IMFe87, h.M)', '(I.MFe87, hM)', '(I.MFe87, h.M)', '(IM.Fe87, hM)', '(IM.Fe87, h.M)', '(IMF.e87, hM)', '(IMF.e87, h.M)', '(IMFe.87, hM)', '(IMFe.87, h.M)', '(IMFe8.7, hM)', '(IMFe8.7, h.M)', '(IMFe87h, M)', '(I.MFe87h, M)', '(IM.Fe87h, M)', '(IMF.e87h, M)', '(IMFe.87h, M)', '(IMFe8.7h, M)', '(IMFe87.h, M)']
