__author__ = 'wcybxzj'

import roman
knownValues = ( (1226, 'MCCXXVI'),
                (1301, 'MCCCI'),
                (1485, 'MCDLXXXV'),
                (1509, 'MDIX'),
                (1607, 'MDCVII'),
                (1754, 'MDCCLIV'),
                (1832, 'MDCCCXXXII'),
                (1993, 'MCMXCIII'),
                (2074, 'MMLXXIV'),
                (2152, 'MMCLII'),
                (2212, 'MMCCXII'),
                (2343, 'MMCCCXLIII'),
                (2499, 'MMCDXCIX'),
                (2574, 'MMDLXXIV'),
                (2646, 'MMDCXLVI'),
                (2723, 'MMDCCXXIII'),
                (2892, 'MMDCCCXCII'),
                (2975, 'MMCMLXXV'),
                (3051, 'MMMLI') )

def work(flag):
    funcName = 'fromRoman%s' % flag
    func = getattr(roman, funcName)
    for integer, numeral in knownValues:
        result = func(numeral)
        if result == integer:
            pass
        else:
            print 'error'

if __name__ == "__main__":
    import timeit

    start = timeit.default_timer()
    for i in range(20000):
        work('Old')
    elapsed = (timeit.default_timer() - start)
    print elapsed

    start = timeit.default_timer()
    for i in range(20000):
        work('New')
    elapsed = (timeit.default_timer() - start)
    print elapsed

