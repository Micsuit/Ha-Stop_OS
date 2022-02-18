import timeit

def not_not_conv(x): return not not x

def bool_conv(x): return bool(x)

print(f"bool: {timeit.timeit('def bool_conv(x): return bool(x)')} sec\nnot not: {timeit.timeit('def not_not_conv(x): return not not x')} sec")