from lru_cache import LRUCache
from scheduler import can_attend_all, min_rooms_required


def test_lru():
    print("===== LRU Cache Test =====")

    cache = LRUCache(2)

    cache.put(1, 10)
    cache.put(2, 20)

    print("Get 1:", cache.get(1))  

    cache.put(3, 30)  
    print("Get 2:", cache.get(2))  

    cache.put(4, 40)  
    print("Get 1:", cache.get(1))  
    print("Get 3:", cache.get(3))  
    print("Get 4:", cache.get(4))  


def test_scheduler():
    print("\n===== Scheduler Test =====")

    events1 = [(9, 10), (10, 11), (11, 12)]
    print("Can attend all (events1):", can_attend_all(events1))

    events2 = [(9, 11), (10, 12), (11, 13)]
    print("Can attend all (events2):", can_attend_all(events2))

    print("Min rooms (events2):", min_rooms_required(events2))
