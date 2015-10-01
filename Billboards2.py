__author__ = 'rfischer'
_best_profit = 0

# TODO: Debug with sample data--it is definitely getting the wrong value
def calc_profit(cur_index, cur_profit, cur_contiguous):
    global _best_profit

    new_profit = cur_profit
    if cur_contiguous < K:
        new_profit = cur_profit + _billboard_profit[cur_index]

    # Always calculate the rest of the summation skipping this value, first
    if cur_index+1 < N:
        new_profit = calc_profit(cur_index+1, new_profit, 0 if cur_contiguous == K else cur_contiguous+1)

    if new_profit > _best_profit:
        _best_profit = new_profit

    return _best_profit


N, K = [int(x) for x in raw_input().split(' ')]


_billboard_profit = []
for i in range(0, N):
    _billboard_profit.append(int(raw_input()))

# TODO: Try without calling this function and see if run time error is on reading of input
print calc_profit(0, 0, K)

when the number of contiguous has not been reached and it is not at the end of the array, profit should be passed through because th

