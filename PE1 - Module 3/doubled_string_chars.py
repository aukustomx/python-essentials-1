import time
import timeit

def doubled_string(s):
    timeit
    start_time = time.time()
    result = ''
    for i in s:
        result += i * 2
    l = len(result)
    total_time = time.time() - start_time
    print(f'{total_time:f}')
    return l

def doubled_string_conprehension(s):
    start_time = time.time()
    result = "".join(i * 2 for i in s)
    l = len(result)
    total_time = time.time() - start_time
    print(f'{total_time:f}')
    return l
