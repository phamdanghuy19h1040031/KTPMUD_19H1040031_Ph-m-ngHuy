def is_prime(n):
    if n < 2: return False
    for x in range(2, int(n ** 0.5) + 1):
        if not n % x: return False
    return True


arr = [int(x) for x in input().split()]
print(sum(1 for x in arr if is_prime(x)) >= 2)
