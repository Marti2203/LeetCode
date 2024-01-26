
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


def test_10():
    assert solution.Solution().ambiguousCoordinates('22bziocAg2') == ['(2, bziocAg)', '(2, b.ziocAg)', '(2, bz.iocAg)', '(2, bzi.ocAg)', '(2, bzio.cAg)', '(2, bzioc.Ag)', '(2, bziocA.g)', '(2b, ziocAg)', '(2b, z.iocAg)', '(2b, zi.ocAg)', '(2b, zio.cAg)', '(2b, zioc.Ag)', '(2b, ziocA.g)', '(2.b, ziocAg)', '(2.b, z.iocAg)', '(2.b, zi.ocAg)', '(2.b, zio.cAg)', '(2.b, zioc.Ag)', '(2.b, ziocA.g)', '(2bz, iocAg)', '(2bz, i.ocAg)', '(2bz, io.cAg)', '(2bz, ioc.Ag)', '(2bz, iocA.g)', '(2.bz, iocAg)', '(2.bz, i.ocAg)', '(2.bz, io.cAg)', '(2.bz, ioc.Ag)', '(2.bz, iocA.g)', '(2b.z, iocAg)', '(2b.z, i.ocAg)', '(2b.z, io.cAg)', '(2b.z, ioc.Ag)', '(2b.z, iocA.g)', '(2bzi, ocAg)', '(2bzi, o.cAg)', '(2bzi, oc.Ag)', '(2bzi, ocA.g)', '(2.bzi, ocAg)', '(2.bzi, o.cAg)', '(2.bzi, oc.Ag)', '(2.bzi, ocA.g)', '(2b.zi, ocAg)', '(2b.zi, o.cAg)', '(2b.zi, oc.Ag)', '(2b.zi, ocA.g)', '(2bz.i, ocAg)', '(2bz.i, o.cAg)', '(2bz.i, oc.Ag)', '(2bz.i, ocA.g)', '(2bzio, cAg)', '(2bzio, c.Ag)', '(2bzio, cA.g)', '(2.bzio, cAg)', '(2.bzio, c.Ag)', '(2.bzio, cA.g)', '(2b.zio, cAg)', '(2b.zio, c.Ag)', '(2b.zio, cA.g)', '(2bz.io, cAg)', '(2bz.io, c.Ag)', '(2bz.io, cA.g)', '(2bzi.o, cAg)', '(2bzi.o, c.Ag)', '(2bzi.o, cA.g)', '(2bzioc, Ag)', '(2bzioc, A.g)', '(2.bzioc, Ag)', '(2.bzioc, A.g)', '(2b.zioc, Ag)', '(2b.zioc, A.g)', '(2bz.ioc, Ag)', '(2bz.ioc, A.g)', '(2bzi.oc, Ag)', '(2bzi.oc, A.g)', '(2bzio.c, Ag)', '(2bzio.c, A.g)', '(2bziocA, g)', '(2.bziocA, g)', '(2b.ziocA, g)', '(2bz.iocA, g)', '(2bzi.ocA, g)', '(2bzio.cA, g)', '(2bzioc.A, g)']
