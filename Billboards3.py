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



class SnapShot:
    def __init__(self, contiguous, stage, value):
        self.contiguous = contiguous
        self.stage = stage
        self.value = value

# Add the values from the data set to get the profit for this set
def calc_profit_for_set(data_set):
    total = 0
    for d in data_set:
        total += d.value

    return total

def calc_profit_non_recursive():
    global _best_profit
    t1 = []
    c1 = []
    new_profit = 0

    c1.append(SnapShot(0,0,0))
    while c1:
        # Get the info for the last billboard on the stack
        curSnap = c1.pop()

        # if the last billboard is reached
        if len(c1) == N-1:
            if curSnap.contiguous < K:
                # Stage doesn't matter for this last item.  It is always added if possible,
                # because their is no concern for what comes after it.
                c1.append(SnapShot(curSnap.contiguous+1, 2, profit[len(c1)]))
            else:
                c1.append(SnapShot(0, 2, 0))

            new_profit = calc_profit_for_set(c1)
            if new_profit > _best_profit:
                _best_profit = new_profit

            c1.pop()
        elif curSnap.stage == 0:
            # This is the case where you always try without the current billboard,
            # but don't forget to change the state
            c1.append(SnapShot(0, 1, 0))
            c1.append(SnapShot(0, 0, 0))
        elif curSnap.stage == 1:
            contiguous = 0
            if len(c1) > 0:
                contiguous = c1[len(c1)-1].contiguous
            # Include the billboard, if it is within the bounds of K
            if contiguous < K:
                c1.append(SnapShot(contiguous+1, 2, profit[len(c1)]))
            else:
                c1.append(SnapShot(0, 2, 0))
            c1.append(SnapShot(contiguous+1, 0, 0))

    return _best_profit


N, K = [int(x) for x in raw_input().split(' ')]

profit = []
for i in range(0, N):
    profit.append(int(raw_input()))

print calc_profit_non_recursive()