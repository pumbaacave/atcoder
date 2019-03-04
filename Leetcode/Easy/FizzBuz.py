class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        F = "Fizz"
        B = "Buzz"
        FB = F + B

        def fbfy(num):
            if num % 15 == 0:
                return FB
            elif num % 5 == 0:
                return B
            elif num % 3 == 0:
                return F
            else:
                return str(num)
        nums = range(1, n + 1)
        return list(map(fbfy, nums))
