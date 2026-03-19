def can_attend_all(events):
    
    events.sort(key=lambda x: x[0])

    for i in range(1, len(events)):
        if events[i][0] < events[i - 1][1]:
            return False
    return True


def min_rooms_required(events):
    if not events:
        return 0

    starts = sorted([e[0] for e in events])
    ends = sorted([e[1] for e in events])

    s = 0
    e = 0
    rooms = 0
    max_rooms = 0

    while s < len(events):
        if starts[s] < ends[e]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s += 1
        else:
            rooms -= 1
            e += 1

    return max_rooms
