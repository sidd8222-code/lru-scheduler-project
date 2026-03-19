import unittest
from lru_cache import LRUCache
from scheduler import can_attend_all, min_rooms_required


class TestLRUCache(unittest.TestCase):

    def test_lru_basic(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)

        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)


class TestScheduler(unittest.TestCase):

    def test_can_attend(self):
        events = [(9, 10), (10, 11)]
        self.assertTrue(can_attend_all(events))

    def test_overlap(self):
        events = [(9, 11), (10, 12)]
        self.assertFalse(can_attend_all(events))

    def test_rooms(self):
        events = [(9, 11), (10, 12), (11, 13)]
        self.assertEqual(min_rooms_required(events), 2)


if __name__ == "__main__":
    unittest.main()