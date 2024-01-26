
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
    assert solution.Solution().ambiguousCoordinates('SGPaTxY2L9') == ['(G, PaTxY2L)', '(G, P.aTxY2L)', '(G, Pa.TxY2L)', '(G, PaT.xY2L)', '(G, PaTx.Y2L)', '(G, PaTxY.2L)', '(G, PaTxY2.L)', '(GP, aTxY2L)', '(GP, a.TxY2L)', '(GP, aT.xY2L)', '(GP, aTx.Y2L)', '(GP, aTxY.2L)', '(GP, aTxY2.L)', '(G.P, aTxY2L)', '(G.P, a.TxY2L)', '(G.P, aT.xY2L)', '(G.P, aTx.Y2L)', '(G.P, aTxY.2L)', '(G.P, aTxY2.L)', '(GPa, TxY2L)', '(GPa, T.xY2L)', '(GPa, Tx.Y2L)', '(GPa, TxY.2L)', '(GPa, TxY2.L)', '(G.Pa, TxY2L)', '(G.Pa, T.xY2L)', '(G.Pa, Tx.Y2L)', '(G.Pa, TxY.2L)', '(G.Pa, TxY2.L)', '(GP.a, TxY2L)', '(GP.a, T.xY2L)', '(GP.a, Tx.Y2L)', '(GP.a, TxY.2L)', '(GP.a, TxY2.L)', '(GPaT, xY2L)', '(GPaT, x.Y2L)', '(GPaT, xY.2L)', '(GPaT, xY2.L)', '(G.PaT, xY2L)', '(G.PaT, x.Y2L)', '(G.PaT, xY.2L)', '(G.PaT, xY2.L)', '(GP.aT, xY2L)', '(GP.aT, x.Y2L)', '(GP.aT, xY.2L)', '(GP.aT, xY2.L)', '(GPa.T, xY2L)', '(GPa.T, x.Y2L)', '(GPa.T, xY.2L)', '(GPa.T, xY2.L)', '(GPaTx, Y2L)', '(GPaTx, Y.2L)', '(GPaTx, Y2.L)', '(G.PaTx, Y2L)', '(G.PaTx, Y.2L)', '(G.PaTx, Y2.L)', '(GP.aTx, Y2L)', '(GP.aTx, Y.2L)', '(GP.aTx, Y2.L)', '(GPa.Tx, Y2L)', '(GPa.Tx, Y.2L)', '(GPa.Tx, Y2.L)', '(GPaT.x, Y2L)', '(GPaT.x, Y.2L)', '(GPaT.x, Y2.L)', '(GPaTxY, 2L)', '(GPaTxY, 2.L)', '(G.PaTxY, 2L)', '(G.PaTxY, 2.L)', '(GP.aTxY, 2L)', '(GP.aTxY, 2.L)', '(GPa.TxY, 2L)', '(GPa.TxY, 2.L)', '(GPaT.xY, 2L)', '(GPaT.xY, 2.L)', '(GPaTx.Y, 2L)', '(GPaTx.Y, 2.L)', '(GPaTxY2, L)', '(G.PaTxY2, L)', '(GP.aTxY2, L)', '(GPa.TxY2, L)', '(GPaT.xY2, L)', '(GPaTx.Y2, L)', '(GPaTxY.2, L)']
