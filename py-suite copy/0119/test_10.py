
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
    assert solution.Solution().getRow(77) == [1, 77, 2926, 73150, 1353275, 19757815, 237093780, 2404808340, 21042072975, 161322559475, 1096993404430, 6681687099710, 36749279048405, 183746395242025, 839983521106400, 3527930788646880, 13670731806006660, 49053802362729780, 163512674542432600, 507749884105448600, 1472474663905800940, 3996716944887173980, 10173461314258261040, 24327842273226276400, 54737645114759121900, 116043807643289338428, 232087615286578676856, 438387717763537500728, 782835210292031251300, 1322721562217570045300, 2116354499548112072480, 3208666499314879593760, 4612458092765139416030, 6289715581043371930950, 8139631928409069557700, 10000119226331142599460, 11666805764052999699370, 12928082062869540207410, 13608507434599516007800, 13608507434599516007800, 12928082062869540207410, 11666805764052999699370, 10000119226331142599460, 8139631928409069557700, 6289715581043371930950, 4612458092765139416030, 3208666499314879593760, 2116354499548112072480, 1322721562217570045300, 782835210292031251300, 438387717763537500728, 232087615286578676856, 116043807643289338428, 54737645114759121900, 24327842273226276400, 10173461314258261040, 3996716944887173980, 1472474663905800940, 507749884105448600, 163512674542432600, 49053802362729780, 13670731806006660, 3527930788646880, 839983521106400, 183746395242025, 36749279048405, 6681687099710, 1096993404430, 161322559475, 21042072975, 2404808340, 237093780, 19757815, 1353275, 73150, 2926, 77, 1]
