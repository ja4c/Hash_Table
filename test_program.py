import unittest

from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()

    def test_collection_starts_empty(self):
        self.assertEqual(self.ht.collection, {})

    def test_hash_sums_code_points(self):
        self.assertEqual(self.ht.hash("golf"), 424)

    def test_add_single_pair(self):
        self.ht.add("golf", "sport")
        self.assertEqual(self.ht.collection, {424: {"golf": "sport"}})

    def test_add_colliding_keys_share_a_bucket(self):
        self.ht.add("dear", "friend")
        self.ht.add("read", "book")
        self.assertEqual(
            self.ht.collection, {412: {"dear": "friend", "read": "book"}}
        )

    def test_add_rose(self):
        self.ht.add("rose", "flower")
        self.assertEqual(self.ht.collection, {441: {"rose": "flower"}})

    def test_add_fcc_and_cfc(self):
        self.ht.add("fcc", "coding")
        self.ht.add("cfc", "chemical")
        self.assertEqual(
            self.ht.collection, {300: {"fcc": "coding", "cfc": "chemical"}}
        )

    def test_remove_existing_key(self):
        self.ht.add("golf", "sport")
        self.ht.remove("golf")
        self.assertEqual(self.ht.collection, {})

    def test_remove_missing_key_does_nothing(self):
        self.ht.add("golf", "sport")
        self.ht.remove("tennis")
        self.assertEqual(self.ht.collection, {424: {"golf": "sport"}})

    def test_remove_only_deletes_one_colliding_pair(self):
        self.ht.add("fcc", "coding")
        self.ht.add("cfc", "chemical")
        self.ht.remove("fcc")
        self.assertEqual(self.ht.collection, {300: {"cfc": "chemical"}})

    def test_lookup_existing_key(self):
        self.ht.add("golf", "sport")
        self.assertEqual(self.ht.lookup("golf"), "sport")

    def test_lookup_missing_key(self):
        self.assertIsNone(self.ht.lookup("golf"))

    def test_lookup_colliding_but_absent_key(self):
        self.ht.add("fcc", "coding")
        self.assertIsNone(self.ht.lookup("cfc"))


if __name__ == "__main__":
    unittest.main()
