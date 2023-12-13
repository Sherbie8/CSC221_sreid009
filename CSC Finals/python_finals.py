def mini_maxi_sumi(*n):
    minimum = min(n)
    maximum = max(n)
    total = sum(n)
    return (minimum, maximum, total)

num = (2023, 221, 1214, 1200, 2002)

result = mini_maxi_sumi(*num)

(f"Numbers: {num}")
("Result (min, max, sum):", result)

############################################

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num**2, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

#############################################

def int_and_string(a,b):

  if isinstance(a, (str)):
    b = str(b)
  elif isinstance(a, (int, float)):
    b = float(b)
  else:
    return b

  if isinstance(b, (str)):
    a = str(a)
  elif isinstance(b, (int, float)):
    a = float(a)
  else:
      return a
  return a + b

int_and_string(3,5)
int_and_string("This is a string: ", "Thirty")
int_and_string("'This is a string with integer': ", 123)
