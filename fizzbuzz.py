class FizzBuzz(object):
    def __init__(self, number):
        if FizzBuzz.is_vaild_number(number):
            self.number = number

    @property
    def result(self):
        if self.number % 3 == 0 and self.number % 5 == 0:
            return "FizzBuzz"
        elif self.number % 3 == 0:
            return "Fizz"
        elif self.number % 5 == 0:
            return "Buzz"
        return self.number

    @staticmethod
    def is_vaild_number(number):
        if number <= 0 or number > 100:
            raise ValueError('Number must be between 0 and 101')
        return True
