
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


def test_0():
    assert solution.Solution().generateMatrix(77) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 78], [303, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 380, 79], [302, 599, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 674, 381, 80], [301, 598, 887, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 960, 675, 382, 81], [300, 597, 886, 1167, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1238, 961, 676, 383, 82], [299, 596, 885, 1166, 1439, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1723, 1724, 1725, 1726, 1727, 1728, 1729, 1730, 1731, 1732, 1733, 1734, 1735, 1736, 1737, 1738, 1739, 1740, 1741, 1742, 1743, 1744, 1745, 1746, 1747, 1748, 1749, 1750, 1751, 1752, 1753, 1754, 1755, 1756, 1757, 1758, 1759, 1760, 1761, 1762, 1763, 1764, 1765, 1766, 1767, 1768, 1769, 1508, 1239, 962, 677, 384, 83], [298, 595, 884, 1165, 1438, 1703, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 1770, 1509, 1240, 963, 678, 385, 84], [297, 594, 883, 1164, 1437, 1702, 1959, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2024, 1771, 1510, 1241, 964, 679, 386, 85], [296, 593, 882, 1163, 1436, 1701, 1958, 2207, 2448, 2449, 2450, 2451, 2452, 2453, 2454, 2455, 2456, 2457, 2458, 2459, 2460, 2461, 2462, 2463, 2464, 2465, 2466, 2467, 2468, 2469, 2470, 2471, 2472, 2473, 2474, 2475, 2476, 2477, 2478, 2479, 2480, 2481, 2482, 2483, 2484, 2485, 2486, 2487, 2488, 2489, 2490, 2491, 2492, 2493, 2494, 2495, 2496, 2497, 2498, 2499, 2500, 2501, 2502, 2503, 2504, 2505, 2506, 2507, 2270, 2025, 1772, 1511, 1242, 965, 680, 387, 86], [295, 592, 881, 1162, 1435, 1700, 1957, 2206, 2447, 2680, 2681, 2682, 2683, 2684, 2685, 2686, 2687, 2688, 2689, 2690, 2691, 2692, 2693, 2694, 2695, 2696, 2697, 2698, 2699, 2700, 2701, 2702, 2703, 2704, 2705, 2706, 2707, 2708, 2709, 2710, 2711, 2712, 2713, 2714, 2715, 2716, 2717, 2718, 2719, 2720, 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2730, 2731, 2732, 2733, 2734, 2735, 2736, 2737, 2508, 2271, 2026, 1773, 1512, 1243, 966, 681, 388, 87], [294, 591, 880, 1161, 1434, 1699, 1956, 2205, 2446, 2679, 2904, 2905, 2906, 2907, 2908, 2909, 2910, 2911, 2912, 2913, 2914, 2915, 2916, 2917, 2918, 2919, 2920, 2921, 2922, 2923, 2924, 2925, 2926, 2927, 2928, 2929, 2930, 2931, 2932, 2933, 2934, 2935, 2936, 2937, 2938, 2939, 2940, 2941, 2942, 2943, 2944, 2945, 2946, 2947, 2948, 2949, 2950, 2951, 2952, 2953, 2954, 2955, 2956, 2957, 2958, 2959, 2738, 2509, 2272, 2027, 1774, 1513, 1244, 967, 682, 389, 88], [293, 590, 879, 1160, 1433, 1698, 1955, 2204, 2445, 2678, 2903, 3120, 3121, 3122, 3123, 3124, 3125, 3126, 3127, 3128, 3129, 3130, 3131, 3132, 3133, 3134, 3135, 3136, 3137, 3138, 3139, 3140, 3141, 3142, 3143, 3144, 3145, 3146, 3147, 3148, 3149, 3150, 3151, 3152, 3153, 3154, 3155, 3156, 3157, 3158, 3159, 3160, 3161, 3162, 3163, 3164, 3165, 3166, 3167, 3168, 3169, 3170, 3171, 3172, 3173, 2960, 2739, 2510, 2273, 2028, 1775, 1514, 1245, 968, 683, 390, 89], [292, 589, 878, 1159, 1432, 1697, 1954, 2203, 2444, 2677, 2902, 3119, 3328, 3329, 3330, 3331, 3332, 3333, 3334, 3335, 3336, 3337, 3338, 3339, 3340, 3341, 3342, 3343, 3344, 3345, 3346, 3347, 3348, 3349, 3350, 3351, 3352, 3353, 3354, 3355, 3356, 3357, 3358, 3359, 3360, 3361, 3362, 3363, 3364, 3365, 3366, 3367, 3368, 3369, 3370, 3371, 3372, 3373, 3374, 3375, 3376, 3377, 3378, 3379, 3174, 2961, 2740, 2511, 2274, 2029, 1776, 1515, 1246, 969, 684, 391, 90], [291, 588, 877, 1158, 1431, 1696, 1953, 2202, 2443, 2676, 2901, 3118, 3327, 3528, 3529, 3530, 3531, 3532, 3533, 3534, 3535, 3536, 3537, 3538, 3539, 3540, 3541, 3542, 3543, 3544, 3545, 3546, 3547, 3548, 3549, 3550, 3551, 3552, 3553, 3554, 3555, 3556, 3557, 3558, 3559, 3560, 3561, 3562, 3563, 3564, 3565, 3566, 3567, 3568, 3569, 3570, 3571, 3572, 3573, 3574, 3575, 3576, 3577, 3380, 3175, 2962, 2741, 2512, 2275, 2030, 1777, 1516, 1247, 970, 685, 392, 91], [290, 587, 876, 1157, 1430, 1695, 1952, 2201, 2442, 2675, 2900, 3117, 3326, 3527, 3720, 3721, 3722, 3723, 3724, 3725, 3726, 3727, 3728, 3729, 3730, 3731, 3732, 3733, 3734, 3735, 3736, 3737, 3738, 3739, 3740, 3741, 3742, 3743, 3744, 3745, 3746, 3747, 3748, 3749, 3750, 3751, 3752, 3753, 3754, 3755, 3756, 3757, 3758, 3759, 3760, 3761, 3762, 3763, 3764, 3765, 3766, 3767, 3578, 3381, 3176, 2963, 2742, 2513, 2276, 2031, 1778, 1517, 1248, 971, 686, 393, 92], [289, 586, 875, 1156, 1429, 1694, 1951, 2200, 2441, 2674, 2899, 3116, 3325, 3526, 3719, 3904, 3905, 3906, 3907, 3908, 3909, 3910, 3911, 3912, 3913, 3914, 3915, 3916, 3917, 3918, 3919, 3920, 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3942, 3943, 3944, 3945, 3946, 3947, 3948, 3949, 3768, 3579, 3382, 3177, 2964, 2743, 2514, 2277, 2032, 1779, 1518, 1249, 972, 687, 394, 93], [288, 585, 874, 1155, 1428, 1693, 1950, 2199, 2440, 2673, 2898, 3115, 3324, 3525, 3718, 3903, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087, 4088, 4089, 4090, 4091, 4092, 4093, 4094, 4095, 4096, 4097, 4098, 4099, 4100, 4101, 4102, 4103, 4104, 4105, 4106, 4107, 4108, 4109, 4110, 4111, 4112, 4113, 4114, 4115, 4116, 4117, 4118, 4119, 4120, 4121, 4122, 4123, 3950, 3769, 3580, 3383, 3178, 2965, 2744, 2515, 2278, 2033, 1780, 1519, 1250, 973, 688, 395, 94], [287, 584, 873, 1154, 1427, 1692, 1949, 2198, 2439, 2672, 2897, 3114, 3323, 3524, 3717, 3902, 4079, 4248, 4249, 4250, 4251, 4252, 4253, 4254, 4255, 4256, 4257, 4258, 4259, 4260, 4261, 4262, 4263, 4264, 4265, 4266, 4267, 4268, 4269, 4270, 4271, 4272, 4273, 4274, 4275, 4276, 4277, 4278, 4279, 4280, 4281, 4282, 4283, 4284, 4285, 4286, 4287, 4288, 4289, 4124, 3951, 3770, 3581, 3384, 3179, 2966, 2745, 2516, 2279, 2034, 1781, 1520, 1251, 974, 689, 396, 95], [286, 583, 872, 1153, 1426, 1691, 1948, 2197, 2438, 2671, 2896, 3113, 3322, 3523, 3716, 3901, 4078, 4247, 4408, 4409, 4410, 4411, 4412, 4413, 4414, 4415, 4416, 4417, 4418, 4419, 4420, 4421, 4422, 4423, 4424, 4425, 4426, 4427, 4428, 4429, 4430, 4431, 4432, 4433, 4434, 4435, 4436, 4437, 4438, 4439, 4440, 4441, 4442, 4443, 4444, 4445, 4446, 4447, 4290, 4125, 3952, 3771, 3582, 3385, 3180, 2967, 2746, 2517, 2280, 2035, 1782, 1521, 1252, 975, 690, 397, 96], [285, 582, 871, 1152, 1425, 1690, 1947, 2196, 2437, 2670, 2895, 3112, 3321, 3522, 3715, 3900, 4077, 4246, 4407, 4560, 4561, 4562, 4563, 4564, 4565, 4566, 4567, 4568, 4569, 4570, 4571, 4572, 4573, 4574, 4575, 4576, 4577, 4578, 4579, 4580, 4581, 4582, 4583, 4584, 4585, 4586, 4587, 4588, 4589, 4590, 4591, 4592, 4593, 4594, 4595, 4596, 4597, 4448, 4291, 4126, 3953, 3772, 3583, 3386, 3181, 2968, 2747, 2518, 2281, 2036, 1783, 1522, 1253, 976, 691, 398, 97], [284, 581, 870, 1151, 1424, 1689, 1946, 2195, 2436, 2669, 2894, 3111, 3320, 3521, 3714, 3899, 4076, 4245, 4406, 4559, 4704, 4705, 4706, 4707, 4708, 4709, 4710, 4711, 4712, 4713, 4714, 4715, 4716, 4717, 4718, 4719, 4720, 4721, 4722, 4723, 4724, 4725, 4726, 4727, 4728, 4729, 4730, 4731, 4732, 4733, 4734, 4735, 4736, 4737, 4738, 4739, 4598, 4449, 4292, 4127, 3954, 3773, 3584, 3387, 3182, 2969, 2748, 2519, 2282, 2037, 1784, 1523, 1254, 977, 692, 399, 98], [283, 580, 869, 1150, 1423, 1688, 1945, 2194, 2435, 2668, 2893, 3110, 3319, 3520, 3713, 3898, 4075, 4244, 4405, 4558, 4703, 4840, 4841, 4842, 4843, 4844, 4845, 4846, 4847, 4848, 4849, 4850, 4851, 4852, 4853, 4854, 4855, 4856, 4857, 4858, 4859, 4860, 4861, 4862, 4863, 4864, 4865, 4866, 4867, 4868, 4869, 4870, 4871, 4872, 4873, 4740, 4599, 4450, 4293, 4128, 3955, 3774, 3585, 3388, 3183, 2970, 2749, 2520, 2283, 2038, 1785, 1524, 1255, 978, 693, 400, 99], [282, 579, 868, 1149, 1422, 1687, 1944, 2193, 2434, 2667, 2892, 3109, 3318, 3519, 3712, 3897, 4074, 4243, 4404, 4557, 4702, 4839, 4968, 4969, 4970, 4971, 4972, 4973, 4974, 4975, 4976, 4977, 4978, 4979, 4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 4874, 4741, 4600, 4451, 4294, 4129, 3956, 3775, 3586, 3389, 3184, 2971, 2750, 2521, 2284, 2039, 1786, 1525, 1256, 979, 694, 401, 100], [281, 578, 867, 1148, 1421, 1686, 1943, 2192, 2433, 2666, 2891, 3108, 3317, 3518, 3711, 3896, 4073, 4242, 4403, 4556, 4701, 4838, 4967, 5088, 5089, 5090, 5091, 5092, 5093, 5094, 5095, 5096, 5097, 5098, 5099, 5100, 5101, 5102, 5103, 5104, 5105, 5106, 5107, 5108, 5109, 5110, 5111, 5112, 5113, 5114, 5115, 5116, 5117, 5000, 4875, 4742, 4601, 4452, 4295, 4130, 3957, 3776, 3587, 3390, 3185, 2972, 2751, 2522, 2285, 2040, 1787, 1526, 1257, 980, 695, 402, 101], [280, 577, 866, 1147, 1420, 1685, 1942, 2191, 2432, 2665, 2890, 3107, 3316, 3517, 3710, 3895, 4072, 4241, 4402, 4555, 4700, 4837, 4966, 5087, 5200, 5201, 5202, 5203, 5204, 5205, 5206, 5207, 5208, 5209, 5210, 5211, 5212, 5213, 5214, 5215, 5216, 5217, 5218, 5219, 5220, 5221, 5222, 5223, 5224, 5225, 5226, 5227, 5118, 5001, 4876, 4743, 4602, 4453, 4296, 4131, 3958, 3777, 3588, 3391, 3186, 2973, 2752, 2523, 2286, 2041, 1788, 1527, 1258, 981, 696, 403, 102], [279, 576, 865, 1146, 1419, 1684, 1941, 2190, 2431, 2664, 2889, 3106, 3315, 3516, 3709, 3894, 4071, 4240, 4401, 4554, 4699, 4836, 4965, 5086, 5199, 5304, 5305, 5306, 5307, 5308, 5309, 5310, 5311, 5312, 5313, 5314, 5315, 5316, 5317, 5318, 5319, 5320, 5321, 5322, 5323, 5324, 5325, 5326, 5327, 5328, 5329, 5228, 5119, 5002, 4877, 4744, 4603, 4454, 4297, 4132, 3959, 3778, 3589, 3392, 3187, 2974, 2753, 2524, 2287, 2042, 1789, 1528, 1259, 982, 697, 404, 103], [278, 575, 864, 1145, 1418, 1683, 1940, 2189, 2430, 2663, 2888, 3105, 3314, 3515, 3708, 3893, 4070, 4239, 4400, 4553, 4698, 4835, 4964, 5085, 5198, 5303, 5400, 5401, 5402, 5403, 5404, 5405, 5406, 5407, 5408, 5409, 5410, 5411, 5412, 5413, 5414, 5415, 5416, 5417, 5418, 5419, 5420, 5421, 5422, 5423, 5330, 5229, 5120, 5003, 4878, 4745, 4604, 4455, 4298, 4133, 3960, 3779, 3590, 3393, 3188, 2975, 2754, 2525, 2288, 2043, 1790, 1529, 1260, 983, 698, 405, 104], [277, 574, 863, 1144, 1417, 1682, 1939, 2188, 2429, 2662, 2887, 3104, 3313, 3514, 3707, 3892, 4069, 4238, 4399, 4552, 4697, 4834, 4963, 5084, 5197, 5302, 5399, 5488, 5489, 5490, 5491, 5492, 5493, 5494, 5495, 5496, 5497, 5498, 5499, 5500, 5501, 5502, 5503, 5504, 5505, 5506, 5507, 5508, 5509, 5424, 5331, 5230, 5121, 5004, 4879, 4746, 4605, 4456, 4299, 4134, 3961, 3780, 3591, 3394, 3189, 2976, 2755, 2526, 2289, 2044, 1791, 1530, 1261, 984, 699, 406, 105], [276, 573, 862, 1143, 1416, 1681, 1938, 2187, 2428, 2661, 2886, 3103, 3312, 3513, 3706, 3891, 4068, 4237, 4398, 4551, 4696, 4833, 4962, 5083, 5196, 5301, 5398, 5487, 5568, 5569, 5570, 5571, 5572, 5573, 5574, 5575, 5576, 5577, 5578, 5579, 5580, 5581, 5582, 5583, 5584, 5585, 5586, 5587, 5510, 5425, 5332, 5231, 5122, 5005, 4880, 4747, 4606, 4457, 4300, 4135, 3962, 3781, 3592, 3395, 3190, 2977, 2756, 2527, 2290, 2045, 1792, 1531, 1262, 985, 700, 407, 106], [275, 572, 861, 1142, 1415, 1680, 1937, 2186, 2427, 2660, 2885, 3102, 3311, 3512, 3705, 3890, 4067, 4236, 4397, 4550, 4695, 4832, 4961, 5082, 5195, 5300, 5397, 5486, 5567, 5640, 5641, 5642, 5643, 5644, 5645, 5646, 5647, 5648, 5649, 5650, 5651, 5652, 5653, 5654, 5655, 5656, 5657, 5588, 5511, 5426, 5333, 5232, 5123, 5006, 4881, 4748, 4607, 4458, 4301, 4136, 3963, 3782, 3593, 3396, 3191, 2978, 2757, 2528, 2291, 2046, 1793, 1532, 1263, 986, 701, 408, 107], [274, 571, 860, 1141, 1414, 1679, 1936, 2185, 2426, 2659, 2884, 3101, 3310, 3511, 3704, 3889, 4066, 4235, 4396, 4549, 4694, 4831, 4960, 5081, 5194, 5299, 5396, 5485, 5566, 5639, 5704, 5705, 5706, 5707, 5708, 5709, 5710, 5711, 5712, 5713, 5714, 5715, 5716, 5717, 5718, 5719, 5658, 5589, 5512, 5427, 5334, 5233, 5124, 5007, 4882, 4749, 4608, 4459, 4302, 4137, 3964, 3783, 3594, 3397, 3192, 2979, 2758, 2529, 2292, 2047, 1794, 1533, 1264, 987, 702, 409, 108], [273, 570, 859, 1140, 1413, 1678, 1935, 2184, 2425, 2658, 2883, 3100, 3309, 3510, 3703, 3888, 4065, 4234, 4395, 4548, 4693, 4830, 4959, 5080, 5193, 5298, 5395, 5484, 5565, 5638, 5703, 5760, 5761, 5762, 5763, 5764, 5765, 5766, 5767, 5768, 5769, 5770, 5771, 5772, 5773, 5720, 5659, 5590, 5513, 5428, 5335, 5234, 5125, 5008, 4883, 4750, 4609, 4460, 4303, 4138, 3965, 3784, 3595, 3398, 3193, 2980, 2759, 2530, 2293, 2048, 1795, 1534, 1265, 988, 703, 410, 109], [272, 569, 858, 1139, 1412, 1677, 1934, 2183, 2424, 2657, 2882, 3099, 3308, 3509, 3702, 3887, 4064, 4233, 4394, 4547, 4692, 4829, 4958, 5079, 5192, 5297, 5394, 5483, 5564, 5637, 5702, 5759, 5808, 5809, 5810, 5811, 5812, 5813, 5814, 5815, 5816, 5817, 5818, 5819, 5774, 5721, 5660, 5591, 5514, 5429, 5336, 5235, 5126, 5009, 4884, 4751, 4610, 4461, 4304, 4139, 3966, 3785, 3596, 3399, 3194, 2981, 2760, 2531, 2294, 2049, 1796, 1535, 1266, 989, 704, 411, 110], [271, 568, 857, 1138, 1411, 1676, 1933, 2182, 2423, 2656, 2881, 3098, 3307, 3508, 3701, 3886, 4063, 4232, 4393, 4546, 4691, 4828, 4957, 5078, 5191, 5296, 5393, 5482, 5563, 5636, 5701, 5758, 5807, 5848, 5849, 5850, 5851, 5852, 5853, 5854, 5855, 5856, 5857, 5820, 5775, 5722, 5661, 5592, 5515, 5430, 5337, 5236, 5127, 5010, 4885, 4752, 4611, 4462, 4305, 4140, 3967, 3786, 3597, 3400, 3195, 2982, 2761, 2532, 2295, 2050, 1797, 1536, 1267, 990, 705, 412, 111], [270, 567, 856, 1137, 1410, 1675, 1932, 2181, 2422, 2655, 2880, 3097, 3306, 3507, 3700, 3885, 4062, 4231, 4392, 4545, 4690, 4827, 4956, 5077, 5190, 5295, 5392, 5481, 5562, 5635, 5700, 5757, 5806, 5847, 5880, 5881, 5882, 5883, 5884, 5885, 5886, 5887, 5858, 5821, 5776, 5723, 5662, 5593, 5516, 5431, 5338, 5237, 5128, 5011, 4886, 4753, 4612, 4463, 4306, 4141, 3968, 3787, 3598, 3401, 3196, 2983, 2762, 2533, 2296, 2051, 1798, 1537, 1268, 991, 706, 413, 112], [269, 566, 855, 1136, 1409, 1674, 1931, 2180, 2421, 2654, 2879, 3096, 3305, 3506, 3699, 3884, 4061, 4230, 4391, 4544, 4689, 4826, 4955, 5076, 5189, 5294, 5391, 5480, 5561, 5634, 5699, 5756, 5805, 5846, 5879, 5904, 5905, 5906, 5907, 5908, 5909, 5888, 5859, 5822, 5777, 5724, 5663, 5594, 5517, 5432, 5339, 5238, 5129, 5012, 4887, 4754, 4613, 4464, 4307, 4142, 3969, 3788, 3599, 3402, 3197, 2984, 2763, 2534, 2297, 2052, 1799, 1538, 1269, 992, 707, 414, 113], [268, 565, 854, 1135, 1408, 1673, 1930, 2179, 2420, 2653, 2878, 3095, 3304, 3505, 3698, 3883, 4060, 4229, 4390, 4543, 4688, 4825, 4954, 5075, 5188, 5293, 5390, 5479, 5560, 5633, 5698, 5755, 5804, 5845, 5878, 5903, 5920, 5921, 5922, 5923, 5910, 5889, 5860, 5823, 5778, 5725, 5664, 5595, 5518, 5433, 5340, 5239, 5130, 5013, 4888, 4755, 4614, 4465, 4308, 4143, 3970, 3789, 3600, 3403, 3198, 2985, 2764, 2535, 2298, 2053, 1800, 1539, 1270, 993, 708, 415, 114], [267, 564, 853, 1134, 1407, 1672, 1929, 2178, 2419, 2652, 2877, 3094, 3303, 3504, 3697, 3882, 4059, 4228, 4389, 4542, 4687, 4824, 4953, 5074, 5187, 5292, 5389, 5478, 5559, 5632, 5697, 5754, 5803, 5844, 5877, 5902, 5919, 5928, 5929, 5924, 5911, 5890, 5861, 5824, 5779, 5726, 5665, 5596, 5519, 5434, 5341, 5240, 5131, 5014, 4889, 4756, 4615, 4466, 4309, 4144, 3971, 3790, 3601, 3404, 3199, 2986, 2765, 2536, 2299, 2054, 1801, 1540, 1271, 994, 709, 416, 115], [266, 563, 852, 1133, 1406, 1671, 1928, 2177, 2418, 2651, 2876, 3093, 3302, 3503, 3696, 3881, 4058, 4227, 4388, 4541, 4686, 4823, 4952, 5073, 5186, 5291, 5388, 5477, 5558, 5631, 5696, 5753, 5802, 5843, 5876, 5901, 5918, 5927, 5926, 5925, 5912, 5891, 5862, 5825, 5780, 5727, 5666, 5597, 5520, 5435, 5342, 5241, 5132, 5015, 4890, 4757, 4616, 4467, 4310, 4145, 3972, 3791, 3602, 3405, 3200, 2987, 2766, 2537, 2300, 2055, 1802, 1541, 1272, 995, 710, 417, 116], [265, 562, 851, 1132, 1405, 1670, 1927, 2176, 2417, 2650, 2875, 3092, 3301, 3502, 3695, 3880, 4057, 4226, 4387, 4540, 4685, 4822, 4951, 5072, 5185, 5290, 5387, 5476, 5557, 5630, 5695, 5752, 5801, 5842, 5875, 5900, 5917, 5916, 5915, 5914, 5913, 5892, 5863, 5826, 5781, 5728, 5667, 5598, 5521, 5436, 5343, 5242, 5133, 5016, 4891, 4758, 4617, 4468, 4311, 4146, 3973, 3792, 3603, 3406, 3201, 2988, 2767, 2538, 2301, 2056, 1803, 1542, 1273, 996, 711, 418, 117], [264, 561, 850, 1131, 1404, 1669, 1926, 2175, 2416, 2649, 2874, 3091, 3300, 3501, 3694, 3879, 4056, 4225, 4386, 4539, 4684, 4821, 4950, 5071, 5184, 5289, 5386, 5475, 5556, 5629, 5694, 5751, 5800, 5841, 5874, 5899, 5898, 5897, 5896, 5895, 5894, 5893, 5864, 5827, 5782, 5729, 5668, 5599, 5522, 5437, 5344, 5243, 5134, 5017, 4892, 4759, 4618, 4469, 4312, 4147, 3974, 3793, 3604, 3407, 3202, 2989, 2768, 2539, 2302, 2057, 1804, 1543, 1274, 997, 712, 419, 118], [263, 560, 849, 1130, 1403, 1668, 1925, 2174, 2415, 2648, 2873, 3090, 3299, 3500, 3693, 3878, 4055, 4224, 4385, 4538, 4683, 4820, 4949, 5070, 5183, 5288, 5385, 5474, 5555, 5628, 5693, 5750, 5799, 5840, 5873, 5872, 5871, 5870, 5869, 5868, 5867, 5866, 5865, 5828, 5783, 5730, 5669, 5600, 5523, 5438, 5345, 5244, 5135, 5018, 4893, 4760, 4619, 4470, 4313, 4148, 3975, 3794, 3605, 3408, 3203, 2990, 2769, 2540, 2303, 2058, 1805, 1544, 1275, 998, 713, 420, 119], [262, 559, 848, 1129, 1402, 1667, 1924, 2173, 2414, 2647, 2872, 3089, 3298, 3499, 3692, 3877, 4054, 4223, 4384, 4537, 4682, 4819, 4948, 5069, 5182, 5287, 5384, 5473, 5554, 5627, 5692, 5749, 5798, 5839, 5838, 5837, 5836, 5835, 5834, 5833, 5832, 5831, 5830, 5829, 5784, 5731, 5670, 5601, 5524, 5439, 5346, 5245, 5136, 5019, 4894, 4761, 4620, 4471, 4314, 4149, 3976, 3795, 3606, 3409, 3204, 2991, 2770, 2541, 2304, 2059, 1806, 1545, 1276, 999, 714, 421, 120], [261, 558, 847, 1128, 1401, 1666, 1923, 2172, 2413, 2646, 2871, 3088, 3297, 3498, 3691, 3876, 4053, 4222, 4383, 4536, 4681, 4818, 4947, 5068, 5181, 5286, 5383, 5472, 5553, 5626, 5691, 5748, 5797, 5796, 5795, 5794, 5793, 5792, 5791, 5790, 5789, 5788, 5787, 5786, 5785, 5732, 5671, 5602, 5525, 5440, 5347, 5246, 5137, 5020, 4895, 4762, 4621, 4472, 4315, 4150, 3977, 3796, 3607, 3410, 3205, 2992, 2771, 2542, 2305, 2060, 1807, 1546, 1277, 1000, 715, 422, 121], [260, 557, 846, 1127, 1400, 1665, 1922, 2171, 2412, 2645, 2870, 3087, 3296, 3497, 3690, 3875, 4052, 4221, 4382, 4535, 4680, 4817, 4946, 5067, 5180, 5285, 5382, 5471, 5552, 5625, 5690, 5747, 5746, 5745, 5744, 5743, 5742, 5741, 5740, 5739, 5738, 5737, 5736, 5735, 5734, 5733, 5672, 5603, 5526, 5441, 5348, 5247, 5138, 5021, 4896, 4763, 4622, 4473, 4316, 4151, 3978, 3797, 3608, 3411, 3206, 2993, 2772, 2543, 2306, 2061, 1808, 1547, 1278, 1001, 716, 423, 122], [259, 556, 845, 1126, 1399, 1664, 1921, 2170, 2411, 2644, 2869, 3086, 3295, 3496, 3689, 3874, 4051, 4220, 4381, 4534, 4679, 4816, 4945, 5066, 5179, 5284, 5381, 5470, 5551, 5624, 5689, 5688, 5687, 5686, 5685, 5684, 5683, 5682, 5681, 5680, 5679, 5678, 5677, 5676, 5675, 5674, 5673, 5604, 5527, 5442, 5349, 5248, 5139, 5022, 4897, 4764, 4623, 4474, 4317, 4152, 3979, 3798, 3609, 3412, 3207, 2994, 2773, 2544, 2307, 2062, 1809, 1548, 1279, 1002, 717, 424, 123], [258, 555, 844, 1125, 1398, 1663, 1920, 2169, 2410, 2643, 2868, 3085, 3294, 3495, 3688, 3873, 4050, 4219, 4380, 4533, 4678, 4815, 4944, 5065, 5178, 5283, 5380, 5469, 5550, 5623, 5622, 5621, 5620, 5619, 5618, 5617, 5616, 5615, 5614, 5613, 5612, 5611, 5610, 5609, 5608, 5607, 5606, 5605, 5528, 5443, 5350, 5249, 5140, 5023, 4898, 4765, 4624, 4475, 4318, 4153, 3980, 3799, 3610, 3413, 3208, 2995, 2774, 2545, 2308, 2063, 1810, 1549, 1280, 1003, 718, 425, 124], [257, 554, 843, 1124, 1397, 1662, 1919, 2168, 2409, 2642, 2867, 3084, 3293, 3494, 3687, 3872, 4049, 4218, 4379, 4532, 4677, 4814, 4943, 5064, 5177, 5282, 5379, 5468, 5549, 5548, 5547, 5546, 5545, 5544, 5543, 5542, 5541, 5540, 5539, 5538, 5537, 5536, 5535, 5534, 5533, 5532, 5531, 5530, 5529, 5444, 5351, 5250, 5141, 5024, 4899, 4766, 4625, 4476, 4319, 4154, 3981, 3800, 3611, 3414, 3209, 2996, 2775, 2546, 2309, 2064, 1811, 1550, 1281, 1004, 719, 426, 125], [256, 553, 842, 1123, 1396, 1661, 1918, 2167, 2408, 2641, 2866, 3083, 3292, 3493, 3686, 3871, 4048, 4217, 4378, 4531, 4676, 4813, 4942, 5063, 5176, 5281, 5378, 5467, 5466, 5465, 5464, 5463, 5462, 5461, 5460, 5459, 5458, 5457, 5456, 5455, 5454, 5453, 5452, 5451, 5450, 5449, 5448, 5447, 5446, 5445, 5352, 5251, 5142, 5025, 4900, 4767, 4626, 4477, 4320, 4155, 3982, 3801, 3612, 3415, 3210, 2997, 2776, 2547, 2310, 2065, 1812, 1551, 1282, 1005, 720, 427, 126], [255, 552, 841, 1122, 1395, 1660, 1917, 2166, 2407, 2640, 2865, 3082, 3291, 3492, 3685, 3870, 4047, 4216, 4377, 4530, 4675, 4812, 4941, 5062, 5175, 5280, 5377, 5376, 5375, 5374, 5373, 5372, 5371, 5370, 5369, 5368, 5367, 5366, 5365, 5364, 5363, 5362, 5361, 5360, 5359, 5358, 5357, 5356, 5355, 5354, 5353, 5252, 5143, 5026, 4901, 4768, 4627, 4478, 4321, 4156, 3983, 3802, 3613, 3416, 3211, 2998, 2777, 2548, 2311, 2066, 1813, 1552, 1283, 1006, 721, 428, 127], [254, 551, 840, 1121, 1394, 1659, 1916, 2165, 2406, 2639, 2864, 3081, 3290, 3491, 3684, 3869, 4046, 4215, 4376, 4529, 4674, 4811, 4940, 5061, 5174, 5279, 5278, 5277, 5276, 5275, 5274, 5273, 5272, 5271, 5270, 5269, 5268, 5267, 5266, 5265, 5264, 5263, 5262, 5261, 5260, 5259, 5258, 5257, 5256, 5255, 5254, 5253, 5144, 5027, 4902, 4769, 4628, 4479, 4322, 4157, 3984, 3803, 3614, 3417, 3212, 2999, 2778, 2549, 2312, 2067, 1814, 1553, 1284, 1007, 722, 429, 128], [253, 550, 839, 1120, 1393, 1658, 1915, 2164, 2405, 2638, 2863, 3080, 3289, 3490, 3683, 3868, 4045, 4214, 4375, 4528, 4673, 4810, 4939, 5060, 5173, 5172, 5171, 5170, 5169, 5168, 5167, 5166, 5165, 5164, 5163, 5162, 5161, 5160, 5159, 5158, 5157, 5156, 5155, 5154, 5153, 5152, 5151, 5150, 5149, 5148, 5147, 5146, 5145, 5028, 4903, 4770, 4629, 4480, 4323, 4158, 3985, 3804, 3615, 3418, 3213, 3000, 2779, 2550, 2313, 2068, 1815, 1554, 1285, 1008, 723, 430, 129], [252, 549, 838, 1119, 1392, 1657, 1914, 2163, 2404, 2637, 2862, 3079, 3288, 3489, 3682, 3867, 4044, 4213, 4374, 4527, 4672, 4809, 4938, 5059, 5058, 5057, 5056, 5055, 5054, 5053, 5052, 5051, 5050, 5049, 5048, 5047, 5046, 5045, 5044, 5043, 5042, 5041, 5040, 5039, 5038, 5037, 5036, 5035, 5034, 5033, 5032, 5031, 5030, 5029, 4904, 4771, 4630, 4481, 4324, 4159, 3986, 3805, 3616, 3419, 3214, 3001, 2780, 2551, 2314, 2069, 1816, 1555, 1286, 1009, 724, 431, 130], [251, 548, 837, 1118, 1391, 1656, 1913, 2162, 2403, 2636, 2861, 3078, 3287, 3488, 3681, 3866, 4043, 4212, 4373, 4526, 4671, 4808, 4937, 4936, 4935, 4934, 4933, 4932, 4931, 4930, 4929, 4928, 4927, 4926, 4925, 4924, 4923, 4922, 4921, 4920, 4919, 4918, 4917, 4916, 4915, 4914, 4913, 4912, 4911, 4910, 4909, 4908, 4907, 4906, 4905, 4772, 4631, 4482, 4325, 4160, 3987, 3806, 3617, 3420, 3215, 3002, 2781, 2552, 2315, 2070, 1817, 1556, 1287, 1010, 725, 432, 131], [250, 547, 836, 1117, 1390, 1655, 1912, 2161, 2402, 2635, 2860, 3077, 3286, 3487, 3680, 3865, 4042, 4211, 4372, 4525, 4670, 4807, 4806, 4805, 4804, 4803, 4802, 4801, 4800, 4799, 4798, 4797, 4796, 4795, 4794, 4793, 4792, 4791, 4790, 4789, 4788, 4787, 4786, 4785, 4784, 4783, 4782, 4781, 4780, 4779, 4778, 4777, 4776, 4775, 4774, 4773, 4632, 4483, 4326, 4161, 3988, 3807, 3618, 3421, 3216, 3003, 2782, 2553, 2316, 2071, 1818, 1557, 1288, 1011, 726, 433, 132], [249, 546, 835, 1116, 1389, 1654, 1911, 2160, 2401, 2634, 2859, 3076, 3285, 3486, 3679, 3864, 4041, 4210, 4371, 4524, 4669, 4668, 4667, 4666, 4665, 4664, 4663, 4662, 4661, 4660, 4659, 4658, 4657, 4656, 4655, 4654, 4653, 4652, 4651, 4650, 4649, 4648, 4647, 4646, 4645, 4644, 4643, 4642, 4641, 4640, 4639, 4638, 4637, 4636, 4635, 4634, 4633, 4484, 4327, 4162, 3989, 3808, 3619, 3422, 3217, 3004, 2783, 2554, 2317, 2072, 1819, 1558, 1289, 1012, 727, 434, 133], [248, 545, 834, 1115, 1388, 1653, 1910, 2159, 2400, 2633, 2858, 3075, 3284, 3485, 3678, 3863, 4040, 4209, 4370, 4523, 4522, 4521, 4520, 4519, 4518, 4517, 4516, 4515, 4514, 4513, 4512, 4511, 4510, 4509, 4508, 4507, 4506, 4505, 4504, 4503, 4502, 4501, 4500, 4499, 4498, 4497, 4496, 4495, 4494, 4493, 4492, 4491, 4490, 4489, 4488, 4487, 4486, 4485, 4328, 4163, 3990, 3809, 3620, 3423, 3218, 3005, 2784, 2555, 2318, 2073, 1820, 1559, 1290, 1013, 728, 435, 134], [247, 544, 833, 1114, 1387, 1652, 1909, 2158, 2399, 2632, 2857, 3074, 3283, 3484, 3677, 3862, 4039, 4208, 4369, 4368, 4367, 4366, 4365, 4364, 4363, 4362, 4361, 4360, 4359, 4358, 4357, 4356, 4355, 4354, 4353, 4352, 4351, 4350, 4349, 4348, 4347, 4346, 4345, 4344, 4343, 4342, 4341, 4340, 4339, 4338, 4337, 4336, 4335, 4334, 4333, 4332, 4331, 4330, 4329, 4164, 3991, 3810, 3621, 3424, 3219, 3006, 2785, 2556, 2319, 2074, 1821, 1560, 1291, 1014, 729, 436, 135], [246, 543, 832, 1113, 1386, 1651, 1908, 2157, 2398, 2631, 2856, 3073, 3282, 3483, 3676, 3861, 4038, 4207, 4206, 4205, 4204, 4203, 4202, 4201, 4200, 4199, 4198, 4197, 4196, 4195, 4194, 4193, 4192, 4191, 4190, 4189, 4188, 4187, 4186, 4185, 4184, 4183, 4182, 4181, 4180, 4179, 4178, 4177, 4176, 4175, 4174, 4173, 4172, 4171, 4170, 4169, 4168, 4167, 4166, 4165, 3992, 3811, 3622, 3425, 3220, 3007, 2786, 2557, 2320, 2075, 1822, 1561, 1292, 1015, 730, 437, 136], [245, 542, 831, 1112, 1385, 1650, 1907, 2156, 2397, 2630, 2855, 3072, 3281, 3482, 3675, 3860, 4037, 4036, 4035, 4034, 4033, 4032, 4031, 4030, 4029, 4028, 4027, 4026, 4025, 4024, 4023, 4022, 4021, 4020, 4019, 4018, 4017, 4016, 4015, 4014, 4013, 4012, 4011, 4010, 4009, 4008, 4007, 4006, 4005, 4004, 4003, 4002, 4001, 4000, 3999, 3998, 3997, 3996, 3995, 3994, 3993, 3812, 3623, 3426, 3221, 3008, 2787, 2558, 2321, 2076, 1823, 1562, 1293, 1016, 731, 438, 137], [244, 541, 830, 1111, 1384, 1649, 1906, 2155, 2396, 2629, 2854, 3071, 3280, 3481, 3674, 3859, 3858, 3857, 3856, 3855, 3854, 3853, 3852, 3851, 3850, 3849, 3848, 3847, 3846, 3845, 3844, 3843, 3842, 3841, 3840, 3839, 3838, 3837, 3836, 3835, 3834, 3833, 3832, 3831, 3830, 3829, 3828, 3827, 3826, 3825, 3824, 3823, 3822, 3821, 3820, 3819, 3818, 3817, 3816, 3815, 3814, 3813, 3624, 3427, 3222, 3009, 2788, 2559, 2322, 2077, 1824, 1563, 1294, 1017, 732, 439, 138], [243, 540, 829, 1110, 1383, 1648, 1905, 2154, 2395, 2628, 2853, 3070, 3279, 3480, 3673, 3672, 3671, 3670, 3669, 3668, 3667, 3666, 3665, 3664, 3663, 3662, 3661, 3660, 3659, 3658, 3657, 3656, 3655, 3654, 3653, 3652, 3651, 3650, 3649, 3648, 3647, 3646, 3645, 3644, 3643, 3642, 3641, 3640, 3639, 3638, 3637, 3636, 3635, 3634, 3633, 3632, 3631, 3630, 3629, 3628, 3627, 3626, 3625, 3428, 3223, 3010, 2789, 2560, 2323, 2078, 1825, 1564, 1295, 1018, 733, 440, 139], [242, 539, 828, 1109, 1382, 1647, 1904, 2153, 2394, 2627, 2852, 3069, 3278, 3479, 3478, 3477, 3476, 3475, 3474, 3473, 3472, 3471, 3470, 3469, 3468, 3467, 3466, 3465, 3464, 3463, 3462, 3461, 3460, 3459, 3458, 3457, 3456, 3455, 3454, 3453, 3452, 3451, 3450, 3449, 3448, 3447, 3446, 3445, 3444, 3443, 3442, 3441, 3440, 3439, 3438, 3437, 3436, 3435, 3434, 3433, 3432, 3431, 3430, 3429, 3224, 3011, 2790, 2561, 2324, 2079, 1826, 1565, 1296, 1019, 734, 441, 140], [241, 538, 827, 1108, 1381, 1646, 1903, 2152, 2393, 2626, 2851, 3068, 3277, 3276, 3275, 3274, 3273, 3272, 3271, 3270, 3269, 3268, 3267, 3266, 3265, 3264, 3263, 3262, 3261, 3260, 3259, 3258, 3257, 3256, 3255, 3254, 3253, 3252, 3251, 3250, 3249, 3248, 3247, 3246, 3245, 3244, 3243, 3242, 3241, 3240, 3239, 3238, 3237, 3236, 3235, 3234, 3233, 3232, 3231, 3230, 3229, 3228, 3227, 3226, 3225, 3012, 2791, 2562, 2325, 2080, 1827, 1566, 1297, 1020, 735, 442, 141], [240, 537, 826, 1107, 1380, 1645, 1902, 2151, 2392, 2625, 2850, 3067, 3066, 3065, 3064, 3063, 3062, 3061, 3060, 3059, 3058, 3057, 3056, 3055, 3054, 3053, 3052, 3051, 3050, 3049, 3048, 3047, 3046, 3045, 3044, 3043, 3042, 3041, 3040, 3039, 3038, 3037, 3036, 3035, 3034, 3033, 3032, 3031, 3030, 3029, 3028, 3027, 3026, 3025, 3024, 3023, 3022, 3021, 3020, 3019, 3018, 3017, 3016, 3015, 3014, 3013, 2792, 2563, 2326, 2081, 1828, 1567, 1298, 1021, 736, 443, 142], [239, 536, 825, 1106, 1379, 1644, 1901, 2150, 2391, 2624, 2849, 2848, 2847, 2846, 2845, 2844, 2843, 2842, 2841, 2840, 2839, 2838, 2837, 2836, 2835, 2834, 2833, 2832, 2831, 2830, 2829, 2828, 2827, 2826, 2825, 2824, 2823, 2822, 2821, 2820, 2819, 2818, 2817, 2816, 2815, 2814, 2813, 2812, 2811, 2810, 2809, 2808, 2807, 2806, 2805, 2804, 2803, 2802, 2801, 2800, 2799, 2798, 2797, 2796, 2795, 2794, 2793, 2564, 2327, 2082, 1829, 1568, 1299, 1022, 737, 444, 143], [238, 535, 824, 1105, 1378, 1643, 1900, 2149, 2390, 2623, 2622, 2621, 2620, 2619, 2618, 2617, 2616, 2615, 2614, 2613, 2612, 2611, 2610, 2609, 2608, 2607, 2606, 2605, 2604, 2603, 2602, 2601, 2600, 2599, 2598, 2597, 2596, 2595, 2594, 2593, 2592, 2591, 2590, 2589, 2588, 2587, 2586, 2585, 2584, 2583, 2582, 2581, 2580, 2579, 2578, 2577, 2576, 2575, 2574, 2573, 2572, 2571, 2570, 2569, 2568, 2567, 2566, 2565, 2328, 2083, 1830, 1569, 1300, 1023, 738, 445, 144], [237, 534, 823, 1104, 1377, 1642, 1899, 2148, 2389, 2388, 2387, 2386, 2385, 2384, 2383, 2382, 2381, 2380, 2379, 2378, 2377, 2376, 2375, 2374, 2373, 2372, 2371, 2370, 2369, 2368, 2367, 2366, 2365, 2364, 2363, 2362, 2361, 2360, 2359, 2358, 2357, 2356, 2355, 2354, 2353, 2352, 2351, 2350, 2349, 2348, 2347, 2346, 2345, 2344, 2343, 2342, 2341, 2340, 2339, 2338, 2337, 2336, 2335, 2334, 2333, 2332, 2331, 2330, 2329, 2084, 1831, 1570, 1301, 1024, 739, 446, 145], [236, 533, 822, 1103, 1376, 1641, 1898, 2147, 2146, 2145, 2144, 2143, 2142, 2141, 2140, 2139, 2138, 2137, 2136, 2135, 2134, 2133, 2132, 2131, 2130, 2129, 2128, 2127, 2126, 2125, 2124, 2123, 2122, 2121, 2120, 2119, 2118, 2117, 2116, 2115, 2114, 2113, 2112, 2111, 2110, 2109, 2108, 2107, 2106, 2105, 2104, 2103, 2102, 2101, 2100, 2099, 2098, 2097, 2096, 2095, 2094, 2093, 2092, 2091, 2090, 2089, 2088, 2087, 2086, 2085, 1832, 1571, 1302, 1025, 740, 447, 146], [235, 532, 821, 1102, 1375, 1640, 1897, 1896, 1895, 1894, 1893, 1892, 1891, 1890, 1889, 1888, 1887, 1886, 1885, 1884, 1883, 1882, 1881, 1880, 1879, 1878, 1877, 1876, 1875, 1874, 1873, 1872, 1871, 1870, 1869, 1868, 1867, 1866, 1865, 1864, 1863, 1862, 1861, 1860, 1859, 1858, 1857, 1856, 1855, 1854, 1853, 1852, 1851, 1850, 1849, 1848, 1847, 1846, 1845, 1844, 1843, 1842, 1841, 1840, 1839, 1838, 1837, 1836, 1835, 1834, 1833, 1572, 1303, 1026, 741, 448, 147], [234, 531, 820, 1101, 1374, 1639, 1638, 1637, 1636, 1635, 1634, 1633, 1632, 1631, 1630, 1629, 1628, 1627, 1626, 1625, 1624, 1623, 1622, 1621, 1620, 1619, 1618, 1617, 1616, 1615, 1614, 1613, 1612, 1611, 1610, 1609, 1608, 1607, 1606, 1605, 1604, 1603, 1602, 1601, 1600, 1599, 1598, 1597, 1596, 1595, 1594, 1593, 1592, 1591, 1590, 1589, 1588, 1587, 1586, 1585, 1584, 1583, 1582, 1581, 1580, 1579, 1578, 1577, 1576, 1575, 1574, 1573, 1304, 1027, 742, 449, 148], [233, 530, 819, 1100, 1373, 1372, 1371, 1370, 1369, 1368, 1367, 1366, 1365, 1364, 1363, 1362, 1361, 1360, 1359, 1358, 1357, 1356, 1355, 1354, 1353, 1352, 1351, 1350, 1349, 1348, 1347, 1346, 1345, 1344, 1343, 1342, 1341, 1340, 1339, 1338, 1337, 1336, 1335, 1334, 1333, 1332, 1331, 1330, 1329, 1328, 1327, 1326, 1325, 1324, 1323, 1322, 1321, 1320, 1319, 1318, 1317, 1316, 1315, 1314, 1313, 1312, 1311, 1310, 1309, 1308, 1307, 1306, 1305, 1028, 743, 450, 149], [232, 529, 818, 1099, 1098, 1097, 1096, 1095, 1094, 1093, 1092, 1091, 1090, 1089, 1088, 1087, 1086, 1085, 1084, 1083, 1082, 1081, 1080, 1079, 1078, 1077, 1076, 1075, 1074, 1073, 1072, 1071, 1070, 1069, 1068, 1067, 1066, 1065, 1064, 1063, 1062, 1061, 1060, 1059, 1058, 1057, 1056, 1055, 1054, 1053, 1052, 1051, 1050, 1049, 1048, 1047, 1046, 1045, 1044, 1043, 1042, 1041, 1040, 1039, 1038, 1037, 1036, 1035, 1034, 1033, 1032, 1031, 1030, 1029, 744, 451, 150], [231, 528, 817, 816, 815, 814, 813, 812, 811, 810, 809, 808, 807, 806, 805, 804, 803, 802, 801, 800, 799, 798, 797, 796, 795, 794, 793, 792, 791, 790, 789, 788, 787, 786, 785, 784, 783, 782, 781, 780, 779, 778, 777, 776, 775, 774, 773, 772, 771, 770, 769, 768, 767, 766, 765, 764, 763, 762, 761, 760, 759, 758, 757, 756, 755, 754, 753, 752, 751, 750, 749, 748, 747, 746, 745, 452, 151], [230, 527, 526, 525, 524, 523, 522, 521, 520, 519, 518, 517, 516, 515, 514, 513, 512, 511, 510, 509, 508, 507, 506, 505, 504, 503, 502, 501, 500, 499, 498, 497, 496, 495, 494, 493, 492, 491, 490, 489, 488, 487, 486, 485, 484, 483, 482, 481, 480, 479, 478, 477, 476, 475, 474, 473, 472, 471, 470, 469, 468, 467, 466, 465, 464, 463, 462, 461, 460, 459, 458, 457, 456, 455, 454, 453, 152], [229, 228, 227, 226, 225, 224, 223, 222, 221, 220, 219, 218, 217, 216, 215, 214, 213, 212, 211, 210, 209, 208, 207, 206, 205, 204, 203, 202, 201, 200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180, 179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165, 164, 163, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153]]
