#!/usr/bin/python

import socket
def opcao1():
    try:
        ip = input("Digite o ip: ")
        ports = [80,23,443,21,22,25,3389,110,445,139,143,53,135,3306,8080,1723,111,995,993,5900,1025,587,8888,199,1720,465,548,113,81,6001,10000,514,5060,179,1026,2000,8443,8000,32768,554,26,1433,49152,2001,515,8008,49154,1027,5666,646,5000,5631,631,49153,8081,2049,88,79,5800,106,2121,1110,49155,6000,513,990,5357,427,49156,543,544,5101,144,7,389,8009,3128,444,9999,5009,7070,5190,3000,5432,1900,3986,13,1029,9,5051,6646,49157,1028,873,1755,2717,4899,9100,119,37,1000,3001,5001,82,10010,1030,9090,2107,1024,2103,6004,1801,5050,19,8031,1041,255,1049,1048,2967,1053,3703,1056,1065,1064,1054,17,808,3689,1031,1044,1071,5901,100,9102,8010,2869,1039,5120,4001,9000,2105,636,1038,2601,1,7000,1066,1069,625,311,280,254,4000,1993,1761,5003,2002,2005,1998,1032,1050,6112,3690,1521,2161,6002,1080,2401,4045,902,7937,787,1058,2383,32771,1033,1040,1059,50000,5555,10001,1494,593,2301,3,1,3268,7938,1234,1022,1074,8002,1036,1035,9001,1037,464,497,1935,6666,2003,6543,1352,24,3269,1111,407,500,20,2006,3260,15000,1218,1034,4444,264,2004,33,1042,42510,999,3052,1023,1068,222,7100,888,4827,1999,563,1717,2008,992,32770,32772,7001,8082,2007,740,5550,2009,5801,1043,512,2701,7019,50001,1700,4662,2065,2010,42,9535,2602,3333,161,5100,5002,2604,4002,6059,1047,8192,8193,2702,6789,9595,1051,9594,9593,16993,16992,5226,5225,32769,3283,1052,8194,1055,1062,9415,8701,8652,8651,8089,65389,65000,64680,64623,55600,55555,52869,35500,33354,23502,20828,1311,1060,4443,730,731,709,1067,13782,5902,366,9050,1002,85,5500,5431,1864,1863,8085,51103,49999,45100,10243,49,3495,6667,90,475,27000,1503,6881,1500,8021,340,78,5566,8088,2222,9071,8899,6005,9876,1501,5102,32774,32773,9101,5679,163,648,146,1666,901,83,9207,8001,8083,5004,3476,8084,5214,14238,12345,912,30,2605,2030,6,541,8007,3005,4,1248,2500,880,306,4242,1097,9009,2525,1086,1088,8291,52822,6101,900,7200,2809,395,800,32775,12000,1083,211,987,705,20005,711,13783,6969,3071,5269,5222,1085,1046,5987,5989,5988,2190,11967,8600,3766,7627,8087,30000,9010,7741,14000,3367,1099,1098,3031,2718,6580,15002,4129,6901,3827,3580,2144,9900,8181,3801,1718,2811,9080,2135,1045,2399,3017,10002,1148,9002,8873,2875,9011,5718,8086,3998,2607,11110,4126,5911,5910,9618,2381,1096,3300,3351,1073,8333,3784,5633,15660,6123,3211,1078,3659,3551,2260,2160,2100,16001,3325,3323,1104,9968,9503,9502,9485,9290,9220,8994,8649,8222,7911,7625,7106,65129,63331,6156,6129,60020,5962,5961,5960,5959,5925,5877,5825,5810,58080,57294,50800,50006,50003,49160,49159,49158,48080,40193,34573,34572,34571,3404,33899,3301,32782,32781,31038,30718,28201,27715,25734,24800,22939,21571,20221,20031,19842,19801,19101,17988,1783,16018,16016,15003,14442,13456,10629,10628,10626,10621,10617,10616,10566,10025,10024,10012,1169,5030,5414,1057,6788,1947,1094,1075,1108,4003,1081,1093,4449,1687,1840,1100,1063,1061,1107,1106,9500,20222,7778,1077,1310,2119,2492,1070,20000,8400,1272,6389,7777,1072,1079,1082,8402,89,691,1001,32776,1999,212,2020,6003,7002,2998,50002,3372,898,5510,32,2033,4165,3061,5903,99,749,425,43,5405,6106,13722,6502,7007,458,9666,8100,3737,5298,1152,8090,2191,3011,1580,5200,3851,3371,3370,3369,7402,5054,3918,3077,7443,3493,3828,1186,2179,1183,19315,19283,3995,5963,1124,8500,1089,10004,2251,1087,5280,3871,3030,62078,9091,4111,1334,3261,2522,5859,1247,9944,9943,9877,9110,8654,8254,8180,8011,7512,7435,7103,61900,61532,5922,5915,5904,5822,56738,55055,51493,50636,50389,49175,49165,49163,3546,32784,27355,27353,27352,24444,19780,18988,16012,15742,10778,4006,2126,4446,3880,1782,1296,9998,9040,32779,1021,32777,2021,32778,616,666,700,5802,4321,545,1524,1112,49400,84,38292,2040,32780,3006,2111,1084,1600,2048,2638,6699,9111,16080,6547,6007,1533,5560,2106,1443,667,720,2034,555,801,6025,3221,3826,9200,2608,4279,7025,11111,3527,1151,8200,8300,6689,9878,10009,8800,5730,2394,2393,2725,5061,6566,9081,5678,3800,4550,5080,1201,3168,3814,1862,1114,6510,3905,8383,3914,3971,3809,5033,7676,3517,4900,3869,9418,2909,3878,8042,1091,1090,3920,6567,1138,3945,1175,10003,3390,3889,1131,8292,5087,1119,1117,4848,7800,16000,3324,3322,5221,4445,9917,9575,9099,9003,8290,8099,8093,8045,7921,7920,7496,6839,6792,6779,6692,6565,60443,5952,5950,5907,5906,5862,5850,5815,5811,57797,56737,5544,55056,5440,54328,54045,52848,52673,50500,50300,49176,49167,49161,44501,44176,41511,40911,32785,32783,30951,27356,26214,25735,19350,18101,18040,17877,16113,15004,14441,12265,12174,10215,10180,4567,6100,4004,4005,8022,9898,7999,1271,1199,3003,1122,2323,4224,2022,617,777,417,714,6346,981,722,1009,4998,70,1076,5999,10082,765,301,524,668,2041,6009,1417,1434,259,44443,1984,2068,7004,1007,4343,416,2038,6006,109,4125,1461,9103,911,726,1010,2046,2035,7201,687,2013,481,125,6669,6668,903,1455,683,1011,2043,2047,31337,256,9929,5998,406,44442,783,843,2042,2045,4040,6060,6051,1145,3916,9443,9444,1875,7272,4252,4200,7024,1556,13724,1141,1233,8765,1137,3963,5938,9191,3808,8686,3981,2710,3852,3849,3944,3853,9988,1163,4164,3820,6481,3731,5081,40000,8097,4555,3863,1287,4430,7744,1812,7913,1166,1164,1165,8019,10160,4658,7878,3304,3307,1259,1092,7278,3872,10008,7725,3410,1971,3697,3859,3514,4949,4147,7900,5353,3931,8675,1277,3957,1213,2382,6600,3700,3007,4080,1113,3969,1132,1309,3848,7281,3907,3972,3968,1126,5223,1217,3870,3941,8293,1719,1300,2099,6068,3013,3050,1174,3684,2170,3792,1216,5151,7080,22222,4143,5868,8889,12006,1121,3119,8015,10023,3824,1154,20002,3888,4009,5063,3376,1185,1198,1192,1972,1130,1149,4096,6500,8294,3990,3993,8016,3846,3929,1187,5074,8766,1102,2800,9941,9914,9815,9673,9643,9621,9501,9409,9198,9197,9098,8996,8987,8877,8676,8648,8540,8481,8385,8189,8098,8095,8050,7929,7770,7749,7438,7241,7123,7051,7050,6896,6732,6711,65310,6520,6504,6247,6203,61613,60642,60146,60123,5981,5940,59202,59201,59200,5918,5914,59110,5909,5905,5899,58838,5869,58632,58630,5823,5818,5812,5807,58002,58001,57665,55576,55020,53535,5339,53314,53313,53211,52853,52851,52850,52849,52847,5279,52735,52710,52660,5242,5212,51413,51191,5040,50050,49401,49236,49195,49186,49171,49168,49164,4875,47544,46996,46200,44709,41523,41064,40811,3994,39659,39376,39136,38188,38185,37839,35513,33554,33453,32835,32822,32816,32803,32792,32791,30704,30005,29831,29672,28211,27357,26470,23796,23052,2196,21792,19900,18264,18018,17595,16851,16800,16705,15402,15001,12452,12380,12262,12215,12059,12021,10873,10058,10034,10022,10011,2910,1594,1658,1583,3162,2920,26000,2366,4600,1688,1322,2557,1095,1839,2288,1123,5968,9600,1244,1641,2200,1105,6550,5501,1328,2968,1805,1914,1974,31727,3400,1301,1147,1721,1236,2501,2012,6222,1220,1109,1347,502,701,2232,2241,4559,710,10005,5680,623,913,1103,780,930,803,725,639,540,102,5010,1222,953,8118,9992,1270,27,123,86,447,1158,442,18000,419,931,874,856,250,475,2044,441,210,6008,7003,5803,1008,556,6103,829,3299,55,713,1550,709,2628,223,3025,87,57,10083,5520,980,251,1013,9152,1212,2433,1516,333,2011,748,1350,1526,7010,1241,127,157,220,1351,2067,684,77,4333,674,943,904,840,825,792,732,1020,1006,657,557,610,1547,523,996,2025,602,3456,862,600,2903,257,1522,1353,6662,998,660,729,730,731,782,1357,3632,3399,6050,2201,971,969,905,846,839,823,822,795,790,778,757,659,225,1015,1014,1012,655,786,6017,6670,690,388,44334,754,5011,98,411,1525,3999,740,12346,802,1337,1127,2112,1414,2600,621,606,59,928,924,922,921,918,878,864,859,806,805,728,252,1005,1004,641,758,669,38037,715,1413,2104,1229,3817,6063,6062,6055,6052,6030,6021,6015,6010,3220,6115,3940,2340,8006,4141,3810,1565,3511,5986,5985,2723,9202,4036,4035,2312,3652,3280,4243,4298,4297,4294,4262,4234,4220,4206,22555,9300,7121,1927,4433,5070,2148,1168,9979,7998,4414,1823,3653,1223,8201,4876,3240,2644,4020,2436,3906,4375,4024,5581,5580,9694,6251,7345,7325,7320,7300,3121,5473,5475,3600,3943,4912,2142,1976,1975,5202,5201,4016,5111,9911,10006,3923,3930,1221,2973,3909,5814,14001,3080,4158,3526,1911,5066,2711,2187,3788,3796,3922,2292,16161,3102,4881,3979,3670,4174,3483,2631,1750,3897,7500,5553,5554,9875,4570,3860,3712,8052,2083,8883,2271,1208,3319,3935,3430,1215,3962,3368,3964,1128,5557,4010,9400,1605,3291,7400,5005,1699,1195,5053,3813,1712,3002,3765,3806,43000,2371,3532,3799,3790,3599,3850,4355,4358,4357,4356,5433,3928,4713,4374,3961,9022,3911,3396,7628,3200,1753,3967,2505,5133,3658,8471,1314,2558,6161,4025,3089,9021,30001,8472,5014,9990,1159,1157,1308,5723,3443,4161,1135,9211,9210,4090,7789,6619,9628,12121,4454,3680,3167,3902,3901,3890,3842,16900,4700,4687,8980,1196,4407,3520,3812,5012,10115,1615,2902,4118,2706,2095,2096,3363,5137,3795,8005,10007,3515,8003,3847,3503,5252,27017,2197,4120,1180,5722,1134,1883,1249,3311,3837,2804,4558,4190,2463,1204,4056,1184,19333,9333,3913,3672,4342,4877,3586,8282,1861,1752,9592,1701,6085,2081,4058,2115,8900,4328,2958,2957,7071,3899,2531,2691,5052,1638,3419,2551,4029,3603,1336,2082,1143,3602,1176,4100,3486,6077,4800,2062,1918,12001,12002,9084,7072,1156,2313,3952,4999,5023,2069,28017,27019,27018,3439,6324,1188,1125,3908,7501,8232,1722,2988,10500,1136,1162,10020,22128,1211,3530,12009,9005,3057,3956,1191,3519,5235,1144,4745,1901,1807,2425,5912,3210,32767,5015,5013,3622,4039,10101,5233,5152,3983,3982,9616,4369,3728,3621,2291,5114,7101,1315,2087,5234,1635,3263,4121,4602,2224,3949,9131,3310,3937,2253,3882,3831,2376,2375,3876,3362,3663,3334,47624,1825,3868,4302,5721,1279,2606,1173,22125,17500,12005,6113,1973,3793,3637,8954,3742,9667,41795,41794,4300,8445,12865,3365,4665,3190,3577,3823,2261,2262,2812,1190,22350,3374,4135,2598,2567,1167,8470,8116,3830,8880,2734,3505,3388,3669,1871,4325,8025,1958,3681,3014,8999,4415,3414,4101,6503,9700,3683,1150,18333,4376,3991,3989,3992,2302,3415,1179,3946,2203,4192,4418,2712,25565,4065,3915,2080,3103,2265,8202,2304,8060,4119,4401,1560,3904,4534,1835,1116,8023,8474,3879,4087,4112,6350,9950,3506,3948,3825,2325,1800,1153,6379,3839,5672,4689,47806,3975,3980,4113,2847,2070,3425,6628,3997,3513,3656,2335,1182,1954,3996,4599,2391,3479,5021,5020,1558,1924,4545,2991,6065,1290,1559,1317,5423,1707,5055,9975,9971,9919,9915,9912,9910,9908,9901,9844,9830,9826,9825,9823,9814,9812,9777,9745,9683,9680,9679,9674,9665,9661,9654,9648,9620,9619,9613,9583,9527,9513,9493,9478,9464,9454,9364,9351,9183,9170,9133,9130,9128,9125,9065,9061,9044,9037,9013,9004,8925,8898,8887,8882,8879,8878,8865,8843,8801,8798,8790,8772,8756,8752,8736,8680,8673,8658,8655,8644,8640,8621,8601,8562,8539,8531,8530,8515,8484,8479,8477,8455,8454,8453,8452,8451,8409,8339,8308,8295,8273,8268,8255,8248,8245,8144,8133,8110,8092,8064,8037,8029,8018,8014,7975,7895,7854,7853,7852,7830,7813,7788,7780,7772,7771,7688,7685,7654,7637,7600,7555,7553,7456,7451,7231,7218,7184,7119,7104,7102,7092,7068,7067,7043,7033,6973,6972,6956,6942,6922,6920,6897,6877,6780,6734,6725,6710,6709,6650,6647,6644,6606,65514,65488,6535,65311,65048,64890,64727,64726,64551,64507,64438,64320,6412,64127,64080,63803,63675,6349,63423,6323,63156,6310,63105,6309,62866,6274,6273,62674,6259,62570,62519,6250,62312,62188,62080,62042,62006,61942,61851,61827,61734,61722,61669,61617,61616,61516,61473,61402,6126,6120,61170,61169,61159,60989,6091,6090,60794,60789,60783,60782,60753,60743,60728,60713,6067,60628,60621,60612,60579,60544,60504,60492,60485,60403,60401,60377,60279,60243,60227,60177,60111,60086,60055,60003,60002,60000,59987,59841,59829,59810,59778,5975,5974,5971,59684,5966,5958,59565,5954,5953,59525,59510,59509,59504,5949,59499,5948,5945,5939,5936,5934,59340,5931,5927,5926,5924,5923,59239,5921,5920,59191,5917,59160,59149,59122,59107,5908,59087,58991,58970,58908,5888,5887,5881,5878,5875,5874,58721,5871,58699,58634,58622,58610,5860,5858,58570,58562,5854,5853,5852,5849,58498,5848,58468,5845,58456,58446,58430,5840,5839,5838,58374,5836,5834,5831,58310,58305,5827,5826,58252,5824,5821,5820,5817,58164,58109,58107,5808,58072,5806,5804,57999,57988,57928,57923,57896,57891,57733,57730,57702,57681,57678,57576,57479,57398,57387,5737,57352,57350,5734,57347,57335,5732,57325,57123,5711,57103,57020,56975,56973,56827,56822,56810,56725,56723,56681,5667,56668,5665,56591,56535,56507,56293,56259,5622,5621,5620,5612,5611,56055,56016,55948,55910,55907,55901,55781,55773,55758,55721,55684,55652,55635,55579,55569,55568,55556,5552,55527,55479,55426,55400,55382,55350,55312,55227,55187,55183,55000,54991,54987,54907,54873,54741,54722,54688,54658,54605,5458,5457,54551,54514,5444,5442,5441,54323,54321,54276,54263,54235,54127,54101,54075,53958,53910,53852,53827,53782,5377,53742,5370,53690,53656,53639,53633,53491,5347,53469,53460,53370,53361,53319,53240,53212,53189,53178,53085,52948,5291,52893,52675,52665,5261,5259,52573,52506,52477,52391,52262,52237,52230,52226,52225,5219,52173,52071,52046,52025,52003,52002,52001,52000,51965,51961,51909,51906,51809,51800,51772,51771,51658,51582,51515,51488,51485,51484,5147,51460,51423,51366,51351,51343,51300,5125,51240,51235,51234,51233,5122,5121,51139,51118,51067,51037,51020,51011,50997,5098,5096,5095,50945,5090,50903,5088,50887,50854,50849,50836,50835,50834,50833,50831,50815,50809,50787,50733,50692,50585,50577,50576,50545,50529,50513,50356,50277,50258,50246,50224,50205,50202,50198,50189,5017,5016,50101,50040,50019,50016,49927,49803,49765,49762,49751,49678,49603,49597,49522,49521,49520,49519,49500,49498,49452,49398,49372,49352,4931,49302,49275,49241,49235,49232,49228,49216,49213,49211,49204,49203,49202,49201,49197,49196,49191,49190,49189,49179,49173,49172,49170,49169,49166,49132,49048,4903,49002,48973,48967,48966,48925,48813,48783,48682,48648,48631,4860,4859,48434,48356,4819,48167,48153,48127,48083,48067,48009,47969,47966,4793,47860,47858,47850,4778,47777,4771,4770,47700,4767,47634,4760,47595,47581,47567,47448,47372,47348,47267,47197,4712,47119,47029,47012,46992,46813,46593,4649,4644,46436,46418,46372,46310,46182,46171,46115,4609,4606,46069,46034,45960,45864,45777,45697,45624,45602,45463,45438,45413,4530,45226,45220,4517,4516,45164,45136,45050,45038,44981,44965,4476,4471,44711,44704,4464,44628,44616,44541,44505,44479,44431,44410,44380,44200,44119,44101,44004,4388,43868,4384,43823,43734,43690,43654,43425,43242,43231,43212,43143,43139,43103,43027,43018,43002,42990,42906,42735,42685,42679,42675,42632,42590,42575,42560,42559,42452,42449,42322,42276,42251,42158,42127,42035,42001,41808,41773,41632,41551,41442,41398,41348,41345,41342,41318,41281,41250,41142,41123,40951,40834,40812,40754,40732,40712,40628,40614,40513,40489,40457,40400,40393,40306,40011,40005,40003,40002,40001,39917,39895,39883,39869,39795,39774,39763,39732,39630,39489,39482,39433,39380,39293,39265,39117,39067,38936,38805,38780,38764,38761,38570,38561,38546,38481,38446,38358,38331,38313,38270,38224,38205,38194,38029,37855,37789,37777,37674,37647,37614,37607,37522,37393,37218,37185,37174,37151,37121,36983,36962,36950,36914,36824,36823,36748,36710,36694,36677,36659,36552,36530,36508,36436,36368,36275,36256,36105,36104,36046,35986,35929,35906,35901,35900,35879,35731,35593,35553,35506,35401,35393,35392,35349,35272,35217,35131,35116,35050,35033,34875,34833,34783,34765,34728,34683,34510,34507,34401,34381,34341,34317,34189,34096,34036,34021,33895,33889,33882,33879,33841,33605,33604,33550,33523,33522,33444,33395,33367,33337,33335,33327,33277,33203,33200,33192,33175,33124,33087,33070,33017,33011,33000,32976,32961,32960,32944,32932,32911,32910,32908,32905,32904,32898,32897,32888,32871,32869,32868,32858,32842,32837,32820,32815,32814,32807,32799,32798,32797,32790,32789,32788,32765,32764,32261,32260,32219,32200,32102,32088,32031,32022,32006,31728,31657,31522,31438,31386,31339,31072,31058,31033,30896,30705,30659,30644,30599,30519,30299,30195,30087,29810,29507,29243,29152,29045,28967,28924,28851,28850,28717,28567,28374,28142,28114,27770,27537,27521,27372,27351,27350,27316,27204,27087,27075,27074,27055,27016,27015,26972,26669,26417,26340,26007,26001,25847,25717,25703,25486,25473,25445,25327,25288,25262,25260,25174,24999,24616,24552,24416,24392,24218,23953,23887,23723,23451,23430,23382,23342,23296,23270,23228,23219,23040,23017,22969,22959,22882,22769,22727,22719,22711,22563,22341,22290,22223,22200,22177,22100,22063,22022,21915,21891,21728,21634,21631,21473,21078,21011,20990,20940,20934,20883,20734,20473,20280,20228,20227,20226,20225,20224,20223,20180,20179,20147,20127,20125,20118,20111,20106,20102,20089,20085,20080,20076,20052,20039,20032,20021,20017,20011,19996,19995,19852,19715,19634,19612,19501,19464,19403,19353,19201,19200,19130,19010,18962,18910,18887,18874,18669,18569,18517,18505,18439,18380,18337,18336,18231,18148,18080,18015,18012,17997,17985,17969,17867,17860,17802,17801,17715,17702,17701,17700,17413,17409,17255,17251,17129,17089,17070,17017,17016,16901,16845,16797,16725,16724,16723,16464,16372,16349,16297,16286,16283,16273,16270,16048,15915,15758,15730,15722,15677,15670,15646,15645,15631,15550,15448,15344,15317,15275,15191,15190,15145,15050,15005,14916,14891,14827,14733,14693,14545,14534,14444,14443,14418,14254,14237,14218,14147,13899,13846,13784,13766,13730,13723,13695,13580,13502,13359,13340,13318,13306,13265,13264,13261,13250,13229,13194,13193,13192,13188,13167,13149,13142,13140,13132,13130,13093,13017,12962,12955,12892,12891,12766,12702,12699,12414,12340,12296,12275,12271,12251,12243,12240,12225,12192,12171,12156,12146,12137,12132,12097,12096,12090,12080,12077,12034,12031,12019,11940,11863,11862,11813,11735,11697,11552,11401,11296,11288,11250,11224,11200,11180,11100,11089,11033,11032,11031,11026,11019,11007,11003,10900,10878,10852,10842,10754,10699,10602,10601,10567,10565,10556,10555,10554,10553,10552,10551,10550,10535,10529,10509,10494,10443,10414,10387,10357,10347,10338,10280,10255,10246,10245,10238,10093,10064,10045,10042,10035,10019,10018,1327,2330,2580,2700,1584,9020,3281,2439,1250,1607,1736,1330,2270,2728,2888,3803,5250,1645,1303,3636,1251,1243,1291,1297,1200,1811,4442,1118,8401,2101,2889,1694,1730,1912,1745,2250,1306,2997,2449,1262,4007,1101,1268,1735,1858,1264,1711,3118,4601,1321,1598,1305,1632,9995,1307,1981,2532,1808,2435,1194,1622,1239,1799,2882,1683,3063,3062,1340,4447,1806,6888,2438,1261,5969,9343,2583,2031,3798,2269,20001,2622,11001,1207,2850,21201,2908,3936,3023,2280,2623,7099,2372,1318,1339,1276,11000,48619,3497,1209,1331,1240,3856,2987,2326,25001,25000,1792,3919,1299,2984,1715,1703,1677,2086,1708,1228,3787,5502,1620,1316,1569,1210,1691,1282,2124,1791,2150,9909,4022,1324,2584,2300,9287,2806,1566,1713,1592,3749,1302,1709,3485,2418,2472,24554,3146,2134,2898,9161,9160,2930,1319,3811,2456,2901,6579,2550,8403,31416,22273,7005,66,32786,32787,706,635,6105,400,47,830,4008,5977,1989,1444,3985,678,27001,591,642,446,1441,54320,11,769,983,979,973,967,965,961,942,935,926,925,914,863,858,844,834,817,815,811,809,789,779,743,1019,1507,1492,509,762,5632,578,1495,5308,52,219,525,1420,665,620,3064,3045,653,158,716,861,9991,3049,1366,1364,833,91,1680,3398,750,615,603,6110,101,989,27010,510,810,1139,4199,76,847,649,707,68,449,664,75,104,629,1652,682,577,985,984,974,958,952,949,946,923,916,899,897,894,889,835,824,814,807,804,798,733,727,237,12,10,501,122,440,771,1663,828,860,695,634,538,1359,1358,1517,1370,3900,492,268,27374,605,8076,1651,1178,6401,761,5145,50,2018,1349,2014,7597,2120,1445,1402,1465,9104,627,4660,7273,950,1384,1388,760,92,831,5978,4557,45,112,456,1214,3086,702,6665,1404,651,5300,6347,5400,1389,647,448,1356,5232,1484,450,1991,1988,1523,1400,1399,221,1385,5191,1346,2024,2430,988,962,948,945,941,938,936,929,927,919,906,883,881,875,872,870,866,855,851,850,841,836,826,820,819,816,813,791,745,736,735,724,719,343,334,300,28,249,230,16,1018,1016,658,1474,696,630,663,2307,1552,609,741,353,638,1551,661,491,640,507,673,632,1354,9105,6143,676,214,14141,182,69,27665,1475,97,633,560,799,7009,2015,628,751,4480,1403,8123,1527,723,1466,1486,1650,991,832,137,1348,685,1762,6701,994,4500,194,180,1539,1379,51,886,2064,1405,1435,11371,1401,1369,402,103,1372,704,854,8892,47557,624,1387,3397,1996,1995,1997,18182,18184,3264,3292,13720,9107,9106,201,1381,35,6588,5530,3141,670,970,968,964,963,960,959,951,947,944,939,933,909,895,891,879,869,868,867,837,821,812,797,796,794,788,756,734,721,718,708,703,60,40,253,231,14,1017,1003,656,975,2026,1497,553,511,611,689,1668,1664,15,561,997,505,1496,637,213,1412,1515,692,694,681,680,644,675,1467,454,622,1476,1373,770,262,654,1535,58,177,26208,677,1519,1398,3457,401,412,493,13713,94,1498,871,1390,6145,133,362,118,193,115,1549,7008,608,1426,1436,38,74,73,71,601,136,4144,129,16444,1446,4132,308,1528,1365,1393,1394,1493,138,5997,397,29,31,44,2627,6147,1510,568,350,2053,6146,6544,1763,3531,399,1537,1992,1355,1454,261,887,200,1376,1424,6111,1410,1409,686,5301,5302,1513,747,9051,1499,7006,1439,1438,8770,853,196,93,410,462,619,1529,1990,1994,1986,1386,18183,18181,6700,1442,95,6400,1432,1548,486,1422,114,1397,6142,1827,626,422,688,206,202,204,1483,7634,774,699,2023,776,672,1545,2431,697,982,978,972,966,957,956,934,920,915,908,907,892,890,885,884,882,877,876,865,857,852,849,842,838,827,818,793,785,784,755,746,738,737,717,34,336,325,303,276,273,236,235,233,181,604,1362,712,1437,2027,1368,1531,645,65301,260,536,764,698,607,1667,1662,1661,404,224,418,176,848,315,466,403,1456,1479,355,763,1472,453,759,437,2432,120,415,1544,1511,1538,346,173,54,56,265,1462,13701,1518,1457,117,1470,13715,13714,267,1419,1418,1407,380,518,65,391,392,413,1391,614,1408,162,108,4987,1502,598,582,487,530,1509,72,4672,189,209,270,7464,408,191,1459,5714,5717,5713,564,767,583,1395,192,1448,428,4133,1416,773,1458,526,1363,742,1464,1427,1482,569,571,6141,351,3984,5490,2,13718,373,17300,910,148,7326,271,423,1451,480,1430,1429,781,383,2564,613,612,652,5303,1383,128,19150,1453,190,1505,1371,533,27009,27007,27005,27003,27002,744,1423,1374,141,1440,1396,352,96,48,552,570,217,528,452,451,2766,2108,132,1993,1987,130,18187,216,3421,142,13721,67,15151,364,1411,205,6548,124,116,5193,258,485,599,149,1469,775,2019,516,986,977,976,955,954,937,932,8,896,893,845,768,766,739,337,329,326,305,295,294,293,289,288,277,238,234,229,228,226,522,2028,150,572,596,420,460,1543,358,361,470,360,457,643,322,168,753,369,185,43188,1541,1540,752,496,662,1449,1480,1473,184,1672,1671,1670,435,434,1532,1360,174,472,1361,17007,414,535,432,479,473,151,1542,438,1488,1508,618,316,1367,439,284,542,370,2016,248,1491,44123,41230,7173,5670,18136,3925,7088,1425,17755,17756,4072,5841,2102,4123,2989,10051,10050,31029,3726,9978,9925,6061,6058,6057,6056,6054,6053,6049,6048,6047,6046,6045,6044,6043,6042,6041,6040,6039,6038,6037,6036,6035,6034,6033,6032,6031,6029,6028,6027,6026,6024,6023,6022,6020,6019,6018,6016,6014,6013,6012,6011,36462,5793,3423,3424,4095,3646,3510,3722,3651,14500,3865,15345,3763,38422,3877,9092,5344,2341,6116,2157,165,6936,8041,4888,4889,3074,2165,4389,5770,5769,16619,11876,11877,3741,3633,3840,3717,3716,3590,2805,4537,9762,5007,5006,5358,4879,6114,4185,2784,3724,2596,2595,4417,4845,22321,22289,3219,1338,36411,3861,5166,3674,1785,534,6602,47001,5363,8912,2231,5747,5748,11208,7236,4049,4050,22347,63,3233,3359,4177,48050,3111,3427,5321,5320,3702,2907,8991,8990,2054,4847,9802,9800,4368,5990,3563,5744,5743,12321,12322,9206,9204,9205,9201,9203,2949,2948,6626,8199,4145,3482,2216,13708,3786,3375,7566,2539,2387,3317,2410,2255,3883,4299,4296,4295,4293,4292,4291,4290,4289,4288,4287,4286,4285,4284,4283,4282,4281,4280,4278,4277,4276,4275,4274,4273,4272,4271,4270,4269,4268,4267,4266,4265,4264,4263,4261,4260,4259,4258,4257,4256,4255,4254,4253,4251,4250,4249,4248,4247,4246,4245,4244,4241,4240,4239,4238,4237,4236,4235,4233,4232,4231,4230,4229,4228,4227,4226,4225,4223,4222,4221,4219,4218,4217,4216,4215,4214,4213,4212,4211,4210,4209,4208,4207,4205,4204,4203,4202,4201,2530,5164,28200,3845,3541,4052,21590,1796,25793,8699,8182,4991,2474,5780,3676,24249,1631,6672,6673,3601,5046,3509,1852,2386,8473,7802,4789,3555,12013,12012,3752,3245,3231,16666,6678,17184,9086,9598,3073,2074,1956,2610,3738,2994,2993,2802,1885,14149,13786,10100,9284,14150,10107,4032,2821,3207,14154,24323,2771,5646,2426,18668,2554,4188,3654,8034,5675,15118,4031,2529,2248,1142,19194,433,3534,3664,2537,519,2655,4184,1506,3098,7887,37654,1979,9629,2357,1889,3314,3313,4867,2696,3217,6306,1189,5281,8953,1910,13894,372,3720,1382,2542,3584,4034,145,27999,3791,21800,2670,3492,24678,34249,39681,1846,5197,5462,5463,2862,2977,2978,3468,2675,3474,4422,12753,13709,2573,3012,4307,4725,3346,3686,4070,9555,4711,4323,4322,10200,7727,3608,3959,2405,3858,3857,24322,6118,4176,6442,8937,17224,17225,33434,1906,22351,2158,5153,3885,24465,3040,20167,8066,474,2739,3308,590,3309,7902,7901,7903,20046,5582,5583,7872,13716,13717,13705,6252,2915,1965,3459,3160,3754,3243,10261,7932,7933,5450,11971,379,7548,1832,3805,3805,16789,8320,8321,4423,2296,7359,7358,7357,7356,7355,7354,7353,7352,7351,7350,7349,7348,7347,7346,7344,7343,7342,7341,7340,7339,7338,7337,7336,7335,7334,7333,7332,7331,7330,7329,7328,7327,7324,7323,7322,7321,7319,7318,7317,7316,7315,7314,7313,7312,7311,7310,7309,7308,7307,7306,7305,7304,7303,7302,7301,8140,5196,5195,6130,5474,5471,5472,5470,4146,3713,5048,31457,7631,3544,41121,11600,3696,3696,3549,1380,22951,22800,3521,2060,6083,9668,3552,1814,1977,2576,2729,24680,13710,13712,25900,2403,2402,2470,5203,3579,2306,1450,7015,7012,7011,22763,2156,2493,4019,4018,4017,4015,2392,3175,32249,1627,10104,2609,5406,3251,4094,3241,6514,6418,3734,2679,4953,5008,2880,8243,8280,26133,8555,5629,3547,5639,5638,5637,5115,3723,4950,3895,3894,3491,3318,6419,3185,243,3212,9536,1925,11171,8404,8405,8989,6787,6483,3867,3866,1860,1870,5306,3816,7588,6786,2084,11165,11161,11163,11162,11164,3708,4850,7677,16959,247,3478,5349,3854,5397,7411,9612,11173,9293,5027,5026,5705,8778,527,1312,8808,6144,4157,4156,3249,7471,3615,2154,45966,17235,3018,38800,2737,156,3807,2876,1759,7981,3606,3647,3438,4683,9306,9312,7016,33334,3413,3834,3835,2440,6121,2568,17185,7982,2290,2569,2863,1964,4738,2132,17777,16162,6551,3230,4538,3884,9282,9281,4882,5146,580,1967,2659,2409,5416,2657,3380,5417,2658,5161,5162,10162,10161,33656,7560,2599,2704,2703,4170,7734,9522,3158,4426,4786,2721]
        print(f"Iniciando scanning de portas no IP {ip}...\n")
        for porta in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.01)
            connect = s.connect_ex((ip,porta))
            if connect == 0:
                print(f"    [+] {ip} está com a porta {porta} ABERTA")
                s.close()

        print("\n=================================\nVerificação de portas concluída.\n=================================")
    except:
        print("OCORREU UM ERRO, TALVEZ VOCÊ TENHA INSERIDO O IP INCORRETAMENTE!")
def opcao2():
    print("Digite o IP de rede sem o último byte, Exemplo: 192.168.0")
    ip = input("$: ")

    print(f"Iniciando scanning de portas em todos hosts ativos...\n")

    for ip_final in range(1, 255):
        ip_completo = ip + "." + str(ip_final)
        ports = [80,23,443,21,22,25,3389,110,445,139,143,53,135,3306,8080]
        for porta in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.01)
            connect = s.connect_ex((ip_completo, porta))
            if connect == 0:
                print(f"    [+] {ip_completo} está com a porta {porta} ABERTA")
            s.close()

    print("\nVerificação de portas concluída.")

print("1 - Realizar varredura no host especificado.")
print("2 - Realizar varredura em todos hosts da rede. (Obs: isso pode levar muito tempo!)")
entrada = input("Insira uma Opção: ")

if entrada == "1":
    opcao1()
elif entrada == "2":
    opcao2()
else:
    print("Você digitou incorretamente")
