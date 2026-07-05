import unittest
from engine.math.vector2 import Vector2


class TestVector2(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

        # Test data
        self.v1 = Vector2(5, 12)
        self.v2 = Vector2(10, 25)

    def test_add(self):
        # Positive test case
        result = self.v1 + self.v2
        self.assertEqual(result, Vector2(15, 37))

        # Negative test case for data type
        with self.assertRaises(ValueError) as context:
            self.v1 + "not a vector"
        self.assertEqual(str(context.exception), "Value must be a Vector2.")

    def test_minus(self):
        # Positive test case
        result = self.v1 - self.v2
        self.assertEqual(result, Vector2(-5, -13))

        # Negative test case for data type
        with self.assertRaises(ValueError) as context:
            self.v1 - "not a vector"
        self.assertEqual(str(context.exception), "Value must be a Vector2.")

    def test_mul(self):
        # Positive test case
        result = self.v1 * self.v2
        self.assertEqual(result, Vector2(50, 300))

        # Negative test case for data type
        with self.assertRaises(ValueError) as context:
            self.v1 * "not a vector"
        self.assertEqual(str(context.exception), "Value must be either an integer, a float, or a Vector2.")

    def test_div(self):
        # Positive test case
        result = self.v1 / self.v2
        self.assertEqual(result, Vector2(0.5, 0.48))

        # Negative test case for data type
        with self.assertRaises(ValueError) as context:
            self.v1 / "not a vector"
        self.assertEqual(str(context.exception), "Value must be either an integer, a float, or a Vector2.")

        # Negative test case for zero division
        with self.assertRaises(ValueError):
            self.v1 / Vector2(0, 0)

         # Zero division - zero x component only
        with self.assertRaises(ValueError):
            self.v1 / Vector2(0, 5)

        # Zero division - zero y component only
        with self.assertRaises(ValueError):
            self.v1 / Vector2(5, 0)

    def test_normalise(self):
        # Positive test case
        result = self.v1.normalize()
        self.assertEqual(result, Vector2(0.38461538461538464, 0.9230769230769231))


if __name__ == "__main__":
    unittest.main()