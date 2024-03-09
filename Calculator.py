import unittest

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive_numbers(self):
        a, b = 8, 10
        result = self.calculator.add(a, b)
        self.assertEqual(result, 18, "Сума 8 і 10 буде 18")

    def test_add_negative_numbers(self):
        a, b = -29, -39
        result = self.calculator.add(a, b)
        self.assertEqual(result, -68, "Сума -29 і -39 має бути -68")

if __name__ == "__main__":
    unittest.main()
    
calculator = Calculator()
result = calculator.devide(6, 2)
print('Віднімання:', result)
