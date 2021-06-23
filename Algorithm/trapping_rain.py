def trapping_rain(buildings):
    max_right = 0
    max_left = 0
    save_water = 0

    for i in range(len(buildings)):
        point = buildings[i]

        # 오른쪽 최대 높이
        if len(buildings[i:]) != 0:
            max_right = max(buildings[i:])

        if len(buildings[:i]) != 0:
            max_left = max(buildings[:i])

        if i != 0:
            water = min(max_right, max_left) - point
            if water < 0: pass
            elif water >= 0: save_water += water

        # print(i, max_right, max_left, save_water)

    return save_water


print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))