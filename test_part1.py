import pytest


def is_prime(n):
    if n < 2: return False
    for x in range(2, int(n ** 0.5) + 1):
        if not n % x: return False
    return True


@pytest.mark.parametrize(
    "arr,output",
    [([4, 6, 8, 10], 0),
     ([2, 4, 6, 8], 1),
     ([67, 113, 14, 77], 2)])
def test_prime(arr, output):
    assert sum(1 for x in arr if is_prime(x)) == output