import sys

def fibonacciNoRecursivo(n: int) -> int:
  fib_seq = [0,1]
  if n >= 2:
    for i in range(2,n + 1):
      fib_seq.append(fib_seq[i - 2] + fib_seq[i - 1])
  return fib_seq[n]


if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))