import math
from typing import Union


# class num
class NUM:
    # constructor, initialize all variables
    def __init__(self, at: int = 0, txt: str = "") -> None:
        self.at = at
        self.txt = txt
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.lo = math.inf
        self.hi = -math.inf
        self.w = -1 if "-" in self.txt else 1
        self.has = {}

    def add(self, n: Union[float, str], count: int = 1) -> None:
        """
        Add n and update values required for standard deviation
        :param n: Union[float, str]:
        :param count: int:
        """
        if n != '?':
            self.n += count
            d = n - self.mu
            self.mu += d / self.n
            self.m2 += d * (n - self.mu)
            self.sd = 0 if self.n < 2 else (self.m2 / (self.n - 1)) ** .5
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self) -> float:
        """
        Get mean
        :return: float: mean value
        """
        return self.mu

    def div(self) -> float:
        """
        Get standard deviation using Welford's Aglorithm
        :return: float: standard deviation
        """
        # return (self.m2 < 0 or self.n < 2) and 0 or (self.m2 / (self.n - 1)) ** 0.5
        if self.m2 < 0 or self.n < 2:
            return 0
        else:
            return (self.m2 / (self.n - 1)) ** 0.5

    def norm(self, n: Union[float, str]) -> Union[float, str]:
        """
        Get the normalised value of given number
        :param n: float if contains a numeric value else str: `?`
        :return: float: normalised value or return str: `?` as it is
        """
        return n if n == '?' else (n - self.lo) / (self.hi - self.lo + 1e-32)

    def dist(self, n1: Union[float, str], n2: Union[float, str]) -> int:
        """
        Returns distance between the two numbers
        :param n1: float if contains a numeric value else str: `?`
        :param n2: float if contains a numeric value else str: `?`
        :return: int: absolute value of the difference
        """
        if n1 == '?' and n2 == '?':
            return 1
        n1 = self.norm(n1)
        n2 = self.norm(n2)
        if n1 == '?':
            n1 = 1 if n2 < 0.5 else 0
        if n2 == '?':
            n2 = 1 if n1 < 0.5 else 0
        return abs(n1 - n2)

    def delta(self, other):
        e = 1e-32
        return abs(self.mu - other.mu) / ((e + self.sd ** 2 / self.n + other.sd ** 2 / other.n) ** .5)
