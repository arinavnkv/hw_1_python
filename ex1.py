N = int(input("Введите значение N: "))

def is_prime(n):
    if n <= 1:
        return False

    i = 2
    while i * i <= n and n % i != 0:
        i += 1
    return (i*i > n)

def sum_of_primes(N):
    prime_sum = 0
    for i in range(2, N + 1):
        if is_prime(i):
            prime_sum += i
    return prime_sum


print(f"Сумма простых чисел в диапазоне от 2 до {N} равна: {sum_of_primes(N)}")
