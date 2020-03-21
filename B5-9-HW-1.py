# Вам предлагается написать декоратор для подобной логики, который измерял бы скорость работы функций. Как-то так:

# @time_this(num_runs=10)
# def f():
#     for j in range(1000000):
#         pass
# Примечания:

# в данном случае внутри вложенной функции (где-то в декораторе) стоит выводить среднее время выполнения;
# можно либо зафиксировать число запусков, либо передавать как параметр.
# Опционально: вы можете выполнить несколько дополнительных требований и получить за них баллы:

# задание с одной звездочкой: написать декоратор в качестве объекта класса-секундомера;
# задание с двумя звездочками: написать декоратор в качестве объекта класса-секундомера, который можно использовать как контекстный менеджер.
# Кстати, вот наблюдение. В юните B5.7 была задачка на последовательность Фибоначчи. Если увеличить верхнюю границу последовательности, то функцию, написанную в той задачке, можно прогнать для отладки поведения секундомера.

import time
from functools import wraps

# декоратор оценки времени выполнения
# задание с одной звездочкой: написать декоратор в качестве объекта класса-секундомера

class Timer():
    def __init__(self, num_runs=10):
        self.num_runs = num_runs

    def time_this(self, func):
        @wraps(func) # трансляция __name__, __doc__
        def wrapper(param=None):
            avg_time = 0
            for _ in range(self.num_runs):
                t0 = time.time()
                # обернутая функция              
                if param: func_res = func(param)
                else: func_res = func()              
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= self.num_runs
            print(self.num_runs, "@time_this for: {0} - Выполнение заняло {1} секунд".format(func.__name__, avg_time))
            return func_res   
        return wrapper

def fibo(imax):
    '''
    вычисляет imax-й член ряда Фибоначчи
    '''
    fi1 = 1 
    fi2 = 2
    fi3 = fi2 + fi1
    i = 2
    while i < imax:
        fi1 = fi2
        fi2 = fi3
        fi3 = fi2 + fi1
        i += 1 
    return fi3

def f():
    '''
    dummy func: for in range(1000000)
    '''
    for _ in range(1000000):
        pass

if __name__ == "__main__":
    f = Timer(10).time_this(f)
    f()
    print(f.__name__)

    fibo = Timer(10).time_this(fibo)
    i = 10000
    len_of_10000th_fibo = len(str(fibo(i)))
    print(fibo.__name__, i, len_of_10000th_fibo)

