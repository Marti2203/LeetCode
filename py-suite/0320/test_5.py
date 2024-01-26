
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
    assert solution.Solution().generateAbbreviations('LqHIj16upV') == ['10', '9V', '8p1', '8pV', '7u2', '7u1V', '7up1', '7upV', '663', '662V', '661p1', '661pV', '66u2', '66u1V', '66up1', '66upV', '514', '513V', '512p1', '512pV', '511u2', '511u1V', '511up1', '511upV', '5163', '5162V', '5161p1', '5161pV', '516u2', '516u1V', '516up1', '516upV', '4j5', '4j4V', '4j3p1', '4j3pV', '4j2u2', '4j2u1V', '4j2up1', '4j2upV', '4j163', '4j162V', '4j161p1', '4j161pV', '4j16u2', '4j16u1V', '4j16up1', '4j16upV', '4j14', '4j13V', '4j12p1', '4j12pV', '4j11u2', '4j11u1V', '4j11up1', '4j11upV', '4j163', '4j162V', '4j161p1', '4j161pV', '4j16u2', '4j16u1V', '4j16up1', '4j16upV', '3I6', '3I5V', '3I4p1', '3I4pV', '3I3u2', '3I3u1V', '3I3up1', '3I3upV', '3I263', '3I262V', '3I261p1', '3I261pV', '3I26u2', '3I26u1V', '3I26up1', '3I26upV', '3I114', '3I113V', '3I112p1', '3I112pV', '3I111u2', '3I111u1V', '3I111up1', '3I111upV', '3I1163', '3I1162V', '3I1161p1', '3I1161pV', '3I116u2', '3I116u1V', '3I116up1', '3I116upV', '3Ij5', '3Ij4V', '3Ij3p1', '3Ij3pV', '3Ij2u2', '3Ij2u1V', '3Ij2up1', '3Ij2upV', '3Ij163', '3Ij162V', '3Ij161p1', '3Ij161pV', '3Ij16u2', '3Ij16u1V', '3Ij16up1', '3Ij16upV', '3Ij14', '3Ij13V', '3Ij12p1', '3Ij12pV', '3Ij11u2', '3Ij11u1V', '3Ij11up1', '3Ij11upV', '3Ij163', '3Ij162V', '3Ij161p1', '3Ij161pV', '3Ij16u2', '3Ij16u1V', '3Ij16up1', '3Ij16upV', '2H7', '2H6V', '2H5p1', '2H5pV', '2H4u2', '2H4u1V', '2H4up1', '2H4upV', '2H363', '2H362V', '2H361p1', '2H361pV', '2H36u2', '2H36u1V', '2H36up1', '2H36upV', '2H214', '2H213V', '2H212p1', '2H212pV', '2H211u2', '2H211u1V', '2H211up1', '2H211upV', '2H2163', '2H2162V', '2H2161p1', '2H2161pV', '2H216u2', '2H216u1V', '2H216up1', '2H216upV', '2H1j5', '2H1j4V', '2H1j3p1', '2H1j3pV', '2H1j2u2', '2H1j2u1V', '2H1j2up1', '2H1j2upV', '2H1j163', '2H1j162V', '2H1j161p1', '2H1j161pV', '2H1j16u2', '2H1j16u1V', '2H1j16up1', '2H1j16upV', '2H1j14', '2H1j13V', '2H1j12p1', '2H1j12pV', '2H1j11u2', '2H1j11u1V', '2H1j11up1', '2H1j11upV', '2H1j163', '2H1j162V', '2H1j161p1', '2H1j161pV', '2H1j16u2', '2H1j16u1V', '2H1j16up1', '2H1j16upV', '2HI6', '2HI5V', '2HI4p1', '2HI4pV', '2HI3u2', '2HI3u1V', '2HI3up1', '2HI3upV', '2HI263', '2HI262V', '2HI261p1', '2HI261pV', '2HI26u2', '2HI26u1V', '2HI26up1', '2HI26upV', '2HI114', '2HI113V', '2HI112p1', '2HI112pV', '2HI111u2', '2HI111u1V', '2HI111up1', '2HI111upV', '2HI1163', '2HI1162V', '2HI1161p1', '2HI1161pV', '2HI116u2', '2HI116u1V', '2HI116up1', '2HI116upV', '2HIj5', '2HIj4V', '2HIj3p1', '2HIj3pV', '2HIj2u2', '2HIj2u1V', '2HIj2up1', '2HIj2upV', '2HIj163', '2HIj162V', '2HIj161p1', '2HIj161pV', '2HIj16u2', '2HIj16u1V', '2HIj16up1', '2HIj16upV', '2HIj14', '2HIj13V', '2HIj12p1', '2HIj12pV', '2HIj11u2', '2HIj11u1V', '2HIj11up1', '2HIj11upV', '2HIj163', '2HIj162V', '2HIj161p1', '2HIj161pV', '2HIj16u2', '2HIj16u1V', '2HIj16up1', '2HIj16upV', '1q8', '1q7V', '1q6p1', '1q6pV', '1q5u2', '1q5u1V', '1q5up1', '1q5upV', '1q463', '1q462V', '1q461p1', '1q461pV', '1q46u2', '1q46u1V', '1q46up1', '1q46upV', '1q314', '1q313V', '1q312p1', '1q312pV', '1q311u2', '1q311u1V', '1q311up1', '1q311upV', '1q3163', '1q3162V', '1q3161p1', '1q3161pV', '1q316u2', '1q316u1V', '1q316up1', '1q316upV', '1q2j5', '1q2j4V', '1q2j3p1', '1q2j3pV', '1q2j2u2', '1q2j2u1V', '1q2j2up1', '1q2j2upV', '1q2j163', '1q2j162V', '1q2j161p1', '1q2j161pV', '1q2j16u2', '1q2j16u1V', '1q2j16up1', '1q2j16upV', '1q2j14', '1q2j13V', '1q2j12p1', '1q2j12pV', '1q2j11u2', '1q2j11u1V', '1q2j11up1', '1q2j11upV', '1q2j163', '1q2j162V', '1q2j161p1', '1q2j161pV', '1q2j16u2', '1q2j16u1V', '1q2j16up1', '1q2j16upV', '1q1I6', '1q1I5V', '1q1I4p1', '1q1I4pV', '1q1I3u2', '1q1I3u1V', '1q1I3up1', '1q1I3upV', '1q1I263', '1q1I262V', '1q1I261p1', '1q1I261pV', '1q1I26u2', '1q1I26u1V', '1q1I26up1', '1q1I26upV', '1q1I114', '1q1I113V', '1q1I112p1', '1q1I112pV', '1q1I111u2', '1q1I111u1V', '1q1I111up1', '1q1I111upV', '1q1I1163', '1q1I1162V', '1q1I1161p1', '1q1I1161pV', '1q1I116u2', '1q1I116u1V', '1q1I116up1', '1q1I116upV', '1q1Ij5', '1q1Ij4V', '1q1Ij3p1', '1q1Ij3pV', '1q1Ij2u2', '1q1Ij2u1V', '1q1Ij2up1', '1q1Ij2upV', '1q1Ij163', '1q1Ij162V', '1q1Ij161p1', '1q1Ij161pV', '1q1Ij16u2', '1q1Ij16u1V', '1q1Ij16up1', '1q1Ij16upV', '1q1Ij14', '1q1Ij13V', '1q1Ij12p1', '1q1Ij12pV', '1q1Ij11u2', '1q1Ij11u1V', '1q1Ij11up1', '1q1Ij11upV', '1q1Ij163', '1q1Ij162V', '1q1Ij161p1', '1q1Ij161pV', '1q1Ij16u2', '1q1Ij16u1V', '1q1Ij16up1', '1q1Ij16upV', '1qH7', '1qH6V', '1qH5p1', '1qH5pV', '1qH4u2', '1qH4u1V', '1qH4up1', '1qH4upV', '1qH363', '1qH362V', '1qH361p1', '1qH361pV', '1qH36u2', '1qH36u1V', '1qH36up1', '1qH36upV', '1qH214', '1qH213V', '1qH212p1', '1qH212pV', '1qH211u2', '1qH211u1V', '1qH211up1', '1qH211upV', '1qH2163', '1qH2162V', '1qH2161p1', '1qH2161pV', '1qH216u2', '1qH216u1V', '1qH216up1', '1qH216upV', '1qH1j5', '1qH1j4V', '1qH1j3p1', '1qH1j3pV', '1qH1j2u2', '1qH1j2u1V', '1qH1j2up1', '1qH1j2upV', '1qH1j163', '1qH1j162V', '1qH1j161p1', '1qH1j161pV', '1qH1j16u2', '1qH1j16u1V', '1qH1j16up1', '1qH1j16upV', '1qH1j14', '1qH1j13V', '1qH1j12p1', '1qH1j12pV', '1qH1j11u2', '1qH1j11u1V', '1qH1j11up1', '1qH1j11upV', '1qH1j163', '1qH1j162V', '1qH1j161p1', '1qH1j161pV', '1qH1j16u2', '1qH1j16u1V', '1qH1j16up1', '1qH1j16upV', '1qHI6', '1qHI5V', '1qHI4p1', '1qHI4pV', '1qHI3u2', '1qHI3u1V', '1qHI3up1', '1qHI3upV', '1qHI263', '1qHI262V', '1qHI261p1', '1qHI261pV', '1qHI26u2', '1qHI26u1V', '1qHI26up1', '1qHI26upV', '1qHI114', '1qHI113V', '1qHI112p1', '1qHI112pV', '1qHI111u2', '1qHI111u1V', '1qHI111up1', '1qHI111upV', '1qHI1163', '1qHI1162V', '1qHI1161p1', '1qHI1161pV', '1qHI116u2', '1qHI116u1V', '1qHI116up1', '1qHI116upV', '1qHIj5', '1qHIj4V', '1qHIj3p1', '1qHIj3pV', '1qHIj2u2', '1qHIj2u1V', '1qHIj2up1', '1qHIj2upV', '1qHIj163', '1qHIj162V', '1qHIj161p1', '1qHIj161pV', '1qHIj16u2', '1qHIj16u1V', '1qHIj16up1', '1qHIj16upV', '1qHIj14', '1qHIj13V', '1qHIj12p1', '1qHIj12pV', '1qHIj11u2', '1qHIj11u1V', '1qHIj11up1', '1qHIj11upV', '1qHIj163', '1qHIj162V', '1qHIj161p1', '1qHIj161pV', '1qHIj16u2', '1qHIj16u1V', '1qHIj16up1', '1qHIj16upV', 'L9', 'L8V', 'L7p1', 'L7pV', 'L6u2', 'L6u1V', 'L6up1', 'L6upV', 'L563', 'L562V', 'L561p1', 'L561pV', 'L56u2', 'L56u1V', 'L56up1', 'L56upV', 'L414', 'L413V', 'L412p1', 'L412pV', 'L411u2', 'L411u1V', 'L411up1', 'L411upV', 'L4163', 'L4162V', 'L4161p1', 'L4161pV', 'L416u2', 'L416u1V', 'L416up1', 'L416upV', 'L3j5', 'L3j4V', 'L3j3p1', 'L3j3pV', 'L3j2u2', 'L3j2u1V', 'L3j2up1', 'L3j2upV', 'L3j163', 'L3j162V', 'L3j161p1', 'L3j161pV', 'L3j16u2', 'L3j16u1V', 'L3j16up1', 'L3j16upV', 'L3j14', 'L3j13V', 'L3j12p1', 'L3j12pV', 'L3j11u2', 'L3j11u1V', 'L3j11up1', 'L3j11upV', 'L3j163', 'L3j162V', 'L3j161p1', 'L3j161pV', 'L3j16u2', 'L3j16u1V', 'L3j16up1', 'L3j16upV', 'L2I6', 'L2I5V', 'L2I4p1', 'L2I4pV', 'L2I3u2', 'L2I3u1V', 'L2I3up1', 'L2I3upV', 'L2I263', 'L2I262V', 'L2I261p1', 'L2I261pV', 'L2I26u2', 'L2I26u1V', 'L2I26up1', 'L2I26upV', 'L2I114', 'L2I113V', 'L2I112p1', 'L2I112pV', 'L2I111u2', 'L2I111u1V', 'L2I111up1', 'L2I111upV', 'L2I1163', 'L2I1162V', 'L2I1161p1', 'L2I1161pV', 'L2I116u2', 'L2I116u1V', 'L2I116up1', 'L2I116upV', 'L2Ij5', 'L2Ij4V', 'L2Ij3p1', 'L2Ij3pV', 'L2Ij2u2', 'L2Ij2u1V', 'L2Ij2up1', 'L2Ij2upV', 'L2Ij163', 'L2Ij162V', 'L2Ij161p1', 'L2Ij161pV', 'L2Ij16u2', 'L2Ij16u1V', 'L2Ij16up1', 'L2Ij16upV', 'L2Ij14', 'L2Ij13V', 'L2Ij12p1', 'L2Ij12pV', 'L2Ij11u2', 'L2Ij11u1V', 'L2Ij11up1', 'L2Ij11upV', 'L2Ij163', 'L2Ij162V', 'L2Ij161p1', 'L2Ij161pV', 'L2Ij16u2', 'L2Ij16u1V', 'L2Ij16up1', 'L2Ij16upV', 'L1H7', 'L1H6V', 'L1H5p1', 'L1H5pV', 'L1H4u2', 'L1H4u1V', 'L1H4up1', 'L1H4upV', 'L1H363', 'L1H362V', 'L1H361p1', 'L1H361pV', 'L1H36u2', 'L1H36u1V', 'L1H36up1', 'L1H36upV', 'L1H214', 'L1H213V', 'L1H212p1', 'L1H212pV', 'L1H211u2', 'L1H211u1V', 'L1H211up1', 'L1H211upV', 'L1H2163', 'L1H2162V', 'L1H2161p1', 'L1H2161pV', 'L1H216u2', 'L1H216u1V', 'L1H216up1', 'L1H216upV', 'L1H1j5', 'L1H1j4V', 'L1H1j3p1', 'L1H1j3pV', 'L1H1j2u2', 'L1H1j2u1V', 'L1H1j2up1', 'L1H1j2upV', 'L1H1j163', 'L1H1j162V', 'L1H1j161p1', 'L1H1j161pV', 'L1H1j16u2', 'L1H1j16u1V', 'L1H1j16up1', 'L1H1j16upV', 'L1H1j14', 'L1H1j13V', 'L1H1j12p1', 'L1H1j12pV', 'L1H1j11u2', 'L1H1j11u1V', 'L1H1j11up1', 'L1H1j11upV', 'L1H1j163', 'L1H1j162V', 'L1H1j161p1', 'L1H1j161pV', 'L1H1j16u2', 'L1H1j16u1V', 'L1H1j16up1', 'L1H1j16upV', 'L1HI6', 'L1HI5V', 'L1HI4p1', 'L1HI4pV', 'L1HI3u2', 'L1HI3u1V', 'L1HI3up1', 'L1HI3upV', 'L1HI263', 'L1HI262V', 'L1HI261p1', 'L1HI261pV', 'L1HI26u2', 'L1HI26u1V', 'L1HI26up1', 'L1HI26upV', 'L1HI114', 'L1HI113V', 'L1HI112p1', 'L1HI112pV', 'L1HI111u2', 'L1HI111u1V', 'L1HI111up1', 'L1HI111upV', 'L1HI1163', 'L1HI1162V', 'L1HI1161p1', 'L1HI1161pV', 'L1HI116u2', 'L1HI116u1V', 'L1HI116up1', 'L1HI116upV', 'L1HIj5', 'L1HIj4V', 'L1HIj3p1', 'L1HIj3pV', 'L1HIj2u2', 'L1HIj2u1V', 'L1HIj2up1', 'L1HIj2upV', 'L1HIj163', 'L1HIj162V', 'L1HIj161p1', 'L1HIj161pV', 'L1HIj16u2', 'L1HIj16u1V', 'L1HIj16up1', 'L1HIj16upV', 'L1HIj14', 'L1HIj13V', 'L1HIj12p1', 'L1HIj12pV', 'L1HIj11u2', 'L1HIj11u1V', 'L1HIj11up1', 'L1HIj11upV', 'L1HIj163', 'L1HIj162V', 'L1HIj161p1', 'L1HIj161pV', 'L1HIj16u2', 'L1HIj16u1V', 'L1HIj16up1', 'L1HIj16upV', 'Lq8', 'Lq7V', 'Lq6p1', 'Lq6pV', 'Lq5u2', 'Lq5u1V', 'Lq5up1', 'Lq5upV', 'Lq463', 'Lq462V', 'Lq461p1', 'Lq461pV', 'Lq46u2', 'Lq46u1V', 'Lq46up1', 'Lq46upV', 'Lq314', 'Lq313V', 'Lq312p1', 'Lq312pV', 'Lq311u2', 'Lq311u1V', 'Lq311up1', 'Lq311upV', 'Lq3163', 'Lq3162V', 'Lq3161p1', 'Lq3161pV', 'Lq316u2', 'Lq316u1V', 'Lq316up1', 'Lq316upV', 'Lq2j5', 'Lq2j4V', 'Lq2j3p1', 'Lq2j3pV', 'Lq2j2u2', 'Lq2j2u1V', 'Lq2j2up1', 'Lq2j2upV', 'Lq2j163', 'Lq2j162V', 'Lq2j161p1', 'Lq2j161pV', 'Lq2j16u2', 'Lq2j16u1V', 'Lq2j16up1', 'Lq2j16upV', 'Lq2j14', 'Lq2j13V', 'Lq2j12p1', 'Lq2j12pV', 'Lq2j11u2', 'Lq2j11u1V', 'Lq2j11up1', 'Lq2j11upV', 'Lq2j163', 'Lq2j162V', 'Lq2j161p1', 'Lq2j161pV', 'Lq2j16u2', 'Lq2j16u1V', 'Lq2j16up1', 'Lq2j16upV', 'Lq1I6', 'Lq1I5V', 'Lq1I4p1', 'Lq1I4pV', 'Lq1I3u2', 'Lq1I3u1V', 'Lq1I3up1', 'Lq1I3upV', 'Lq1I263', 'Lq1I262V', 'Lq1I261p1', 'Lq1I261pV', 'Lq1I26u2', 'Lq1I26u1V', 'Lq1I26up1', 'Lq1I26upV', 'Lq1I114', 'Lq1I113V', 'Lq1I112p1', 'Lq1I112pV', 'Lq1I111u2', 'Lq1I111u1V', 'Lq1I111up1', 'Lq1I111upV', 'Lq1I1163', 'Lq1I1162V', 'Lq1I1161p1', 'Lq1I1161pV', 'Lq1I116u2', 'Lq1I116u1V', 'Lq1I116up1', 'Lq1I116upV', 'Lq1Ij5', 'Lq1Ij4V', 'Lq1Ij3p1', 'Lq1Ij3pV', 'Lq1Ij2u2', 'Lq1Ij2u1V', 'Lq1Ij2up1', 'Lq1Ij2upV', 'Lq1Ij163', 'Lq1Ij162V', 'Lq1Ij161p1', 'Lq1Ij161pV', 'Lq1Ij16u2', 'Lq1Ij16u1V', 'Lq1Ij16up1', 'Lq1Ij16upV', 'Lq1Ij14', 'Lq1Ij13V', 'Lq1Ij12p1', 'Lq1Ij12pV', 'Lq1Ij11u2', 'Lq1Ij11u1V', 'Lq1Ij11up1', 'Lq1Ij11upV', 'Lq1Ij163', 'Lq1Ij162V', 'Lq1Ij161p1', 'Lq1Ij161pV', 'Lq1Ij16u2', 'Lq1Ij16u1V', 'Lq1Ij16up1', 'Lq1Ij16upV', 'LqH7', 'LqH6V', 'LqH5p1', 'LqH5pV', 'LqH4u2', 'LqH4u1V', 'LqH4up1', 'LqH4upV', 'LqH363', 'LqH362V', 'LqH361p1', 'LqH361pV', 'LqH36u2', 'LqH36u1V', 'LqH36up1', 'LqH36upV', 'LqH214', 'LqH213V', 'LqH212p1', 'LqH212pV', 'LqH211u2', 'LqH211u1V', 'LqH211up1', 'LqH211upV', 'LqH2163', 'LqH2162V', 'LqH2161p1', 'LqH2161pV', 'LqH216u2', 'LqH216u1V', 'LqH216up1', 'LqH216upV', 'LqH1j5', 'LqH1j4V', 'LqH1j3p1', 'LqH1j3pV', 'LqH1j2u2', 'LqH1j2u1V', 'LqH1j2up1', 'LqH1j2upV', 'LqH1j163', 'LqH1j162V', 'LqH1j161p1', 'LqH1j161pV', 'LqH1j16u2', 'LqH1j16u1V', 'LqH1j16up1', 'LqH1j16upV', 'LqH1j14', 'LqH1j13V', 'LqH1j12p1', 'LqH1j12pV', 'LqH1j11u2', 'LqH1j11u1V', 'LqH1j11up1', 'LqH1j11upV', 'LqH1j163', 'LqH1j162V', 'LqH1j161p1', 'LqH1j161pV', 'LqH1j16u2', 'LqH1j16u1V', 'LqH1j16up1', 'LqH1j16upV', 'LqHI6', 'LqHI5V', 'LqHI4p1', 'LqHI4pV', 'LqHI3u2', 'LqHI3u1V', 'LqHI3up1', 'LqHI3upV', 'LqHI263', 'LqHI262V', 'LqHI261p1', 'LqHI261pV', 'LqHI26u2', 'LqHI26u1V', 'LqHI26up1', 'LqHI26upV', 'LqHI114', 'LqHI113V', 'LqHI112p1', 'LqHI112pV', 'LqHI111u2', 'LqHI111u1V', 'LqHI111up1', 'LqHI111upV', 'LqHI1163', 'LqHI1162V', 'LqHI1161p1', 'LqHI1161pV', 'LqHI116u2', 'LqHI116u1V', 'LqHI116up1', 'LqHI116upV', 'LqHIj5', 'LqHIj4V', 'LqHIj3p1', 'LqHIj3pV', 'LqHIj2u2', 'LqHIj2u1V', 'LqHIj2up1', 'LqHIj2upV', 'LqHIj163', 'LqHIj162V', 'LqHIj161p1', 'LqHIj161pV', 'LqHIj16u2', 'LqHIj16u1V', 'LqHIj16up1', 'LqHIj16upV', 'LqHIj14', 'LqHIj13V', 'LqHIj12p1', 'LqHIj12pV', 'LqHIj11u2', 'LqHIj11u1V', 'LqHIj11up1', 'LqHIj11upV', 'LqHIj163', 'LqHIj162V', 'LqHIj161p1', 'LqHIj161pV', 'LqHIj16u2', 'LqHIj16u1V', 'LqHIj16up1', 'LqHIj16upV']
