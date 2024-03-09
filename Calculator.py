import unittest

class Calculator:
    def add(self, a, b):
        return a + b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive_numbers(self):
        a, b = 8, 10
        result = self.calculator.add(a, b)
        self.assertEqual(result, 18, "Сума 8 і 10 буде 18")

if __name__ == "__main__":
    unittest.main()
    
calculator = Calculator()
result = calculator.devide(6, 2)
print('діленя:', result)
