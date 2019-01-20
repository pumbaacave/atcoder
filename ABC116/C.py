num = int(input())
targets = map(int, input().split())
targets = list(targets)


global water_cnt
water_cnt = 0
def exe_water(init_state):
    global water_cnt
    # break condition
    if sum(init_state) == 0:
        return
    temp_water_cnt = min(init_state)
    water_cnt += temp_water_cnt

    lowest = temp_water_cnt
    # init sub_state
    sub_state = []
    for h in init_state:
        substracted_h = h - lowest
        if substracted_h != 0:
            sub_state.append(substracted_h)
        else:
            exe_water(sub_state)
            # reinit for next sequence
            sub_state = []
    # end case where no trailing 0
    exe_water(sub_state)

exe_water(targets)
print(water_cnt)
