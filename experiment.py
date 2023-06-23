import re
import copy
from functools import wraps

def func_dict(func):

    d = {}

    while func:

        re_res = re.search('code object (\w+) at', str(func.__code__))

        func_name = re_res.group(1)

        d[func_name] = func

        func = func.__dict__.get('__wrapped__', None)

    return d

 

def n(f, lis):

    d = func_dict(f).items()

    orig_func = list(d)[-1][1]

    funcs = [copy.deepcopy(v) for k, v in d if k in lis]

    for a, b in zip(funcs, funcs[1:]+ [None]):

        if not b:

            b = orig_func

        a.__wrapped__ = b

        a.__closure__[0].cell_contents = b

    return funcs[0] if funcs else orig_func

 

 

def a(some_arg):

    def b(func):

        @wraps(func)

        def a_wrapper(*args, **kwargs):

            print(some_arg)

            return func(*args, **kwargs)

        return a_wrapper

    return b

 

def d(some_arg):

    def e(func):

        @wraps(func)

        def d_wrapper(*args, **kwargs):

            print(some_arg)

            return func(*args, **kwargs)

        return d_wrapper

    return e

 

def g(some_arg):

    def h(func):

        @wraps(func)

        def g_wrapper(*args, **kwargs):

            print(some_arg)

            return func(*args, **kwargs)

        return g_wrapper

    return h

 

@a('lol')

@d('ok')

@g('now')

def main_func(a):

    print(a)

   

f = n(main_func, ['d_wrapper'])

f('wow')

 
