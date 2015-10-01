__author__ = 'rfischer'
import sys

_best_profit = 0

def calc_profit(cur_index, cur_profit, cur_contiguos):
    global _best_profit

    new_profit = cur_profit

    # Always calculate the rest of the summation skipping this value, first
    if cur_index+1 < N:
        new_profit = calc_profit(cur_index+1, cur_profit, 0)

    # Next, try with this billboard used, if possible
    if cur_contiguos < K:
        if cur_index+1 < N:
            new_profit = calc_profit(cur_index+1, cur_profit + profit[cur_index], cur_contiguos+1)
        else:
            new_profit = cur_profit + profit[cur_index]

    if new_profit > _best_profit:
        _best_profit = new_profit

    return _best_profit


N, K = [int(x) for x in raw_input().split(' ')]

sys.setrecursionlimit(3000)
profit = []
for i in range(0, N):
    profit.append(int(raw_input()))

print calc_profit(0, 0, 0)