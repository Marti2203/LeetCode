
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


def test_14():
    assert solution.Solution().getRow(95) == [1, 95, 4465, 138415, 3183545, 57940519, 869107785, 11050084695, 121550931645, 1174992339235, 10104934117421, 78083581816435, 546585072715045, 3489735464257595, 20439879147794485, 110375347398090219, 551876736990451095, 2564603660132096265, 11113282527239083815, 45038039715653129145, 171144550919481890751, 611230538998149609825, 2055957267539230505775, 6525429588276688127025, 19576288764830064381075, 55596660092117382842253, 149683315632623723036835, 382524028838927292205245, 928986927180251995355595, 2146280142106099437545685, 4721816312633418762600507, 9900582591005555469968805, 19801165182011110939937610, 37802224438384848158062710, 68933468093525311347055530, 120141187248715542633439638, 200235312081192571055732730, 319294146291631397088871110, 487343696971437395556698010, 712271557112100808890558630, 997180179956941132446782082, 1337680729210530787428610110, 1719875223270682440979641570, 2119846205426655101672581470, 2505272788231501483794869010, 2839309159995701681634184878, 3086205608690980088732809650, 3217533506933149454210801550, 3217533506933149454210801550, 3086205608690980088732809650, 2839309159995701681634184878, 2505272788231501483794869010, 2119846205426655101672581470, 1719875223270682440979641570, 1337680729210530787428610110, 997180179956941132446782082, 712271557112100808890558630, 487343696971437395556698010, 319294146291631397088871110, 200235312081192571055732730, 120141187248715542633439638, 68933468093525311347055530, 37802224438384848158062710, 19801165182011110939937610, 9900582591005555469968805, 4721816312633418762600507, 2146280142106099437545685, 928986927180251995355595, 382524028838927292205245, 149683315632623723036835, 55596660092117382842253, 19576288764830064381075, 6525429588276688127025, 2055957267539230505775, 611230538998149609825, 171144550919481890751, 45038039715653129145, 11113282527239083815, 2564603660132096265, 551876736990451095, 110375347398090219, 20439879147794485, 3489735464257595, 546585072715045, 78083581816435, 10104934117421, 1174992339235, 121550931645, 11050084695, 869107785, 57940519, 3183545, 138415, 4465, 95, 1]
