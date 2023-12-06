# times = [48, 93, 84, 66]
# distances = [261, 1192, 1019, 1063]

times = [4893846]
distances = [26111921019106]
# times = [71530]
# distances = [940200]
def calc_distance(total_time, time_preparing):
    return (total_time - time_preparing) * time_preparing

part1 = 1
for time, distance in zip(times, distances):
    curr = 0

    for prepare_time in range(1, time):
        if calc_distance(time, prepare_time) > distance:
            curr += 1

    part1 *= curr

print(part1)