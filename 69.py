#69. Write a python program to Define a function that generates Fibonacci series up to ‘n’.
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series
print("Fibonacci series up to 20:", fibonacci_series(20))

