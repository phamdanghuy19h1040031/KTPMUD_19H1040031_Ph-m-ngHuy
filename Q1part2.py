class Real_Number:
    def __init__(self, real_number):
        self.real_number = real_number

    def module(self):
        return float(self.real_number)


class Complex_Number(Real_Number):
    def __init__(self, real_number, image_number):
        super().__init__(real_number)
        self.image_number = image_number

    def module(self):
        return (self.real_number ** 2 + self.image_number ** 2) ** 0.5


real = 6
img = -8

real_obj = Real_Number(real)
print(real_obj.module())

complex_obj = Complex_Number(real, img)
print(complex_obj.module())