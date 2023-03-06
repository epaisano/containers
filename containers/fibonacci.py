
###########################################################################
# example fibonacci number code;
# you do not have to modify this code in any way
###########################################################################


def fibs(n):
    '''
    This function computes the first n fibonacci numbers.
    Notice that this function uses O(n) memory.
    '''
    fibs = []
    fibs.append(1)
    if n == 1:
        return fibs
    fibs.append(1)
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def fib_bad(n):
    '''
    This function computes the n-th fibonacci number,
    but it uses O(n) memory to do so,
    which is bad.
    '''
    return fibs(n)[-1]


def fib(n):
    '''
    This function computes the n-th fibonacci number,
    but it consumes only O(1) memory,
    and is optimal.
    '''
    if n < 2:
        return 1
    f0 = 1
    f1 = 1
    for i in range(n - 1):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f2


###########################################################################
# fibonacci number code using generators;
# you will need to implement the functions below
###########################################################################


class Fib:
    '''
    This class represents all the fibonacci numbers,
    but uses O(1) memory to do so.

    >>> list(Fib(5))
    [1, 1, 2, 3, 5]
    '''
    def __init__(self, n=None):
        '''
        n is the number of Fibonacci numbers we will run;
        if n is None, then we will run forever
        '''
        self.n = n

    def __repr__(self):
        if self.n is not None:
            return f'Fib({self.n})'
        else:
            return f'Fib()'

    def __iter__(self):
        '''
        This functions supports for loops and can be converted
        into lists. This makes this function an iterable
        '''
        return FibIter(self.n)


class FibIter:
    '''
    This is the iterator helper class for the Fib class.
    '''
    def __init__(self, n):
        self.n = n
        self.fiba = 0
        self.fibb = 1
        self.i = 0

    def __next__(self):
        '''
        Return the "next" Fibonacci number in our sequence.
        The Fibonacci number corresponding to position self.i
        '''
        if self.n is not None:
            if self.i >= self.n:
                # kinda like a base case
                # must raise this StopIteration
                # or else it will run forever
                raise StopIteration
            elif self.i == 0:
                self.i += 1
                return 1
            else:
                self.result = self.fiba + self.fibb
                self.fiba = self.fibb
                self.fibb = self.result
                self.i += 1
                return self.result
        else:
            if self.i == 0:
                self.i += 1
                return 1
            else:
                self.result = self.fiba + self.fibb
                self.fiba = self.fibb
                self.fibb = self.result
                self.i += 1
                return self.result


def fib_yield(n=None):
    '''
    This function returns a generator that computes the
    first n fibonacci numbers.
    If n is None, then the generator is infinite.
    '''
    if n is not None:
        fiba = 0
        fibb = 1
        for i in range(1, n+1):
            if i == 1:
                yield 1
            else:
                result = fiba + fibb
                fiba = fibb
                fibb = result
                yield result
    else:
        i = 0
        while i:
            i += 1
