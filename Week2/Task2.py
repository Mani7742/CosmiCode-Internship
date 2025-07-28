# Create a program that generates the first 30 Fibonacci numbers using both iterative and recursive approaches.
def fibonacci_iterative(n):
    fib_seq = []
    a,b = 0,1
    for _ in range(n):
        fib_seq.append(a)
        a,b = b, a+b
    return fib_seq

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

if __name__ == "__main__":
    count = 30
    print("Fibonacci sequence (iterative):", fibonacci_iterative(count))
    print("Fibonacci sequence (recursive):")
    fibonacci_recursive_seq=[fibonacci_recursive(i) for i in range(count)]
    print(fibonacci_recursive_seq)