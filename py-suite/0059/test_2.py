
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


def test_2():
    assert solution.Solution().generateMatrix(75) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 76], [295, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 370, 77], [294, 583, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 656, 371, 78], [293, 582, 863, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 934, 657, 372, 79], [292, 581, 862, 1135, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1204, 935, 658, 373, 80], [291, 580, 861, 1134, 1399, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686, 1687, 1688, 1689, 1690, 1691, 1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1700, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1466, 1205, 936, 659, 374, 81], [290, 579, 860, 1133, 1398, 1655, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1720, 1467, 1206, 937, 660, 375, 82], [289, 578, 859, 1132, 1397, 1654, 1903, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 1966, 1721, 1468, 1207, 938, 661, 376, 83], [288, 577, 858, 1131, 1396, 1653, 1902, 2143, 2376, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394, 2395, 2396, 2397, 2398, 2399, 2400, 2401, 2402, 2403, 2404, 2405, 2406, 2407, 2408, 2409, 2410, 2411, 2412, 2413, 2414, 2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429, 2430, 2431, 2432, 2433, 2204, 1967, 1722, 1469, 1208, 939, 662, 377, 84], [287, 576, 857, 1130, 1395, 1652, 1901, 2142, 2375, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2607, 2608, 2609, 2610, 2611, 2612, 2613, 2614, 2615, 2616, 2617, 2618, 2619, 2620, 2621, 2622, 2623, 2624, 2625, 2626, 2627, 2628, 2629, 2630, 2631, 2632, 2633, 2634, 2635, 2636, 2637, 2638, 2639, 2640, 2641, 2642, 2643, 2644, 2645, 2646, 2647, 2648, 2649, 2650, 2651, 2652, 2653, 2654, 2655, 2434, 2205, 1968, 1723, 1470, 1209, 940, 663, 378, 85], [286, 575, 856, 1129, 1394, 1651, 1900, 2141, 2374, 2599, 2816, 2817, 2818, 2819, 2820, 2821, 2822, 2823, 2824, 2825, 2826, 2827, 2828, 2829, 2830, 2831, 2832, 2833, 2834, 2835, 2836, 2837, 2838, 2839, 2840, 2841, 2842, 2843, 2844, 2845, 2846, 2847, 2848, 2849, 2850, 2851, 2852, 2853, 2854, 2855, 2856, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2866, 2867, 2868, 2869, 2656, 2435, 2206, 1969, 1724, 1471, 1210, 941, 664, 379, 86], [285, 574, 855, 1128, 1393, 1650, 1899, 2140, 2373, 2598, 2815, 3024, 3025, 3026, 3027, 3028, 3029, 3030, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3041, 3042, 3043, 3044, 3045, 3046, 3047, 3048, 3049, 3050, 3051, 3052, 3053, 3054, 3055, 3056, 3057, 3058, 3059, 3060, 3061, 3062, 3063, 3064, 3065, 3066, 3067, 3068, 3069, 3070, 3071, 3072, 3073, 3074, 3075, 2870, 2657, 2436, 2207, 1970, 1725, 1472, 1211, 942, 665, 380, 87], [284, 573, 854, 1127, 1392, 1649, 1898, 2139, 2372, 2597, 2814, 3023, 3224, 3225, 3226, 3227, 3228, 3229, 3230, 3231, 3232, 3233, 3234, 3235, 3236, 3237, 3238, 3239, 3240, 3241, 3242, 3243, 3244, 3245, 3246, 3247, 3248, 3249, 3250, 3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264, 3265, 3266, 3267, 3268, 3269, 3270, 3271, 3272, 3273, 3076, 2871, 2658, 2437, 2208, 1971, 1726, 1473, 1212, 943, 666, 381, 88], [283, 572, 853, 1126, 1391, 1648, 1897, 2138, 2371, 2596, 2813, 3022, 3223, 3416, 3417, 3418, 3419, 3420, 3421, 3422, 3423, 3424, 3425, 3426, 3427, 3428, 3429, 3430, 3431, 3432, 3433, 3434, 3435, 3436, 3437, 3438, 3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448, 3449, 3450, 3451, 3452, 3453, 3454, 3455, 3456, 3457, 3458, 3459, 3460, 3461, 3462, 3463, 3274, 3077, 2872, 2659, 2438, 2209, 1972, 1727, 1474, 1213, 944, 667, 382, 89], [282, 571, 852, 1125, 1390, 1647, 1896, 2137, 2370, 2595, 2812, 3021, 3222, 3415, 3600, 3601, 3602, 3603, 3604, 3605, 3606, 3607, 3608, 3609, 3610, 3611, 3612, 3613, 3614, 3615, 3616, 3617, 3618, 3619, 3620, 3621, 3622, 3623, 3624, 3625, 3626, 3627, 3628, 3629, 3630, 3631, 3632, 3633, 3634, 3635, 3636, 3637, 3638, 3639, 3640, 3641, 3642, 3643, 3644, 3645, 3464, 3275, 3078, 2873, 2660, 2439, 2210, 1973, 1728, 1475, 1214, 945, 668, 383, 90], [281, 570, 851, 1124, 1389, 1646, 1895, 2136, 2369, 2594, 2811, 3020, 3221, 3414, 3599, 3776, 3777, 3778, 3779, 3780, 3781, 3782, 3783, 3784, 3785, 3786, 3787, 3788, 3789, 3790, 3791, 3792, 3793, 3794, 3795, 3796, 3797, 3798, 3799, 3800, 3801, 3802, 3803, 3804, 3805, 3806, 3807, 3808, 3809, 3810, 3811, 3812, 3813, 3814, 3815, 3816, 3817, 3818, 3819, 3646, 3465, 3276, 3079, 2874, 2661, 2440, 2211, 1974, 1729, 1476, 1215, 946, 669, 384, 91], [280, 569, 850, 1123, 1388, 1645, 1894, 2135, 2368, 2593, 2810, 3019, 3220, 3413, 3598, 3775, 3944, 3945, 3946, 3947, 3948, 3949, 3950, 3951, 3952, 3953, 3954, 3955, 3956, 3957, 3958, 3959, 3960, 3961, 3962, 3963, 3964, 3965, 3966, 3967, 3968, 3969, 3970, 3971, 3972, 3973, 3974, 3975, 3976, 3977, 3978, 3979, 3980, 3981, 3982, 3983, 3984, 3985, 3820, 3647, 3466, 3277, 3080, 2875, 2662, 2441, 2212, 1975, 1730, 1477, 1216, 947, 670, 385, 92], [279, 568, 849, 1122, 1387, 1644, 1893, 2134, 2367, 2592, 2809, 3018, 3219, 3412, 3597, 3774, 3943, 4104, 4105, 4106, 4107, 4108, 4109, 4110, 4111, 4112, 4113, 4114, 4115, 4116, 4117, 4118, 4119, 4120, 4121, 4122, 4123, 4124, 4125, 4126, 4127, 4128, 4129, 4130, 4131, 4132, 4133, 4134, 4135, 4136, 4137, 4138, 4139, 4140, 4141, 4142, 4143, 3986, 3821, 3648, 3467, 3278, 3081, 2876, 2663, 2442, 2213, 1976, 1731, 1478, 1217, 948, 671, 386, 93], [278, 567, 848, 1121, 1386, 1643, 1892, 2133, 2366, 2591, 2808, 3017, 3218, 3411, 3596, 3773, 3942, 4103, 4256, 4257, 4258, 4259, 4260, 4261, 4262, 4263, 4264, 4265, 4266, 4267, 4268, 4269, 4270, 4271, 4272, 4273, 4274, 4275, 4276, 4277, 4278, 4279, 4280, 4281, 4282, 4283, 4284, 4285, 4286, 4287, 4288, 4289, 4290, 4291, 4292, 4293, 4144, 3987, 3822, 3649, 3468, 3279, 3082, 2877, 2664, 2443, 2214, 1977, 1732, 1479, 1218, 949, 672, 387, 94], [277, 566, 847, 1120, 1385, 1642, 1891, 2132, 2365, 2590, 2807, 3016, 3217, 3410, 3595, 3772, 3941, 4102, 4255, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407, 4408, 4409, 4410, 4411, 4412, 4413, 4414, 4415, 4416, 4417, 4418, 4419, 4420, 4421, 4422, 4423, 4424, 4425, 4426, 4427, 4428, 4429, 4430, 4431, 4432, 4433, 4434, 4435, 4294, 4145, 3988, 3823, 3650, 3469, 3280, 3083, 2878, 2665, 2444, 2215, 1978, 1733, 1480, 1219, 950, 673, 388, 95], [276, 565, 846, 1119, 1384, 1641, 1890, 2131, 2364, 2589, 2806, 3015, 3216, 3409, 3594, 3771, 3940, 4101, 4254, 4399, 4536, 4537, 4538, 4539, 4540, 4541, 4542, 4543, 4544, 4545, 4546, 4547, 4548, 4549, 4550, 4551, 4552, 4553, 4554, 4555, 4556, 4557, 4558, 4559, 4560, 4561, 4562, 4563, 4564, 4565, 4566, 4567, 4568, 4569, 4436, 4295, 4146, 3989, 3824, 3651, 3470, 3281, 3084, 2879, 2666, 2445, 2216, 1979, 1734, 1481, 1220, 951, 674, 389, 96], [275, 564, 845, 1118, 1383, 1640, 1889, 2130, 2363, 2588, 2805, 3014, 3215, 3408, 3593, 3770, 3939, 4100, 4253, 4398, 4535, 4664, 4665, 4666, 4667, 4668, 4669, 4670, 4671, 4672, 4673, 4674, 4675, 4676, 4677, 4678, 4679, 4680, 4681, 4682, 4683, 4684, 4685, 4686, 4687, 4688, 4689, 4690, 4691, 4692, 4693, 4694, 4695, 4570, 4437, 4296, 4147, 3990, 3825, 3652, 3471, 3282, 3085, 2880, 2667, 2446, 2217, 1980, 1735, 1482, 1221, 952, 675, 390, 97], [274, 563, 844, 1117, 1382, 1639, 1888, 2129, 2362, 2587, 2804, 3013, 3214, 3407, 3592, 3769, 3938, 4099, 4252, 4397, 4534, 4663, 4784, 4785, 4786, 4787, 4788, 4789, 4790, 4791, 4792, 4793, 4794, 4795, 4796, 4797, 4798, 4799, 4800, 4801, 4802, 4803, 4804, 4805, 4806, 4807, 4808, 4809, 4810, 4811, 4812, 4813, 4696, 4571, 4438, 4297, 4148, 3991, 3826, 3653, 3472, 3283, 3086, 2881, 2668, 2447, 2218, 1981, 1736, 1483, 1222, 953, 676, 391, 98], [273, 562, 843, 1116, 1381, 1638, 1887, 2128, 2361, 2586, 2803, 3012, 3213, 3406, 3591, 3768, 3937, 4098, 4251, 4396, 4533, 4662, 4783, 4896, 4897, 4898, 4899, 4900, 4901, 4902, 4903, 4904, 4905, 4906, 4907, 4908, 4909, 4910, 4911, 4912, 4913, 4914, 4915, 4916, 4917, 4918, 4919, 4920, 4921, 4922, 4923, 4814, 4697, 4572, 4439, 4298, 4149, 3992, 3827, 3654, 3473, 3284, 3087, 2882, 2669, 2448, 2219, 1982, 1737, 1484, 1223, 954, 677, 392, 99], [272, 561, 842, 1115, 1380, 1637, 1886, 2127, 2360, 2585, 2802, 3011, 3212, 3405, 3590, 3767, 3936, 4097, 4250, 4395, 4532, 4661, 4782, 4895, 5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010, 5011, 5012, 5013, 5014, 5015, 5016, 5017, 5018, 5019, 5020, 5021, 5022, 5023, 5024, 5025, 4924, 4815, 4698, 4573, 4440, 4299, 4150, 3993, 3828, 3655, 3474, 3285, 3088, 2883, 2670, 2449, 2220, 1983, 1738, 1485, 1224, 955, 678, 393, 100], [271, 560, 841, 1114, 1379, 1636, 1885, 2126, 2359, 2584, 2801, 3010, 3211, 3404, 3589, 3766, 3935, 4096, 4249, 4394, 4531, 4660, 4781, 4894, 4999, 5096, 5097, 5098, 5099, 5100, 5101, 5102, 5103, 5104, 5105, 5106, 5107, 5108, 5109, 5110, 5111, 5112, 5113, 5114, 5115, 5116, 5117, 5118, 5119, 5026, 4925, 4816, 4699, 4574, 4441, 4300, 4151, 3994, 3829, 3656, 3475, 3286, 3089, 2884, 2671, 2450, 2221, 1984, 1739, 1486, 1225, 956, 679, 394, 101], [270, 559, 840, 1113, 1378, 1635, 1884, 2125, 2358, 2583, 2800, 3009, 3210, 3403, 3588, 3765, 3934, 4095, 4248, 4393, 4530, 4659, 4780, 4893, 4998, 5095, 5184, 5185, 5186, 5187, 5188, 5189, 5190, 5191, 5192, 5193, 5194, 5195, 5196, 5197, 5198, 5199, 5200, 5201, 5202, 5203, 5204, 5205, 5120, 5027, 4926, 4817, 4700, 4575, 4442, 4301, 4152, 3995, 3830, 3657, 3476, 3287, 3090, 2885, 2672, 2451, 2222, 1985, 1740, 1487, 1226, 957, 680, 395, 102], [269, 558, 839, 1112, 1377, 1634, 1883, 2124, 2357, 2582, 2799, 3008, 3209, 3402, 3587, 3764, 3933, 4094, 4247, 4392, 4529, 4658, 4779, 4892, 4997, 5094, 5183, 5264, 5265, 5266, 5267, 5268, 5269, 5270, 5271, 5272, 5273, 5274, 5275, 5276, 5277, 5278, 5279, 5280, 5281, 5282, 5283, 5206, 5121, 5028, 4927, 4818, 4701, 4576, 4443, 4302, 4153, 3996, 3831, 3658, 3477, 3288, 3091, 2886, 2673, 2452, 2223, 1986, 1741, 1488, 1227, 958, 681, 396, 103], [268, 557, 838, 1111, 1376, 1633, 1882, 2123, 2356, 2581, 2798, 3007, 3208, 3401, 3586, 3763, 3932, 4093, 4246, 4391, 4528, 4657, 4778, 4891, 4996, 5093, 5182, 5263, 5336, 5337, 5338, 5339, 5340, 5341, 5342, 5343, 5344, 5345, 5346, 5347, 5348, 5349, 5350, 5351, 5352, 5353, 5284, 5207, 5122, 5029, 4928, 4819, 4702, 4577, 4444, 4303, 4154, 3997, 3832, 3659, 3478, 3289, 3092, 2887, 2674, 2453, 2224, 1987, 1742, 1489, 1228, 959, 682, 397, 104], [267, 556, 837, 1110, 1375, 1632, 1881, 2122, 2355, 2580, 2797, 3006, 3207, 3400, 3585, 3762, 3931, 4092, 4245, 4390, 4527, 4656, 4777, 4890, 4995, 5092, 5181, 5262, 5335, 5400, 5401, 5402, 5403, 5404, 5405, 5406, 5407, 5408, 5409, 5410, 5411, 5412, 5413, 5414, 5415, 5354, 5285, 5208, 5123, 5030, 4929, 4820, 4703, 4578, 4445, 4304, 4155, 3998, 3833, 3660, 3479, 3290, 3093, 2888, 2675, 2454, 2225, 1988, 1743, 1490, 1229, 960, 683, 398, 105], [266, 555, 836, 1109, 1374, 1631, 1880, 2121, 2354, 2579, 2796, 3005, 3206, 3399, 3584, 3761, 3930, 4091, 4244, 4389, 4526, 4655, 4776, 4889, 4994, 5091, 5180, 5261, 5334, 5399, 5456, 5457, 5458, 5459, 5460, 5461, 5462, 5463, 5464, 5465, 5466, 5467, 5468, 5469, 5416, 5355, 5286, 5209, 5124, 5031, 4930, 4821, 4704, 4579, 4446, 4305, 4156, 3999, 3834, 3661, 3480, 3291, 3094, 2889, 2676, 2455, 2226, 1989, 1744, 1491, 1230, 961, 684, 399, 106], [265, 554, 835, 1108, 1373, 1630, 1879, 2120, 2353, 2578, 2795, 3004, 3205, 3398, 3583, 3760, 3929, 4090, 4243, 4388, 4525, 4654, 4775, 4888, 4993, 5090, 5179, 5260, 5333, 5398, 5455, 5504, 5505, 5506, 5507, 5508, 5509, 5510, 5511, 5512, 5513, 5514, 5515, 5470, 5417, 5356, 5287, 5210, 5125, 5032, 4931, 4822, 4705, 4580, 4447, 4306, 4157, 4000, 3835, 3662, 3481, 3292, 3095, 2890, 2677, 2456, 2227, 1990, 1745, 1492, 1231, 962, 685, 400, 107], [264, 553, 834, 1107, 1372, 1629, 1878, 2119, 2352, 2577, 2794, 3003, 3204, 3397, 3582, 3759, 3928, 4089, 4242, 4387, 4524, 4653, 4774, 4887, 4992, 5089, 5178, 5259, 5332, 5397, 5454, 5503, 5544, 5545, 5546, 5547, 5548, 5549, 5550, 5551, 5552, 5553, 5516, 5471, 5418, 5357, 5288, 5211, 5126, 5033, 4932, 4823, 4706, 4581, 4448, 4307, 4158, 4001, 3836, 3663, 3482, 3293, 3096, 2891, 2678, 2457, 2228, 1991, 1746, 1493, 1232, 963, 686, 401, 108], [263, 552, 833, 1106, 1371, 1628, 1877, 2118, 2351, 2576, 2793, 3002, 3203, 3396, 3581, 3758, 3927, 4088, 4241, 4386, 4523, 4652, 4773, 4886, 4991, 5088, 5177, 5258, 5331, 5396, 5453, 5502, 5543, 5576, 5577, 5578, 5579, 5580, 5581, 5582, 5583, 5554, 5517, 5472, 5419, 5358, 5289, 5212, 5127, 5034, 4933, 4824, 4707, 4582, 4449, 4308, 4159, 4002, 3837, 3664, 3483, 3294, 3097, 2892, 2679, 2458, 2229, 1992, 1747, 1494, 1233, 964, 687, 402, 109], [262, 551, 832, 1105, 1370, 1627, 1876, 2117, 2350, 2575, 2792, 3001, 3202, 3395, 3580, 3757, 3926, 4087, 4240, 4385, 4522, 4651, 4772, 4885, 4990, 5087, 5176, 5257, 5330, 5395, 5452, 5501, 5542, 5575, 5600, 5601, 5602, 5603, 5604, 5605, 5584, 5555, 5518, 5473, 5420, 5359, 5290, 5213, 5128, 5035, 4934, 4825, 4708, 4583, 4450, 4309, 4160, 4003, 3838, 3665, 3484, 3295, 3098, 2893, 2680, 2459, 2230, 1993, 1748, 1495, 1234, 965, 688, 403, 110], [261, 550, 831, 1104, 1369, 1626, 1875, 2116, 2349, 2574, 2791, 3000, 3201, 3394, 3579, 3756, 3925, 4086, 4239, 4384, 4521, 4650, 4771, 4884, 4989, 5086, 5175, 5256, 5329, 5394, 5451, 5500, 5541, 5574, 5599, 5616, 5617, 5618, 5619, 5606, 5585, 5556, 5519, 5474, 5421, 5360, 5291, 5214, 5129, 5036, 4935, 4826, 4709, 4584, 4451, 4310, 4161, 4004, 3839, 3666, 3485, 3296, 3099, 2894, 2681, 2460, 2231, 1994, 1749, 1496, 1235, 966, 689, 404, 111], [260, 549, 830, 1103, 1368, 1625, 1874, 2115, 2348, 2573, 2790, 2999, 3200, 3393, 3578, 3755, 3924, 4085, 4238, 4383, 4520, 4649, 4770, 4883, 4988, 5085, 5174, 5255, 5328, 5393, 5450, 5499, 5540, 5573, 5598, 5615, 5624, 5625, 5620, 5607, 5586, 5557, 5520, 5475, 5422, 5361, 5292, 5215, 5130, 5037, 4936, 4827, 4710, 4585, 4452, 4311, 4162, 4005, 3840, 3667, 3486, 3297, 3100, 2895, 2682, 2461, 2232, 1995, 1750, 1497, 1236, 967, 690, 405, 112], [259, 548, 829, 1102, 1367, 1624, 1873, 2114, 2347, 2572, 2789, 2998, 3199, 3392, 3577, 3754, 3923, 4084, 4237, 4382, 4519, 4648, 4769, 4882, 4987, 5084, 5173, 5254, 5327, 5392, 5449, 5498, 5539, 5572, 5597, 5614, 5623, 5622, 5621, 5608, 5587, 5558, 5521, 5476, 5423, 5362, 5293, 5216, 5131, 5038, 4937, 4828, 4711, 4586, 4453, 4312, 4163, 4006, 3841, 3668, 3487, 3298, 3101, 2896, 2683, 2462, 2233, 1996, 1751, 1498, 1237, 968, 691, 406, 113], [258, 547, 828, 1101, 1366, 1623, 1872, 2113, 2346, 2571, 2788, 2997, 3198, 3391, 3576, 3753, 3922, 4083, 4236, 4381, 4518, 4647, 4768, 4881, 4986, 5083, 5172, 5253, 5326, 5391, 5448, 5497, 5538, 5571, 5596, 5613, 5612, 5611, 5610, 5609, 5588, 5559, 5522, 5477, 5424, 5363, 5294, 5217, 5132, 5039, 4938, 4829, 4712, 4587, 4454, 4313, 4164, 4007, 3842, 3669, 3488, 3299, 3102, 2897, 2684, 2463, 2234, 1997, 1752, 1499, 1238, 969, 692, 407, 114], [257, 546, 827, 1100, 1365, 1622, 1871, 2112, 2345, 2570, 2787, 2996, 3197, 3390, 3575, 3752, 3921, 4082, 4235, 4380, 4517, 4646, 4767, 4880, 4985, 5082, 5171, 5252, 5325, 5390, 5447, 5496, 5537, 5570, 5595, 5594, 5593, 5592, 5591, 5590, 5589, 5560, 5523, 5478, 5425, 5364, 5295, 5218, 5133, 5040, 4939, 4830, 4713, 4588, 4455, 4314, 4165, 4008, 3843, 3670, 3489, 3300, 3103, 2898, 2685, 2464, 2235, 1998, 1753, 1500, 1239, 970, 693, 408, 115], [256, 545, 826, 1099, 1364, 1621, 1870, 2111, 2344, 2569, 2786, 2995, 3196, 3389, 3574, 3751, 3920, 4081, 4234, 4379, 4516, 4645, 4766, 4879, 4984, 5081, 5170, 5251, 5324, 5389, 5446, 5495, 5536, 5569, 5568, 5567, 5566, 5565, 5564, 5563, 5562, 5561, 5524, 5479, 5426, 5365, 5296, 5219, 5134, 5041, 4940, 4831, 4714, 4589, 4456, 4315, 4166, 4009, 3844, 3671, 3490, 3301, 3104, 2899, 2686, 2465, 2236, 1999, 1754, 1501, 1240, 971, 694, 409, 116], [255, 544, 825, 1098, 1363, 1620, 1869, 2110, 2343, 2568, 2785, 2994, 3195, 3388, 3573, 3750, 3919, 4080, 4233, 4378, 4515, 4644, 4765, 4878, 4983, 5080, 5169, 5250, 5323, 5388, 5445, 5494, 5535, 5534, 5533, 5532, 5531, 5530, 5529, 5528, 5527, 5526, 5525, 5480, 5427, 5366, 5297, 5220, 5135, 5042, 4941, 4832, 4715, 4590, 4457, 4316, 4167, 4010, 3845, 3672, 3491, 3302, 3105, 2900, 2687, 2466, 2237, 2000, 1755, 1502, 1241, 972, 695, 410, 117], [254, 543, 824, 1097, 1362, 1619, 1868, 2109, 2342, 2567, 2784, 2993, 3194, 3387, 3572, 3749, 3918, 4079, 4232, 4377, 4514, 4643, 4764, 4877, 4982, 5079, 5168, 5249, 5322, 5387, 5444, 5493, 5492, 5491, 5490, 5489, 5488, 5487, 5486, 5485, 5484, 5483, 5482, 5481, 5428, 5367, 5298, 5221, 5136, 5043, 4942, 4833, 4716, 4591, 4458, 4317, 4168, 4011, 3846, 3673, 3492, 3303, 3106, 2901, 2688, 2467, 2238, 2001, 1756, 1503, 1242, 973, 696, 411, 118], [253, 542, 823, 1096, 1361, 1618, 1867, 2108, 2341, 2566, 2783, 2992, 3193, 3386, 3571, 3748, 3917, 4078, 4231, 4376, 4513, 4642, 4763, 4876, 4981, 5078, 5167, 5248, 5321, 5386, 5443, 5442, 5441, 5440, 5439, 5438, 5437, 5436, 5435, 5434, 5433, 5432, 5431, 5430, 5429, 5368, 5299, 5222, 5137, 5044, 4943, 4834, 4717, 4592, 4459, 4318, 4169, 4012, 3847, 3674, 3493, 3304, 3107, 2902, 2689, 2468, 2239, 2002, 1757, 1504, 1243, 974, 697, 412, 119], [252, 541, 822, 1095, 1360, 1617, 1866, 2107, 2340, 2565, 2782, 2991, 3192, 3385, 3570, 3747, 3916, 4077, 4230, 4375, 4512, 4641, 4762, 4875, 4980, 5077, 5166, 5247, 5320, 5385, 5384, 5383, 5382, 5381, 5380, 5379, 5378, 5377, 5376, 5375, 5374, 5373, 5372, 5371, 5370, 5369, 5300, 5223, 5138, 5045, 4944, 4835, 4718, 4593, 4460, 4319, 4170, 4013, 3848, 3675, 3494, 3305, 3108, 2903, 2690, 2469, 2240, 2003, 1758, 1505, 1244, 975, 698, 413, 120], [251, 540, 821, 1094, 1359, 1616, 1865, 2106, 2339, 2564, 2781, 2990, 3191, 3384, 3569, 3746, 3915, 4076, 4229, 4374, 4511, 4640, 4761, 4874, 4979, 5076, 5165, 5246, 5319, 5318, 5317, 5316, 5315, 5314, 5313, 5312, 5311, 5310, 5309, 5308, 5307, 5306, 5305, 5304, 5303, 5302, 5301, 5224, 5139, 5046, 4945, 4836, 4719, 4594, 4461, 4320, 4171, 4014, 3849, 3676, 3495, 3306, 3109, 2904, 2691, 2470, 2241, 2004, 1759, 1506, 1245, 976, 699, 414, 121], [250, 539, 820, 1093, 1358, 1615, 1864, 2105, 2338, 2563, 2780, 2989, 3190, 3383, 3568, 3745, 3914, 4075, 4228, 4373, 4510, 4639, 4760, 4873, 4978, 5075, 5164, 5245, 5244, 5243, 5242, 5241, 5240, 5239, 5238, 5237, 5236, 5235, 5234, 5233, 5232, 5231, 5230, 5229, 5228, 5227, 5226, 5225, 5140, 5047, 4946, 4837, 4720, 4595, 4462, 4321, 4172, 4015, 3850, 3677, 3496, 3307, 3110, 2905, 2692, 2471, 2242, 2005, 1760, 1507, 1246, 977, 700, 415, 122], [249, 538, 819, 1092, 1357, 1614, 1863, 2104, 2337, 2562, 2779, 2988, 3189, 3382, 3567, 3744, 3913, 4074, 4227, 4372, 4509, 4638, 4759, 4872, 4977, 5074, 5163, 5162, 5161, 5160, 5159, 5158, 5157, 5156, 5155, 5154, 5153, 5152, 5151, 5150, 5149, 5148, 5147, 5146, 5145, 5144, 5143, 5142, 5141, 5048, 4947, 4838, 4721, 4596, 4463, 4322, 4173, 4016, 3851, 3678, 3497, 3308, 3111, 2906, 2693, 2472, 2243, 2006, 1761, 1508, 1247, 978, 701, 416, 123], [248, 537, 818, 1091, 1356, 1613, 1862, 2103, 2336, 2561, 2778, 2987, 3188, 3381, 3566, 3743, 3912, 4073, 4226, 4371, 4508, 4637, 4758, 4871, 4976, 5073, 5072, 5071, 5070, 5069, 5068, 5067, 5066, 5065, 5064, 5063, 5062, 5061, 5060, 5059, 5058, 5057, 5056, 5055, 5054, 5053, 5052, 5051, 5050, 5049, 4948, 4839, 4722, 4597, 4464, 4323, 4174, 4017, 3852, 3679, 3498, 3309, 3112, 2907, 2694, 2473, 2244, 2007, 1762, 1509, 1248, 979, 702, 417, 124], [247, 536, 817, 1090, 1355, 1612, 1861, 2102, 2335, 2560, 2777, 2986, 3187, 3380, 3565, 3742, 3911, 4072, 4225, 4370, 4507, 4636, 4757, 4870, 4975, 4974, 4973, 4972, 4971, 4970, 4969, 4968, 4967, 4966, 4965, 4964, 4963, 4962, 4961, 4960, 4959, 4958, 4957, 4956, 4955, 4954, 4953, 4952, 4951, 4950, 4949, 4840, 4723, 4598, 4465, 4324, 4175, 4018, 3853, 3680, 3499, 3310, 3113, 2908, 2695, 2474, 2245, 2008, 1763, 1510, 1249, 980, 703, 418, 125], [246, 535, 816, 1089, 1354, 1611, 1860, 2101, 2334, 2559, 2776, 2985, 3186, 3379, 3564, 3741, 3910, 4071, 4224, 4369, 4506, 4635, 4756, 4869, 4868, 4867, 4866, 4865, 4864, 4863, 4862, 4861, 4860, 4859, 4858, 4857, 4856, 4855, 4854, 4853, 4852, 4851, 4850, 4849, 4848, 4847, 4846, 4845, 4844, 4843, 4842, 4841, 4724, 4599, 4466, 4325, 4176, 4019, 3854, 3681, 3500, 3311, 3114, 2909, 2696, 2475, 2246, 2009, 1764, 1511, 1250, 981, 704, 419, 126], [245, 534, 815, 1088, 1353, 1610, 1859, 2100, 2333, 2558, 2775, 2984, 3185, 3378, 3563, 3740, 3909, 4070, 4223, 4368, 4505, 4634, 4755, 4754, 4753, 4752, 4751, 4750, 4749, 4748, 4747, 4746, 4745, 4744, 4743, 4742, 4741, 4740, 4739, 4738, 4737, 4736, 4735, 4734, 4733, 4732, 4731, 4730, 4729, 4728, 4727, 4726, 4725, 4600, 4467, 4326, 4177, 4020, 3855, 3682, 3501, 3312, 3115, 2910, 2697, 2476, 2247, 2010, 1765, 1512, 1251, 982, 705, 420, 127], [244, 533, 814, 1087, 1352, 1609, 1858, 2099, 2332, 2557, 2774, 2983, 3184, 3377, 3562, 3739, 3908, 4069, 4222, 4367, 4504, 4633, 4632, 4631, 4630, 4629, 4628, 4627, 4626, 4625, 4624, 4623, 4622, 4621, 4620, 4619, 4618, 4617, 4616, 4615, 4614, 4613, 4612, 4611, 4610, 4609, 4608, 4607, 4606, 4605, 4604, 4603, 4602, 4601, 4468, 4327, 4178, 4021, 3856, 3683, 3502, 3313, 3116, 2911, 2698, 2477, 2248, 2011, 1766, 1513, 1252, 983, 706, 421, 128], [243, 532, 813, 1086, 1351, 1608, 1857, 2098, 2331, 2556, 2773, 2982, 3183, 3376, 3561, 3738, 3907, 4068, 4221, 4366, 4503, 4502, 4501, 4500, 4499, 4498, 4497, 4496, 4495, 4494, 4493, 4492, 4491, 4490, 4489, 4488, 4487, 4486, 4485, 4484, 4483, 4482, 4481, 4480, 4479, 4478, 4477, 4476, 4475, 4474, 4473, 4472, 4471, 4470, 4469, 4328, 4179, 4022, 3857, 3684, 3503, 3314, 3117, 2912, 2699, 2478, 2249, 2012, 1767, 1514, 1253, 984, 707, 422, 129], [242, 531, 812, 1085, 1350, 1607, 1856, 2097, 2330, 2555, 2772, 2981, 3182, 3375, 3560, 3737, 3906, 4067, 4220, 4365, 4364, 4363, 4362, 4361, 4360, 4359, 4358, 4357, 4356, 4355, 4354, 4353, 4352, 4351, 4350, 4349, 4348, 4347, 4346, 4345, 4344, 4343, 4342, 4341, 4340, 4339, 4338, 4337, 4336, 4335, 4334, 4333, 4332, 4331, 4330, 4329, 4180, 4023, 3858, 3685, 3504, 3315, 3118, 2913, 2700, 2479, 2250, 2013, 1768, 1515, 1254, 985, 708, 423, 130], [241, 530, 811, 1084, 1349, 1606, 1855, 2096, 2329, 2554, 2771, 2980, 3181, 3374, 3559, 3736, 3905, 4066, 4219, 4218, 4217, 4216, 4215, 4214, 4213, 4212, 4211, 4210, 4209, 4208, 4207, 4206, 4205, 4204, 4203, 4202, 4201, 4200, 4199, 4198, 4197, 4196, 4195, 4194, 4193, 4192, 4191, 4190, 4189, 4188, 4187, 4186, 4185, 4184, 4183, 4182, 4181, 4024, 3859, 3686, 3505, 3316, 3119, 2914, 2701, 2480, 2251, 2014, 1769, 1516, 1255, 986, 709, 424, 131], [240, 529, 810, 1083, 1348, 1605, 1854, 2095, 2328, 2553, 2770, 2979, 3180, 3373, 3558, 3735, 3904, 4065, 4064, 4063, 4062, 4061, 4060, 4059, 4058, 4057, 4056, 4055, 4054, 4053, 4052, 4051, 4050, 4049, 4048, 4047, 4046, 4045, 4044, 4043, 4042, 4041, 4040, 4039, 4038, 4037, 4036, 4035, 4034, 4033, 4032, 4031, 4030, 4029, 4028, 4027, 4026, 4025, 3860, 3687, 3506, 3317, 3120, 2915, 2702, 2481, 2252, 2015, 1770, 1517, 1256, 987, 710, 425, 132], [239, 528, 809, 1082, 1347, 1604, 1853, 2094, 2327, 2552, 2769, 2978, 3179, 3372, 3557, 3734, 3903, 3902, 3901, 3900, 3899, 3898, 3897, 3896, 3895, 3894, 3893, 3892, 3891, 3890, 3889, 3888, 3887, 3886, 3885, 3884, 3883, 3882, 3881, 3880, 3879, 3878, 3877, 3876, 3875, 3874, 3873, 3872, 3871, 3870, 3869, 3868, 3867, 3866, 3865, 3864, 3863, 3862, 3861, 3688, 3507, 3318, 3121, 2916, 2703, 2482, 2253, 2016, 1771, 1518, 1257, 988, 711, 426, 133], [238, 527, 808, 1081, 1346, 1603, 1852, 2093, 2326, 2551, 2768, 2977, 3178, 3371, 3556, 3733, 3732, 3731, 3730, 3729, 3728, 3727, 3726, 3725, 3724, 3723, 3722, 3721, 3720, 3719, 3718, 3717, 3716, 3715, 3714, 3713, 3712, 3711, 3710, 3709, 3708, 3707, 3706, 3705, 3704, 3703, 3702, 3701, 3700, 3699, 3698, 3697, 3696, 3695, 3694, 3693, 3692, 3691, 3690, 3689, 3508, 3319, 3122, 2917, 2704, 2483, 2254, 2017, 1772, 1519, 1258, 989, 712, 427, 134], [237, 526, 807, 1080, 1345, 1602, 1851, 2092, 2325, 2550, 2767, 2976, 3177, 3370, 3555, 3554, 3553, 3552, 3551, 3550, 3549, 3548, 3547, 3546, 3545, 3544, 3543, 3542, 3541, 3540, 3539, 3538, 3537, 3536, 3535, 3534, 3533, 3532, 3531, 3530, 3529, 3528, 3527, 3526, 3525, 3524, 3523, 3522, 3521, 3520, 3519, 3518, 3517, 3516, 3515, 3514, 3513, 3512, 3511, 3510, 3509, 3320, 3123, 2918, 2705, 2484, 2255, 2018, 1773, 1520, 1259, 990, 713, 428, 135], [236, 525, 806, 1079, 1344, 1601, 1850, 2091, 2324, 2549, 2766, 2975, 3176, 3369, 3368, 3367, 3366, 3365, 3364, 3363, 3362, 3361, 3360, 3359, 3358, 3357, 3356, 3355, 3354, 3353, 3352, 3351, 3350, 3349, 3348, 3347, 3346, 3345, 3344, 3343, 3342, 3341, 3340, 3339, 3338, 3337, 3336, 3335, 3334, 3333, 3332, 3331, 3330, 3329, 3328, 3327, 3326, 3325, 3324, 3323, 3322, 3321, 3124, 2919, 2706, 2485, 2256, 2019, 1774, 1521, 1260, 991, 714, 429, 136], [235, 524, 805, 1078, 1343, 1600, 1849, 2090, 2323, 2548, 2765, 2974, 3175, 3174, 3173, 3172, 3171, 3170, 3169, 3168, 3167, 3166, 3165, 3164, 3163, 3162, 3161, 3160, 3159, 3158, 3157, 3156, 3155, 3154, 3153, 3152, 3151, 3150, 3149, 3148, 3147, 3146, 3145, 3144, 3143, 3142, 3141, 3140, 3139, 3138, 3137, 3136, 3135, 3134, 3133, 3132, 3131, 3130, 3129, 3128, 3127, 3126, 3125, 2920, 2707, 2486, 2257, 2020, 1775, 1522, 1261, 992, 715, 430, 137], [234, 523, 804, 1077, 1342, 1599, 1848, 2089, 2322, 2547, 2764, 2973, 2972, 2971, 2970, 2969, 2968, 2967, 2966, 2965, 2964, 2963, 2962, 2961, 2960, 2959, 2958, 2957, 2956, 2955, 2954, 2953, 2952, 2951, 2950, 2949, 2948, 2947, 2946, 2945, 2944, 2943, 2942, 2941, 2940, 2939, 2938, 2937, 2936, 2935, 2934, 2933, 2932, 2931, 2930, 2929, 2928, 2927, 2926, 2925, 2924, 2923, 2922, 2921, 2708, 2487, 2258, 2021, 1776, 1523, 1262, 993, 716, 431, 138], [233, 522, 803, 1076, 1341, 1598, 1847, 2088, 2321, 2546, 2763, 2762, 2761, 2760, 2759, 2758, 2757, 2756, 2755, 2754, 2753, 2752, 2751, 2750, 2749, 2748, 2747, 2746, 2745, 2744, 2743, 2742, 2741, 2740, 2739, 2738, 2737, 2736, 2735, 2734, 2733, 2732, 2731, 2730, 2729, 2728, 2727, 2726, 2725, 2724, 2723, 2722, 2721, 2720, 2719, 2718, 2717, 2716, 2715, 2714, 2713, 2712, 2711, 2710, 2709, 2488, 2259, 2022, 1777, 1524, 1263, 994, 717, 432, 139], [232, 521, 802, 1075, 1340, 1597, 1846, 2087, 2320, 2545, 2544, 2543, 2542, 2541, 2540, 2539, 2538, 2537, 2536, 2535, 2534, 2533, 2532, 2531, 2530, 2529, 2528, 2527, 2526, 2525, 2524, 2523, 2522, 2521, 2520, 2519, 2518, 2517, 2516, 2515, 2514, 2513, 2512, 2511, 2510, 2509, 2508, 2507, 2506, 2505, 2504, 2503, 2502, 2501, 2500, 2499, 2498, 2497, 2496, 2495, 2494, 2493, 2492, 2491, 2490, 2489, 2260, 2023, 1778, 1525, 1264, 995, 718, 433, 140], [231, 520, 801, 1074, 1339, 1596, 1845, 2086, 2319, 2318, 2317, 2316, 2315, 2314, 2313, 2312, 2311, 2310, 2309, 2308, 2307, 2306, 2305, 2304, 2303, 2302, 2301, 2300, 2299, 2298, 2297, 2296, 2295, 2294, 2293, 2292, 2291, 2290, 2289, 2288, 2287, 2286, 2285, 2284, 2283, 2282, 2281, 2280, 2279, 2278, 2277, 2276, 2275, 2274, 2273, 2272, 2271, 2270, 2269, 2268, 2267, 2266, 2265, 2264, 2263, 2262, 2261, 2024, 1779, 1526, 1265, 996, 719, 434, 141], [230, 519, 800, 1073, 1338, 1595, 1844, 2085, 2084, 2083, 2082, 2081, 2080, 2079, 2078, 2077, 2076, 2075, 2074, 2073, 2072, 2071, 2070, 2069, 2068, 2067, 2066, 2065, 2064, 2063, 2062, 2061, 2060, 2059, 2058, 2057, 2056, 2055, 2054, 2053, 2052, 2051, 2050, 2049, 2048, 2047, 2046, 2045, 2044, 2043, 2042, 2041, 2040, 2039, 2038, 2037, 2036, 2035, 2034, 2033, 2032, 2031, 2030, 2029, 2028, 2027, 2026, 2025, 1780, 1527, 1266, 997, 720, 435, 142], [229, 518, 799, 1072, 1337, 1594, 1843, 1842, 1841, 1840, 1839, 1838, 1837, 1836, 1835, 1834, 1833, 1832, 1831, 1830, 1829, 1828, 1827, 1826, 1825, 1824, 1823, 1822, 1821, 1820, 1819, 1818, 1817, 1816, 1815, 1814, 1813, 1812, 1811, 1810, 1809, 1808, 1807, 1806, 1805, 1804, 1803, 1802, 1801, 1800, 1799, 1798, 1797, 1796, 1795, 1794, 1793, 1792, 1791, 1790, 1789, 1788, 1787, 1786, 1785, 1784, 1783, 1782, 1781, 1528, 1267, 998, 721, 436, 143], [228, 517, 798, 1071, 1336, 1593, 1592, 1591, 1590, 1589, 1588, 1587, 1586, 1585, 1584, 1583, 1582, 1581, 1580, 1579, 1578, 1577, 1576, 1575, 1574, 1573, 1572, 1571, 1570, 1569, 1568, 1567, 1566, 1565, 1564, 1563, 1562, 1561, 1560, 1559, 1558, 1557, 1556, 1555, 1554, 1553, 1552, 1551, 1550, 1549, 1548, 1547, 1546, 1545, 1544, 1543, 1542, 1541, 1540, 1539, 1538, 1537, 1536, 1535, 1534, 1533, 1532, 1531, 1530, 1529, 1268, 999, 722, 437, 144], [227, 516, 797, 1070, 1335, 1334, 1333, 1332, 1331, 1330, 1329, 1328, 1327, 1326, 1325, 1324, 1323, 1322, 1321, 1320, 1319, 1318, 1317, 1316, 1315, 1314, 1313, 1312, 1311, 1310, 1309, 1308, 1307, 1306, 1305, 1304, 1303, 1302, 1301, 1300, 1299, 1298, 1297, 1296, 1295, 1294, 1293, 1292, 1291, 1290, 1289, 1288, 1287, 1286, 1285, 1284, 1283, 1282, 1281, 1280, 1279, 1278, 1277, 1276, 1275, 1274, 1273, 1272, 1271, 1270, 1269, 1000, 723, 438, 145], [226, 515, 796, 1069, 1068, 1067, 1066, 1065, 1064, 1063, 1062, 1061, 1060, 1059, 1058, 1057, 1056, 1055, 1054, 1053, 1052, 1051, 1050, 1049, 1048, 1047, 1046, 1045, 1044, 1043, 1042, 1041, 1040, 1039, 1038, 1037, 1036, 1035, 1034, 1033, 1032, 1031, 1030, 1029, 1028, 1027, 1026, 1025, 1024, 1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015, 1014, 1013, 1012, 1011, 1010, 1009, 1008, 1007, 1006, 1005, 1004, 1003, 1002, 1001, 724, 439, 146], [225, 514, 795, 794, 793, 792, 791, 790, 789, 788, 787, 786, 785, 784, 783, 782, 781, 780, 779, 778, 777, 776, 775, 774, 773, 772, 771, 770, 769, 768, 767, 766, 765, 764, 763, 762, 761, 760, 759, 758, 757, 756, 755, 754, 753, 752, 751, 750, 749, 748, 747, 746, 745, 744, 743, 742, 741, 740, 739, 738, 737, 736, 735, 734, 733, 732, 731, 730, 729, 728, 727, 726, 725, 440, 147], [224, 513, 512, 511, 510, 509, 508, 507, 506, 505, 504, 503, 502, 501, 500, 499, 498, 497, 496, 495, 494, 493, 492, 491, 490, 489, 488, 487, 486, 485, 484, 483, 482, 481, 480, 479, 478, 477, 476, 475, 474, 473, 472, 471, 470, 469, 468, 467, 466, 465, 464, 463, 462, 461, 460, 459, 458, 457, 456, 455, 454, 453, 452, 451, 450, 449, 448, 447, 446, 445, 444, 443, 442, 441, 148], [223, 222, 221, 220, 219, 218, 217, 216, 215, 214, 213, 212, 211, 210, 209, 208, 207, 206, 205, 204, 203, 202, 201, 200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180, 179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165, 164, 163, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149]]
