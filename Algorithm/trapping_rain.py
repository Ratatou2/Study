def trapping_rain(buildings):
    right_max, left_max = 0, 0
    total_rain = 0

    for i in range(len(buildings)):
        if i != 0:
            for j in range(len(buildings[:i])):
                check_left_max = buildings[j]
                left_max = max(check_left_max, buildings[j])

            for k in range(len(buildings[i:])):
                #print("k값", k)
                check_right_max = buildings[k]
                right_max = max(check_right_max, buildings[k])

        fill = buildings[i] - min(right_max, left_max)
        total_rain += fill
    return total_rain


print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))