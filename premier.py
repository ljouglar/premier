from timeit import default_timer as timer
from math import sqrt


class Premier:
    def __init__(self):
        self.num_start = 3
        self.num_max = 1000000
        self.primes = [2]

    def _gen_numbers(self):
        number = self.num_start
        while number < self.num_max:
            yield number
            number += 1

    def _gen_prime_dividers(self, tested_number):
        divider_max = sqrt(tested_number)
        for divider in self.primes:
            if divider <= divider_max:
                yield divider
            else:
                raise StopIteration

    def run(self):
        print(2)
        for number in self._gen_numbers():
            for divider in self._gen_prime_dividers(number):
                if number % divider == 0:
                    break
            else:
                self.primes.append(number)
                print(number)


start = timer()
Premier().run()
stop = timer()
print(f"Elapsed time : {stop - start}")