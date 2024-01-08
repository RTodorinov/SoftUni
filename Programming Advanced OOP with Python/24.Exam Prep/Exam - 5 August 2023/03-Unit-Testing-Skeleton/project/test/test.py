from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("TestModel", "Test", 100000, 20000)

    def test_init_second_hand_car(self):
        self.assertEqual(self.car.model, "TestModel")
        self.assertEqual(self.car.car_type, "Test")
        self.assertEqual(self.car.mileage, 100000)
        self.assertEqual(self.car.price, 20000)
        self.assertEqual(self.car.repairs, [])
        self.assertListEqual(self.car.repairs, [])

    def test_price_less_than_1_or_equal_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car = SecondHandCar("TestModel", "Test", 100000, 1)
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car = SecondHandCar("TestModel", "Test", 100000, 0.9)
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_less_than_100_or_equal_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car = SecondHandCar("TestModel", "Test", 100, 20000)
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car = SecondHandCar("TestModel", "Test", 99, 20000)
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_promotional_price_more_or_equal_raises(self):
        self.car = SecondHandCar("TestModel", "Test", 200, 100000)
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(100000)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

        self.car = SecondHandCar("TestModel", "Test", 200, 100000)
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(120000)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_promotional_price(self):
        self.assertEqual(self.car.price, 20000)
        result = self.car.set_promotional_price(19000)
        self.assertEqual(self.car.price, 19000)
        self.assertEqual(result, 'The promotional price has been successfully set.')

    def test_need_repair_to_high_price_raises(self):
        self.assertEqual(self.car.price, 20000)
        self.assertEqual(self.car.repairs, [])
        half_price = self.car.price / 2

        result = self.car.need_repair(half_price + 1, "Test repair")

        self.assertEqual(result, 'Repair is impossible!')
        self.assertEqual(self.car.price, 20000)
        self.assertEqual(self.car.repairs, [])

    def test_need_repair(self):
        self.assertEqual(self.car.price, 20000)
        self.assertEqual(self.car.repairs, [])
        half_price = self.car.price / 2 - 1

        current_price = self.car.price
        result = self.car.need_repair(half_price, "Test repair")

        self.assertEqual(result, 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, current_price + half_price)
        self.assertEqual(self.car.repairs, ["Test repair"])

    def test_need_repair_less_than_half_price(self):
        self.assertEqual(self.car.price, 20000)
        self.assertEqual(self.car.repairs, [])
        half_price = self.car.price / 2

        current_price = self.car.price
        result = self.car.need_repair(half_price, "Test repair")

        self.assertEqual(result, 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, current_price + half_price)
        self.assertEqual(self.car.repairs, ["Test repair"])

    def test_compare_different_types_impossible(self):
        car2 = SecondHandCar("TestModel2", "Test2", 9000, 67900)

        result = car2 > self.car
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_compare(self):
        car2 = SecondHandCar("TestModel2", self.car.car_type, 9000, 67900)

        result = car2 > self.car

        self.assertTrue(result)

    def test_str(self):
        self.assertEqual(str(self.car), "Model TestModel | Type Test | Milage 100000km\nCurrent price: 20000.00 | Number of Repairs: 0")


if __name__ == "__main__":
    main()
