from typing import Callable
from functools import wraps


def coroutine(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        gen = fn(*args, **kwargs)
        next(gen)
        return gen
    return wrapper


@coroutine
def foo(successor: Callable = None):
    """
    notice we use yield in both the
    traditional generator sense and
    also in the coroutine sense.
    """
    while True:
        msg = yield  # coroutine feature
        if successor is not None:
            msg = successor.send(msg)
        yield '%s in %s >' % (msg, 'foo')    # generator feature


def main1():
    coro = foo()

    # because a coroutine is a generator
    # we need to advance the returned generator
    # to the first yield within the generator function
    next(coro)

    # the .send() syntax is specific to a coroutine
    # this sends "bar" to the first yield
    # so the msg variable will be assigned that value
    result = coro.send("bar")

    # because our coroutine also yields the msg variable
    # it means we can print that value
    print(result)   # -- bar


@coroutine
def bar(successor: Callable = None):
    while True:
        msg = yield
        if successor is not None:
            msg = successor.send(msg)
        yield '%s in %s >' % (msg, 'bar')


def main():
    fns = [bar, foo, bar, foo, bar, foo]
    # fns = [foo, bar]
    pipeline = None
    for fn in fns:
        pipeline = fn(pipeline)

    msg = pipeline.send('test')
    print(msg)  # beep


if __name__ == '__main__':
    main()

