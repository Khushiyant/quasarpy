import math

class ComplexCalculator:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def add(self, other):
        """
        Add two complex numbers.
        """
        result_real = self.real_part + other.real_part
        result_imaginary = self.imaginary_part + other.imaginary_part
        return ComplexNumber(result_real, result_imaginary)

    def subtract(self, other):
        """
        Subtract one complex number from another.
        """
        result_real = self.real_part - other.real_part
        result_imaginary = self.imaginary_part - other.imaginary_part
        return ComplexNumber(result_real, result_imaginary)

    def multiply(self, other):
        """
        Multiply two complex numbers.
        """
        result_real = (self.real_part * other.real_part) - (self.imaginary_part * other.imaginary_part)
        result_imaginary = (self.real_part * other.imaginary_part) + (self.imaginary_part * other.real_part)
        return ComplexNumber(result_real, result_imaginary)

    def divide(self, other):
        """
        Divide one complex number by another.
        """
        denominator = (other.real_part ** 2) + (other.imaginary_part ** 2)
        if denominator == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result_real = ((self.real_part * other.real_part) + (self.imaginary_part * other.imaginary_part)) / denominator
        result_imaginary = ((self.imaginary_part * other.real_part) - (self.real_part * other.imaginary_part)) / denominator
        return ComplexNumber(result_real, result_imaginary)

    def power(self, exponent):
        """
        Raise the complex number to a given power.
        """
        if exponent < 0:
            raise ValueError("Exponent must be a non-negative integer.")
        result_real = 1
        result_imaginary = 0
        for _ in range(exponent):
            temp_real = result_real * self.real_part - result_imaginary * self.imaginary_part
            temp_imaginary = result_real * self.imaginary_part + result_imaginary * self.real_part
            result_real = temp_real
            result_imaginary = temp_imaginary
        return ComplexNumber(result_real, result_imaginary)

    def conjugate(self):
        """
        Compute the conjugate of the complex number.
        """
        return ComplexNumber(self.real_part, -self.imaginary_part)

    def modulus(self):
        """
        Compute the modulus of the complex number.
        """
        return (self.real_part ** 2 + self.imaginary_part ** 2) ** 0.5

    def argument(self):
        """
        Compute the argument (angle) of the complex number.
        """
        import math
        return math.atan2(self.imaginary_part, self.real_part)

    def cartesian_to_polar(self):
        """
        Convert the complex number from cartesian to polar form.
        """
        modulus = self.modulus()
        argument = self.argument()
        return modulus, argument

    def polar_to_cartesian(self, modulus, argument):
        """
        Convert the complex number from polar to cartesian form.
        """
        import math
        real_part = modulus * math.cos(argument)
        imaginary_part = modulus * math.sin(argument)
        return ComplexNumber(real_part, imaginary_part)

    def test_addition(self):
        """
        Test the addition method of ComplexCalculator.
        """
        c1 = ComplexNumber(3, 4)
        c2 = ComplexNumber(1, 2)
        result = self.add(c1, c2)
        assert result.real_part == 4
        assert result.imaginary_part == 6

    def test_subtraction(self):
        """
        Test the subtraction method of ComplexCalculator.
        """
        c1 = ComplexNumber(3, 4)
        c2 = ComplexNumber(1, 2)
        result = self.subtract(c1, c2)
        assert result.real_part == 2
        assert result.imaginary_part == 2

    def test_multiplication(self):
        """
        Test the multiplication method of ComplexCalculator.
        """
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(2, 3)
        result = self.multiply(c1, c2)
        assert result.real_part == -4
        assert result.imaginary_part == 7

    def test_division(self):
        """
        Test the division method of ComplexCalculator.
        """
        c1 = ComplexNumber(2, 1)
        c2 = ComplexNumber(1, 1)
        result = self.divide(c1, c2)
        assert result.real_part == 1.5
        assert result.imaginary_part == -0.5

    def test_power(self):
        """
        Test the power method of ComplexCalculator.
        """
        c = ComplexNumber(1, 1)
        result = self.power(c, 3)
        assert result.real_part == -2
        assert result.imaginary_part == 2

    def test_conjugate(self):
        """
        Test the conjugate method of ComplexCalculator.
        """
        c = ComplexNumber(3, -2)
        result = self.conjugate(c)
        assert result.real_part == 3
        assert result.imaginary_part == 2

    def test_modulus(self):
        """
        Test the modulus method of ComplexCalculator.
        """
        c = ComplexNumber(3, 4)
        result = self.modulus(c)
        assert result == 5

    def test_argument(self):
        """
        Test the argument method of ComplexCalculator.
        """
        c = ComplexNumber(1, 1)
        result = self.argument(c)
        assert result == math.pi / 4

    def test_cartesian_to_polar(self):
        """
        Test the cartesian_to_polar method of ComplexCalculator.
        """
        c = ComplexNumber(1, 1)
        modulus, argument = self.cartesian_to_polar(c)
        assert modulus == math.sqrt(2)
        assert argument == math.pi / 4

    def test_polar_to_cartesian(self):
        """
        Test the polar_to_cartesian method of ComplexCalculator.
        """
        modulus = math.sqrt(2)
        argument = math.pi / 4
        result = self.polar_to_cartesian(modulus, argument)
        assert result.real_part == 1
        assert result.imaginary_part == 1

class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        return f"{self.real_part} + {self.imaginary_part}i"