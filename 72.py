#72.Write a python program to Generate Fibonacci series using recursion.
def recursive_fib_term(n):
    return n if n <= 1 else recursive_fib_term(n - 1) + recursive_fib_term(n - 2)
fib_sequence = [recursive_fib_term(i) for i in range(7)]
print("Recursive Fibonacci sequence:", fib_sequence)
