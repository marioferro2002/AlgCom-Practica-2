import unittest

from main import shipDetector, image_generator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        image= [[240, 202, 71], [147, 105, 44], [9, 71, 196]]
        your_solution = shipDetector(image)
        solution = [[0, 0], [2, 2]]

        self.assertListEqual(your_solution, solution)

    def test_practice_validator_2_x_2 (self):
        image = image_generator(2)
        your_solution = shipDetector(image['image'])

    def test_practice_validator_3_x_3(self):
        image = image_generator(3)
        your_solution = shipDetector(image['image'])

        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_4_x_4(self):
        image = image_generator(4)
        your_solution = shipDetector(image['image'])

        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_5_x_5(self):
        image = image_generator(5)
        your_solution = shipDetector(image['image'])

        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_10_x_10(self):
        image = image_generator(10)
        your_solution = shipDetector(image['image'])

        self.assertListEqual(your_solution, image['solution'])

if __name__ == '__main__':
    unittest.main()
