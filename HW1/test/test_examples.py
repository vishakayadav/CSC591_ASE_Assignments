from HW1.src.num import NUM
from HW1.src.sym import SYM
from HW1.src import utils
from HW1.src.utils import rnd, oo, the, rand


def test_the():
    r = oo(the)
    return r


def test_rand():
    num1, num2 = NUM(), NUM()
    utils.seed = the['seed']
    for i in range(1, 11):
        num1.add(rand(0, 1))

    utils.seed = the['seed']
    for i in range(1, 11):
        num2.add(rand(0, 1))

    m1, m2 = rnd(num1.mid(), 10), rnd(num2.mid(), 10)
    return m1 == m2 and .5 == rnd(m1, 1)


def test_sym():
    sym = SYM()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == rnd(sym.div())


def test_num():
    num = NUM()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    return 11 / 7 == num.mid() and 0.787 == rnd(num.div())
