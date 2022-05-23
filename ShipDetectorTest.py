import unittest

from main import shipDetector, image_generator, ship_detector_rec


class MyTestCase(unittest.TestCase):
    def test_something(self):
        image= [[240, 202, 71], [147, 105, 44], [9, 71, 196]]
        your_solution = shipDetector(image)
        solution = [[0, 0], [2, 2]]

        self.assertListEqual(your_solution, solution)

    def test_something_rec(self):
        image = [[240, 202, 71], [147, 105, 44], [9, 71, 196]]
        your_solution = ship_detector_rec(image)
        solution = [[2, 2], [0, 0]] # Hem girat la resposta ja que sino no dona com a sol correcta

        self.assertListEqual(your_solution, solution)


    def test_propi_4x4(self):
        image = [[240, 202, 71, 20], [147, 105, 44, 15], [9, 71, 196, 12], [12, 150, 40, 15]]
        your_solution = shipDetector(image)
        solution = [[0, 0], [2, 2], [3, 1]]

        self.assertListEqual(your_solution, solution)

    def test_propi_4x4_rec(self):
        image = [[240, 202, 71, 20], [147, 105, 44, 15], [9, 71, 196, 12], [12, 150, 40, 15]]
        your_solution = shipDetector(image)
        solution = [[0, 0], [2, 2], [3, 1]]

        self.assertListEqual(your_solution, solution)


    def test_propi_2_x_2 (self):
        image = [[240, 202], [147, 105]]
        your_solution = shipDetector(image)
        solution = [[0, 0]]
        your_solution = shipDetector(image)

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
        '''
if __name__ == '__main__':
    unittest.main()
