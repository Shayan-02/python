# fib with def:

def fibonacci(n):
  if n == 1 or n == 2:
    return 1

  return fibonacci(n-1) + fibonacci(n-2)

num_terms = int(input("Enter the number of terms to generate: "))

for i in range(1, num_terms+1):
  print(fibonacci(i), end=" ")