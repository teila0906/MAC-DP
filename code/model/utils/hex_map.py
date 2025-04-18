hex_map = {
    0: {0: 0, 4: 1, 5: 4, 6: 3, 13: 2, 14: 5, 15: 11, 16: 10, 17: 9},
    1: {0: 1, 1: 0, 4: 2, 5: 5, 6: 4, 14: 6, 15: 12, 16: 11, 17: 10, 18: 3},
    2: {0: 2, 1: 1, 5: 6, 6: 5, 7: 0, 14: 7, 15: 13, 16: 12, 17: 11, 18: 4},
    3: {0: 3, 3: 0, 4: 4, 5: 10, 6: 9, 12: 1, 13: 5, 14: 11, 15: 17, 16: 16},
    4: {0: 4, 1: 3, 2: 0, 3: 1, 4: 5, 5: 11, 6: 10, 12: 2, 13: 6, 14: 12, 15: 18, 16: 17, 17: 16, 18: 9},
    5: {0: 5, 1: 4, 2: 1, 3: 2, 4: 6, 5: 12, 6: 11, 7: 3, 8: 0, 13: 7, 14: 13, 15: 19, 16: 18, 17: 17, 18: 10},
    6: {0: 6, 1: 5, 2: 2, 4: 7, 5: 13, 6: 12, 7: 4, 8: 1, 13: 8, 14: 14, 15: 20, 16: 19, 17: 18, 18: 11},
    7: {0: 7, 1: 6, 4: 8, 5: 14, 6: 13, 7: 5, 8: 2, 14: 15, 15: 21, 16: 20, 17: 19, 18: 12},
    8: {0: 8, 1: 7, 5: 15, 6: 14, 7: 6, 15: 22, 16: 21, 17: 20, 18: 13},
    9: {0: 9, 3: 3, 4: 10, 5: 16, 11: 0, 12: 4, 13: 11, 14: 17, 15: 24, 16: 23},
    10: {0: 10, 1: 9, 2: 3, 3: 4, 4: 11, 5: 17, 6: 16, 10: 0, 11: 1, 12: 5, 13: 12, 14: 18, 15: 25, 16: 24, 17: 23},
    11: {0: 11, 1: 10, 2: 4, 3: 5, 4: 12, 5: 18, 6: 17, 7: 9, 8: 3, 9: 0, 10: 1, 11: 2, 12: 6, 13: 13, 14: 19, 15: 26, 16: 25, 17: 24, 18: 16},
    12: {0: 12, 1: 11, 2: 5, 3: 6, 4: 13, 5: 19, 6: 18, 7: 10, 8: 4, 9: 1, 10: 2, 12: 7, 13: 14, 14: 20, 15: 27, 16: 26, 17: 25, 18: 17},
    13: {0: 13, 1: 12, 2: 6, 3: 7, 4: 14, 5: 20, 6: 19, 7: 11, 8: 5, 9: 2, 12: 8, 13: 15, 14: 21, 15: 28, 16: 27, 17: 26, 18: 18},
    14: {0: 14, 1: 13, 2: 7, 3: 8, 4: 15, 5: 21, 6: 20, 7: 12, 8: 6, 14: 22, 15: 29, 16: 28, 17: 27, 18: 19},
    15: {0: 15, 1: 14, 2: 8, 5: 22, 6: 21, 7: 13, 8: 7, 15: 30, 16: 29, 17: 28, 18: 20},
    16: {0: 16, 2: 9, 3: 10, 4: 17, 5: 24, 6: 23, 10: 3, 11: 4, 12: 11, 13: 18, 14: 25, 15: 33, 16: 32, 17: 31},
    17: {0: 17, 1: 16, 2: 10, 3: 11, 4: 18, 5: 25, 6: 24, 8: 9, 9: 3, 10: 4, 11: 5, 12: 12, 13: 19, 14: 26, 15: 34, 16: 33, 17: 32, 18: 23},
    18: {0: 18, 1: 17, 2: 11, 3: 12, 4: 19, 5: 26, 6: 25, 7: 16, 8: 10, 9: 4, 10: 5, 11: 6, 12: 13, 13: 20, 14: 27, 15: 35, 16: 34, 17: 33, 18: 24},
    19: {0: 19, 1: 18, 2: 12, 3: 13, 4: 20, 5: 27, 6: 26, 7: 17, 8: 11, 9: 5, 10: 6, 11: 7, 12: 14, 13: 21, 14: 28, 15: 36, 16: 35, 17: 34, 18: 25},
    20: {0: 20, 1: 19, 2: 13, 3: 14, 4: 21, 5: 28, 6: 27, 7: 18, 8: 12, 9: 6, 10: 7, 11: 8, 12: 15, 13: 22, 14: 29, 15: 37, 16: 36, 17: 35, 18: 26},
    21: {0: 21, 1: 20, 2: 14, 3: 15, 4: 22, 5: 29, 6: 28, 7: 19, 8: 13, 9: 7, 10: 8, 14: 30, 15: 38, 16: 37, 17: 36, 18: 27},
    22: {0: 22, 1: 21, 2: 15, 5: 30, 6: 29, 7: 20, 8: 14, 9: 8, 15: 39, 16: 38, 17: 37, 18: 28},
    23: {0: 23, 3: 16, 4: 24, 5: 32, 6: 31, 10: 9, 11: 10, 12: 17, 13: 25, 14: 33, 15: 42, 16: 41, 17: 40},
    24: {0: 24, 1: 23, 2: 16, 3: 17, 4: 25, 5: 33, 6: 32, 9: 9, 10: 10, 11: 11, 12: 18, 13: 26, 14: 34, 15: 43, 16: 42, 17: 41, 18: 31},
    25: {0: 25, 1: 24, 2: 17, 3: 18, 4: 26, 5: 34, 6: 33, 7: 23, 8: 16, 9: 10, 10: 11, 11: 12, 12: 19, 13: 27, 14: 35, 15: 44, 16: 43, 17: 42, 18: 32},
    26: {0: 26, 1: 25, 2: 18, 3: 19, 4: 27, 5: 35, 6: 34, 7: 24, 8: 17, 9: 11, 10: 12, 11: 13, 12: 20, 13: 28, 14: 36, 15: 45, 16: 44, 17: 43, 18: 33},
    27: {0: 27, 1: 26, 2: 19, 3: 20, 4: 28, 5: 36, 6: 35, 7: 25, 8: 18, 9: 12, 10: 13, 11: 14, 12: 21, 13: 29, 14: 37, 15: 46, 16: 45, 17: 44, 18: 34},
    28: {0: 28, 1: 27, 2: 20, 3: 21, 4: 29, 5: 37, 6: 36, 7: 26, 8: 19, 9: 13, 10: 14, 11: 15, 12: 22, 13: 30, 14: 38, 15: 47, 16: 46, 17: 45, 18: 35},
    29: {0: 29, 1: 28, 2: 21, 3: 22, 4: 30, 5: 38, 6: 37, 7: 27, 8: 20, 9: 14, 10: 15, 14: 39, 15: 48, 16: 47, 17: 46, 18: 36},
    30: {0: 30, 1: 29, 2: 22, 5: 39, 6: 38, 7: 28, 8: 21, 9: 15, 15: 49, 16: 48, 17: 47, 18: 37},
    31: {0: 31, 3: 23, 4: 32, 5: 41, 6: 40, 11: 16, 12: 24, 13: 33, 14: 42, 15: 51, 16: 50},
    32: {0: 32, 1: 31, 2: 23, 3: 24, 4: 33, 5: 42, 6: 41, 10: 16, 11: 17, 12: 25, 13: 34, 14: 43, 15: 52, 16: 51, 17: 50, 18: 40},
    33: {0: 33, 1: 32, 2: 24, 3: 25, 4: 34, 5: 43, 6: 42, 7: 31, 8: 23, 9: 16, 10: 17, 11: 18, 12: 26, 13: 35, 14: 44, 15: 53, 16: 52, 17: 51, 18: 41},
    34: {0: 34, 1: 33, 2: 25, 3: 26, 4: 35, 5: 44, 6: 43, 7: 32, 8: 24, 9: 17, 10: 18, 11: 19, 12: 27, 13: 36, 14: 45, 15: 54, 16: 53, 17: 52, 18: 42},
    35: {0: 35, 1: 34, 2: 26, 3: 27, 4: 36, 5: 45, 6: 44, 7: 33, 8: 25, 9: 18, 10: 19, 11: 20, 12: 28, 13: 37, 14: 46, 15: 55, 16: 54, 17: 53, 18: 43},
    36: {0: 36, 1: 35, 2: 27, 3: 28, 4: 37, 5: 46, 6: 45, 7: 34, 8: 26, 9: 19, 10: 20, 11: 21, 12: 29, 13: 38, 14: 47, 15: 56, 16: 55, 17: 54, 18: 44},
    37: {0: 37, 1: 36, 2: 28, 3: 29, 4: 38, 5: 47, 6: 46, 7: 35, 8: 27, 9: 20, 10: 21, 11: 22, 12: 30, 13: 39, 14: 48, 15: 57, 16: 56, 17: 55, 18: 45},
    38: {0: 38, 1: 37, 2: 29, 3: 30, 4: 39, 5: 48, 6: 47, 7: 36, 8: 28, 9: 21, 10: 22, 14: 49, 15: 58, 16: 57, 17: 56, 18: 46},
    39: {0: 39, 1: 38, 2: 30, 5: 49, 6: 48, 7: 37, 8: 29, 9: 22, 15: 59, 16: 58, 17: 57, 18: 47},
    40: {0: 40, 3: 31, 4: 41, 5: 50, 11: 23, 12: 32, 13: 42, 14: 51, 15: 61, 16: 60},
    41: {0: 41, 1: 40, 2: 31, 3: 32, 4: 42, 5: 51, 6: 50, 10: 23, 11: 24, 12: 33, 13: 43, 14: 52, 15: 62, 16: 61, 17: 60},
    42: {0: 42, 1: 41, 2: 32, 3: 33, 4: 43, 5: 52, 6: 51, 7: 40, 8: 31, 9: 23, 10: 24, 11: 25, 12: 34, 13: 44, 14: 53, 15: 63, 16: 62, 17: 61, 18: 50},
    43: {0: 43, 1: 42, 2: 33, 3: 34, 4: 44, 5: 53, 6: 52, 7: 41, 8: 32, 9: 24, 10: 25, 11: 26, 12: 35, 13: 45, 14: 54, 15: 64, 16: 63, 17: 62, 18: 51},
    44: {0: 44, 1: 43, 2: 34, 3: 35, 4: 45, 5: 54, 6: 53, 7: 42, 8: 33, 9: 25, 10: 26, 11: 27, 12: 36, 13: 46, 14: 55, 15: 65, 16: 64, 17: 63, 18: 52},
    45: {0: 45, 1: 44, 2: 35, 3: 36, 4: 46, 5: 55, 6: 54, 7: 43, 8: 34, 9: 26, 10: 27, 11: 28, 12: 37, 13: 47, 14: 56, 15: 66, 16: 65, 17: 64, 18: 53},
    46: {0: 46, 1: 45, 2: 36, 3: 37, 4: 47, 5: 56, 6: 55, 7: 44, 8: 35, 9: 27, 10: 28, 11: 29, 12: 38, 13: 48, 14: 57, 15: 67, 16: 66, 17: 65, 18: 54},
    47: {0: 47, 1: 46, 2: 37, 3: 38, 4: 48, 5: 57, 6: 56, 7: 45, 8: 36, 9: 28, 10: 29, 11: 30, 12: 39, 13: 49, 14: 58, 15: 68, 16: 67, 17: 66, 18: 55},
    48: {0: 48, 1: 47, 2: 38, 3: 39, 4: 49, 5: 58, 6: 57, 7: 46, 8: 37, 9: 29, 10: 30, 14: 59, 15: 69, 16: 68, 17: 67, 18: 56},
    49: {0: 49, 1: 48, 2: 39, 5: 59, 6: 58, 7: 47, 8: 38, 9: 30, 16: 69, 17: 68, 18: 57},
    50: {0: 50, 2: 40, 3: 41, 4: 51, 5: 61, 6: 60, 10: 31, 11: 32, 12: 42, 13: 52, 14: 62, 15: 72, 16: 71, 17: 70},
    51: {0: 51, 1: 50, 2: 41, 3: 42, 4: 52, 5: 62, 6: 61, 8: 40, 9: 31, 10: 32, 11: 33, 12: 43, 13: 53, 14: 63, 15: 73, 16: 72, 17: 71, 18: 60},
    52: {0: 52, 1: 51, 2: 42, 3: 43, 4: 53, 5: 63, 6: 62, 7: 50, 8: 41, 9: 32, 10: 33, 11: 34, 12: 44, 13: 54, 14: 64, 15: 74, 16: 73, 17: 72, 18: 61},
    53: {0: 53, 1: 52, 2: 43, 3: 44, 4: 54, 5: 64, 6: 63, 7: 51, 8: 42, 9: 33, 10: 34, 11: 35, 12: 45, 13: 55, 14: 65, 15: 75, 16: 74, 17: 73, 18: 62},
    54: {0: 54, 1: 53, 2: 44, 3: 45, 4: 55, 5: 65, 6: 64, 7: 52, 8: 43, 9: 34, 10: 35, 11: 36, 12: 46, 13: 56, 14: 66, 15: 76, 16: 75, 17: 74, 18: 63},
    55: {0: 55, 1: 54, 2: 45, 3: 46, 4: 56, 5: 66, 6: 65, 7: 53, 8: 44, 9: 35, 10: 36, 11: 37, 12: 47, 13: 57, 14: 67, 15: 77, 16: 76, 17: 75, 18: 64},
    56: {0: 56, 1: 55, 2: 46, 3: 47, 4: 57, 5: 67, 6: 66, 7: 54, 8: 45, 9: 36, 10: 37, 11: 38, 12: 48, 13: 58, 14: 68, 15: 78, 16: 77, 17: 76, 18: 65},
    57: {0: 57, 1: 56, 2: 47, 3: 48, 4: 58, 5: 68, 6: 67, 7: 55, 8: 46, 9: 37, 10: 38, 11: 39, 12: 49, 13: 59, 14: 69, 15: 79, 16: 78, 17: 77, 18: 66},
    58: {0: 58, 1: 57, 2: 48, 3: 49, 4: 59, 5: 69, 6: 68, 7: 56, 8: 47, 9: 38, 10: 39, 15: 80, 16: 79, 17: 78, 18: 67},
    59: {0: 59, 1: 58, 2: 49, 6: 69, 7: 57, 8: 48, 9: 39, 16: 80, 17: 79, 18: 68},
    60: {0: 60, 3: 50, 4: 61, 5: 71, 6: 70, 10: 40, 11: 41, 12: 51, 13: 62, 14: 72, 15: 82, 16: 81},
    61: {0: 61, 1: 60, 2: 50, 3: 51, 4: 62, 5: 72, 6: 71, 9: 40, 10: 41, 11: 42, 12: 52, 13: 63, 14: 73, 15: 83, 16: 82, 17: 81, 18: 70},
    62: {0: 62, 1: 61, 2: 51, 3: 52, 4: 63, 5: 73, 6: 72, 7: 60, 8: 50, 9: 41, 10: 42, 11: 43, 12: 53, 13: 64, 14: 74, 15: 84, 16: 83, 17: 82, 18: 71},
    63: {0: 63, 1: 62, 2: 52, 3: 53, 4: 64, 5: 74, 6: 73, 7: 61, 8: 51, 9: 42, 10: 43, 11: 44, 12: 54, 13: 65, 14: 75, 15: 85, 16: 84, 17: 83, 18: 72},
    64: {0: 64, 1: 63, 2: 53, 3: 54, 4: 65, 5: 75, 6: 74, 7: 62, 8: 52, 9: 43, 10: 44, 11: 45, 12: 55, 13: 66, 14: 76, 15: 86, 16: 85, 17: 84, 18: 73},
    65: {0: 65, 1: 64, 2: 54, 3: 55, 4: 66, 5: 76, 6: 75, 7: 63, 8: 53, 9: 44, 10: 45, 11: 46, 12: 56, 13: 67, 14: 77, 15: 87, 16: 86, 17: 85, 18: 74},
    66: {0: 66, 1: 65, 2: 55, 3: 56, 4: 67, 5: 77, 6: 76, 7: 64, 8: 54, 9: 45, 10: 46, 11: 47, 12: 57, 13: 68, 14: 78, 15: 88, 16: 87, 17: 86, 18: 75},
    67: {0: 67, 1: 66, 2: 56, 3: 57, 4: 68, 5: 78, 6: 77, 7: 65, 8: 55, 9: 46, 10: 47, 11: 48, 12: 58, 13: 69, 14: 79, 15: 89, 16: 88, 17: 87, 18: 76},
    68: {0: 68, 1: 67, 2: 57, 3: 58, 4: 69, 5: 79, 6: 78, 7: 66, 8: 56, 9: 47, 10: 48, 11: 49, 12: 59, 14: 80, 15: 90, 16: 89, 17: 88, 18: 77},
    69: {0: 69, 1: 68, 2: 58, 3: 59, 5: 80, 6: 79, 7: 67, 8: 57, 9: 48, 10: 49, 16: 90, 17: 89, 18: 78},
    70: {0: 70, 3: 60, 4: 71, 5: 81, 11: 50, 12: 61, 13: 72, 14: 82, 15: 92, 16: 91},
    71: {0: 71, 1: 70, 2: 60, 3: 61, 4: 72, 5: 82, 6: 81, 10: 50, 11: 51, 12: 62, 13: 73, 14: 83, 15: 93, 16: 92, 17: 91},
    72: {0: 72, 1: 71, 2: 61, 3: 62, 4: 73, 5: 83, 6: 82, 7: 70, 8: 60, 9: 50, 10: 51, 11: 52, 12: 63, 13: 74, 14: 84, 15: 94, 16: 93, 17: 92, 18: 81},
    73: {0: 73, 1: 72, 2: 62, 3: 63, 4: 74, 5: 84, 6: 83, 7: 71, 8: 61, 9: 51, 10: 52, 11: 53, 12: 64, 13: 75, 14: 85, 15: 95, 16: 94, 17: 93, 18: 82},
    74: {0: 74, 1: 73, 2: 63, 3: 64, 4: 75, 5: 85, 6: 84, 7: 72, 8: 62, 9: 52, 10: 53, 11: 54, 12: 65, 13: 76, 14: 86, 15: 96, 16: 95, 17: 94, 18: 83},
    75: {0: 75, 1: 74, 2: 64, 3: 65, 4: 76, 5: 86, 6: 85, 7: 73, 8: 63, 9: 53, 10: 54, 11: 55, 12: 66, 13: 77, 14: 87, 15: 97, 16: 96, 17: 95, 18: 84},
    76: {0: 76, 1: 75, 2: 65, 3: 66, 4: 77, 5: 87, 6: 86, 7: 74, 8: 64, 9: 54, 10: 55, 11: 56, 12: 67, 13: 78, 14: 88, 15: 98, 16: 97, 17: 96, 18: 85},
    77: {0: 77, 1: 76, 2: 66, 3: 67, 4: 78, 5: 88, 6: 87, 7: 75, 8: 65, 9: 55, 10: 56, 11: 57, 12: 68, 13: 79, 14: 89, 15: 99, 16: 98, 17: 97, 18: 86},
    78: {0: 78, 1: 77, 2: 67, 3: 68, 4: 79, 5: 89, 6: 88, 7: 76, 8: 66, 9: 56, 10: 57, 11: 58, 12: 69, 13: 80, 14: 90, 15: 100, 16: 99, 17: 98, 18: 87},
    79: {0: 79, 1: 78, 2: 68, 3: 69, 4: 80, 5: 90, 6: 89, 7: 77, 8: 67, 9: 57, 10: 58, 11: 59, 15: 101, 16: 100, 17: 99, 18: 88},
    80: {0: 80, 1: 79, 2: 69, 6: 90, 7: 78, 8: 68, 9: 58, 10: 59, 16: 101, 17: 100, 18: 89},
    81: {0: 81, 2: 70, 3: 71, 4: 82, 5: 92, 6: 91, 10: 60, 11: 61, 12: 72, 13: 83, 14: 93, 15: 102},
    82: {0: 82, 1: 81, 2: 71, 3: 72, 4: 83, 5: 93, 6: 92, 8: 70, 9: 60, 10: 61, 11: 62, 12: 73, 13: 84, 14: 94, 15: 103, 16: 102, 18: 91},
    83: {0: 83, 1: 82, 2: 72, 3: 73, 4: 84, 5: 94, 6: 93, 7: 81, 8: 71, 9: 61, 10: 62, 11: 63, 12: 74, 13: 85, 14: 95, 15: 104, 16: 103, 17: 102, 18: 92},
    84: {0: 84, 1: 83, 2: 73, 3: 74, 4: 85, 5: 95, 6: 94, 7: 82, 8: 72, 9: 62, 10: 63, 11: 64, 12: 75, 13: 86, 14: 96, 15: 105, 16: 104, 17: 103, 18: 93},
    85: {0: 85, 1: 84, 2: 74, 3: 75, 4: 86, 5: 96, 6: 95, 7: 83, 8: 73, 9: 63, 10: 64, 11: 65, 12: 76, 13: 87, 14: 97, 15: 106, 16: 105, 17: 104, 18: 94},
    86: {0: 86, 1: 85, 2: 75, 3: 76, 4: 87, 5: 97, 6: 96, 7: 84, 8: 74, 9: 64, 10: 65, 11: 66, 12: 77, 13: 88, 14: 98, 15: 107, 16: 106, 17: 105, 18: 95},
    87: {0: 87, 1: 86, 2: 76, 3: 77, 4: 88, 5: 98, 6: 97, 7: 85, 8: 75, 9: 65, 10: 66, 11: 67, 12: 78, 13: 89, 14: 99, 15: 108, 16: 107, 17: 106, 18: 96},
    88: {0: 88, 1: 87, 2: 77, 3: 78, 4: 89, 5: 99, 6: 98, 7: 86, 8: 76, 9: 66, 10: 67, 11: 68, 12: 79, 13: 90, 14: 100, 15: 109, 16: 108, 17: 107, 18: 97},
    89: {0: 89, 1: 88, 2: 78, 3: 79, 4: 90, 5: 100, 6: 99, 7: 87, 8: 77, 9: 67, 10: 68, 11: 69, 12: 80, 14: 101, 15: 110, 16: 109, 17: 108, 18: 98},
    90: {0: 90, 1: 89, 2: 79, 3: 80, 5: 101, 6: 100, 7: 88, 8: 78, 9: 68, 10: 69, 15: 111, 16: 110, 17: 109, 18: 99},
    91: {0: 91, 3: 81, 4: 92, 10: 70, 11: 71, 12: 82, 13: 93, 14: 102},
    92: {0: 92, 1: 91, 2: 81, 3: 82, 4: 93, 5: 102, 9: 70, 10: 71, 11: 72, 12: 83, 13: 94, 14: 103},
    93: {0: 93, 1: 92, 2: 82, 3: 83, 4: 94, 5: 103, 6: 102, 7: 91, 8: 81, 9: 71, 10: 72, 11: 73, 12: 84, 13: 95, 14: 104},
    94: {0: 94, 1: 93, 2: 83, 3: 84, 4: 95, 5: 104, 6: 103, 7: 92, 8: 82, 9: 72, 10: 73, 11: 74, 12: 85, 13: 96, 14: 105, 18: 102},
    95: {0: 95, 1: 94, 2: 84, 3: 85, 4: 96, 5: 105, 6: 104, 7: 93, 8: 83, 9: 73, 10: 74, 11: 75, 12: 86, 13: 97, 14: 106, 15: 112, 18: 103},
    96: {0: 96, 1: 95, 2: 85, 3: 86, 4: 97, 5: 106, 6: 105, 7: 94, 8: 84, 9: 74, 10: 75, 11: 76, 12: 87, 13: 98, 14: 107, 15: 113, 16: 112, 18: 104},
    97: {0: 97, 1: 96, 2: 86, 3: 87, 4: 98, 5: 107, 6: 106, 7: 95, 8: 85, 9: 75, 10: 76, 11: 77, 12: 88, 13: 99, 14: 108, 15: 114, 16: 113, 17: 112, 18: 105},
    98: {0: 98, 1: 97, 2: 87, 3: 88, 4: 99, 5: 108, 6: 107, 7: 96, 8: 86, 9: 76, 10: 77, 11: 78, 12: 89, 13: 100, 14: 109, 15: 115, 16: 114, 17: 113, 18: 106},
    99: {0: 99, 1: 98, 2: 88, 3: 89, 4: 100, 5: 109, 6: 108, 7: 97, 8: 87, 9: 77, 10: 78, 11: 79, 12: 90, 13: 101, 14: 110, 15: 116, 16: 115, 17: 114, 18: 107},
    100: {0: 100, 1: 99, 2: 89, 3: 90, 4: 101, 5: 110, 6: 109, 7: 98, 8: 88, 9: 78, 10: 79, 11: 80, 14: 111, 15: 117, 16: 116, 17: 115, 18: 108},
    101: {0: 101, 1: 100, 2: 90, 5: 111, 6: 110, 7: 99, 8: 89, 9: 79, 10: 80, 16: 117, 17: 116, 18: 109},
    102: {0: 102, 2: 92, 3: 93, 4: 103, 8: 91, 9: 81, 10: 82, 11: 83, 12: 94, 13: 104},
    103: {0: 103, 1: 102, 2: 93, 3: 94, 4: 104, 8: 92, 9: 82, 10: 83, 11: 84, 12: 95, 13: 105},
    104: {0: 104, 1: 103, 2: 94, 3: 95, 4: 105, 7: 102, 8: 93, 9: 83, 10: 84, 11: 85, 12: 96, 13: 106, 14: 112},
    105: {0: 105, 1: 104, 2: 95, 3: 96, 4: 106, 5: 112, 7: 103, 8: 94, 9: 84, 10: 85, 11: 86, 12: 97, 13: 107, 14: 113},
    106: {0: 106, 1: 105, 2: 96, 3: 97, 4: 107, 5: 113, 6: 112, 7: 104, 8: 95, 9: 85, 10: 86, 11: 87, 12: 98, 13: 108, 14: 114},
    107: {0: 107, 1: 106, 2: 97, 3: 98, 4: 108, 5: 114, 6: 113, 7: 105, 8: 96, 9: 86, 10: 87, 11: 88, 12: 99, 13: 109, 14: 115, 18: 112},
    108: {0: 108, 1: 107, 2: 98, 3: 99, 4: 109, 5: 115, 6: 114, 7: 106, 8: 97, 9: 87, 10: 88, 11: 89, 12: 100, 13: 110, 14: 116, 15: 118, 18: 113},
    109: {0: 109, 1: 108, 2: 99, 3: 100, 4: 110, 5: 116, 6: 115, 7: 107, 8: 98, 9: 88, 10: 89, 11: 90, 12: 101, 13: 111, 14: 117, 15: 119, 16: 118, 18: 114},
    110: {0: 110, 1: 109, 2: 100, 3: 101, 4: 111, 5: 117, 6: 116, 7: 108, 8: 99, 9: 89, 10: 90, 15: 120, 16: 119, 17: 118, 18: 115},
    111: {0: 111, 1: 110, 2: 101, 6: 117, 7: 109, 8: 100, 9: 90, 16: 120, 17: 119, 18: 116},
    112: {0: 112, 2: 105, 3: 106, 4: 113, 8: 104, 9: 95, 10: 96, 11: 97, 12: 107, 13: 114},
    113: {0: 113, 1: 112, 2: 106, 3: 107, 4: 114, 8: 105, 9: 96, 10: 97, 11: 98, 12: 108, 13: 115},
    114: {0: 114, 1: 113, 2: 107, 3: 108, 4: 115, 7: 112, 8: 106, 9: 97, 10: 98, 11: 99, 12: 109, 13: 116, 14: 118},
    115: {0: 115, 1: 114, 2: 108, 3: 109, 4: 116, 5: 118, 7: 113, 8: 107, 9: 98, 10: 99, 11: 100, 12: 110, 13: 117, 14: 119},
    116: {0: 116, 1: 115, 2: 109, 3: 110, 4: 117, 5: 119, 6: 118, 7: 114, 8: 108, 9: 99, 10: 100, 11: 101, 12: 111, 14: 120},
    117: {0: 117, 1: 116, 2: 110, 3: 111, 5: 120, 6: 119, 7: 115, 8: 109, 9: 100, 10: 101, 18: 118},
    118: {0: 118, 2: 115, 3: 116, 4: 119, 8: 114, 9: 108, 10: 109, 11: 110, 12: 117, 13: 120},
    119: {0: 119, 1: 118, 2: 116, 3: 117, 4: 120, 8: 115, 9: 109, 10: 110, 11: 111},
    120: {0: 120, 1: 119, 2: 117, 7: 118, 8: 116, 9: 110, 10: 111},
}
