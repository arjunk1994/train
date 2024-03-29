import unittest
class calc:
    
        
    def add(x, y):
        
        return x + y


    def sub(x, y):
        
        return x - y


    def mul(x, y):
    
        return x * y


    def div(x, y):
    
        if y == 0:
            raise ValueError('Can not divide by zero!')
        return x / y



class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(-1, 1), -2)
        self.assertEqual(calc.sub(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.mul(10, 5), 50)
        self.assertEqual(calc.mul(-1, 1), -1)
        self.assertEqual(calc.mul(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.div(-1, 1), -1)
        self.assertEqual(calc.div(-1, -1), 1)
        self.assertEqual(calc.div(5, 2), 2.5)


if __name__ == '__main__':
    unittest.main()


c=int(input("first number"))
d=int(input("2nd number"))
d=calc()
p=d.add(c,d)
p=d.sub(c,d)
p=d.mul(c,d)
p=d.div(c,d)
    
