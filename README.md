1. python B5-9-HW-decorators-n-timing.py - базовый вариант реализации декоратора
Результат выполнения:
- для функции f() - количество прогонов, время выполнения, имя функции после декорирования
- для функции fibo(10000) - вычисление 10000-го члена ряда Фибоначчи - количество прогонов, время выполнения, имя функции после декорирования, номер члена ряда Фибоначчи, длина числа

PS C:\ESNdocs\edX-Py\B5-decorate> python B5-9-HW-decorators-n-timing.py
30 @time_this for: f - Выполнение заняло 0.023099835713704428 секунд
f
50 @time_this for: fibo - Выполнение заняло 0.013159995079040527 секунд
fibo 10000 2090

2. B5-9-HW-1.py - декоратор = метод объекта класса-секундомера Timer()
Результат выполнения такой же:
- для функции f() - количество прогонов, время выполнения, имя функции после декорирования
- для функции fibo(10000) - вычисление 10000-го члена ряда Фибоначчи - количество прогонов, время выполнения, имя функции после декорирования, номер члена ряда Фибоначчи, длина числа

PS C:\ESNdocs\edX-Py\B5-decorate> python B5-9-HW-1.py
10 @time_this for: f - Выполнение заняло 0.0226959228515625 секунд
f
10 @time_this for: fibo - Выполнение заняло 0.013604092597961425 секунд
fibo 10000 2090