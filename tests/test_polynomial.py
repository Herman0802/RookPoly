import unittest
from rookpoly import Polynomial


class TestPolynomial(unittest.TestCase):
    def test_init(self):
        # Test initialization from a sequence
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.coeffs, [1, 2, 3])

        # Test initialization from scalars
        p = Polynomial(1, 2, 3)
        self.assertEqual(p.coeffs, [1, 2, 3])

        # Test copy constructor
        p_copy = Polynomial(p)
        self.assertEqual(p_copy.coeffs, p.coeffs)

        # Test initialization with single scalar
        p = Polynomial(5)
        self.assertEqual(p.coeffs, [5])

        # Test initialization with empty sequence
        p = Polynomial([])
        self.assertEqual(p.coeffs, [])

        # Test initialization with trailing zeros
        p = Polynomial([1, 2, 3, 0, 0, 0])
        self.assertEqual(p.coeffs, [1, 2, 3])

    def test_add(self):
        p1 = Polynomial(1, 2, 3)
        p2 = Polynomial(3, 2, 1)
        self.assertEqual((p1 + p2).coeffs, [4, 4, 4])

    def test_add_scalar(self):
        p = Polynomial(1, 2, 3)
        self.assertEqual((p + 5).coeffs, [6, 2, 3])

    def test_call(self):
        p = Polynomial(1, 2, 3)  # 1 + 2X + 3X^2
        self.assertEqual(p(0), 1)
        self.assertEqual(p(1), 6)
        self.assertEqual(p(2), 17)

    def test_eq(self):
        p1 = Polynomial(1, 2, 3)
        p2 = Polynomial(1, 2, 3)
        p3 = Polynomial(3, 2, 1)
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

    def test_eq_scalar(self):
        p = Polynomial(5)
        self.assertTrue(p == 5)
        self.assertFalse(p == 4)

    def test_add(self):
        p1 = Polynomial(1, 2, 3)
        p2 = Polynomial(4, 5, 6)
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [5, 7, 9])

    def test_add_scalar(self):
        p = Polynomial(1, 2, 3)
        p2 = p + 5
        self.assertEqual(p2.coeffs, [6, 2, 3])

    def test_mul(self):
        p1 = Polynomial(1, 2)
        p2 = Polynomial(3, 4)
        self.assertEqual((p1 * p2).coeffs, [3, 10, 8])

    def test_mul_scalar(self):
        p = Polynomial(1, -2, 3)
        self.assertEqual((p * 3).coeffs, [3, -6, 9])

    def test_neg(self):
        p = Polynomial(1, -2, 3)
        self.assertEqual((-p).coeffs, [-1, 2, -3])

    def test_pow(self):
        p1 = Polynomial(1, 2)
        with self.assertRaises(NotImplementedError):
            p2 = p1 ** 2

    def test_radd(self):
        # Test right-hand addition
        p1 = Polynomial(1, 2, 3)
        p2 = 5 + p1
        self.assertEqual(p2.coeffs, [6, 2, 3])

    def test_repr(self):
        p = Polynomial(1, -2, 3)
        self.assertEqual(repr(p), "Polynomial([1, -2, 3])")

    def test_rmul(self):
        # Test right-hand multiplication
        p1 = Polynomial(1, 2, 3)
        p2 = 5 * p1
        self.assertEqual(p2.coeffs, [5, 10, 15])

    def test_rsub(self):
        # Test right-hand subtraction
        p1 = Polynomial(1, 2, 3)
        p2 = 5 - p1
        self.assertEqual(p2.coeffs, [4, -2, -3])

    def test_str(self):
        p1 = Polynomial(0, 1, 0, 2)
        self.assertEqual(str(p1), "2X^3 + 1X")

        p2 = Polynomial(0, -1, 0, 2, 0)
        self.assertEqual(str(p2), "2X^3 + -1X")

        p3 = Polynomial(0, 0, 0, 0)
        self.assertEqual(str(p3), "0")

    def test_sub(self):
        p1 = Polynomial(1, 2, 3)
        p2 = Polynomial(3, 2, 1)
        p3 = p1 - p2
        self.assertEqual(p3.coeffs, [-2, 0, 2])

    def test_sub_scalar(self):
        p = Polynomial(1, 2, -3)
        p2 = p - 5
        self.assertEqual(p2.coeffs, [-4, 2, -3])

    def test_trim(self):
        p1 = Polynomial([21, 0, 0, 37, 0, 0, 0])
        p1.trim()
        self.assertEqual(p1.coeffs, [21, 0, 0, 37])

        p2 = Polynomial([0, 0, 0, 0])
        p2.trim()
        self.assertEqual(p2.coeffs, [])


if __name__ == '__main__':
    unittest.main()
