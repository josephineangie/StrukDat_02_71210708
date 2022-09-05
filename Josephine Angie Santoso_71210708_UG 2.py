from time import time
import timeit


def fibonacci_iteraktif(n):
    a = 0
    b = 1
    for i in range(0, n):
        x = a
        a = b
        b = x + b
    return a


print("*** Catatan Waktu Fibonacci dengan Cara Iteraktif: ***")

for i in range(1, 101):
    start = timeit.default_timer()
    end = timeit.default_timer()
    print("Bilangan fibonacci ", i, "adalah",
          fibonacci_iteraktif(i), "selama", end-start, "detik.")


def fibonacci_rekursif(n):
    for i in range(0, n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)


print("*** Catatan Waktu Fibonacci dengan Cara Rekursif: ***")

for k in range(1, 101):
    start = timeit.default_timer()
    end = timeit.default_timer()
    print("Bilangan fibonacci ", k, "adalah",
          fibonacci_rekursif(k), "selama", end-start, "detik.")
