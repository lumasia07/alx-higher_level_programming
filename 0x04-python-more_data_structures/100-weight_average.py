#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) and my_list:
        score_sum = 0
        weight_sum = 0

        for score, weight in my_list:
            score_sum += score * weight
            weight_sum += weight

        if weight_sum == 0:
            return 0

        return (score_sum/weight_sum)
    return 0
