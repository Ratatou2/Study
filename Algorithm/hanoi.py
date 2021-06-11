def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)

    peg_list = [1, 2, 3]
    peg_list.remove(start_peg)
    peg_list.remove(end_peg)
    left_peg = peg_list[0]

    hanoi(num_disks-1, start_peg, left_peg)
    move_disk(num_disks, start_peg,end_peg)
    hanoi(num_disks-1, left_peg, end_peg)

hanoi(3, 1, 3)
