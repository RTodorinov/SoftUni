from project.plantation import Plantation
from unittest import TestCase


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(2)

    def test_init_plantation(self):
        self.assertEqual(2, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_is_negative(self):
        with self.assertRaises(ValueError) as ve:
            Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker(self):
        self.assertEqual([], self.plantation.workers)
        self.assertEqual(0, len(self.plantation.workers))

        self.plantation.hire_worker("Test")
        self.assertEqual(["Test"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

    def test_already_hired_worker(self):
        self.plantation.hire_worker("Test")
        self.assertEqual(["Test"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Test")
        self.assertEqual("Worker already hired!", str(ve.exception))
        self.assertEqual(["Test"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

    def test_planting_worker_does_exist(self):
        self.plantation.hire_worker("Test")

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("test2", "test3")
        self.assertEqual("Worker with name test2 is not hired!", str(ve.exception))

    def test_planting_plantation_is_full(self):
        pass

    def test_planting(self):
        self.assertEqual({}, self.plantation.plants)

        self.plantation.hire_worker("Test")
        self.plantation.planting("Test", "rose")

        self.assertEqual({"Test": ["rose"]}, self.plantation.plants)

