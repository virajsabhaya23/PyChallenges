
def get_prime_factors(N):
    factors = list()
    divisor = 2
    while( divisor <= N):
        if (N%divisor == 0) :
            factors.append(divisor)
            N = N//divisor
        else:
            divisor += 1
    return factors

print(get_prime_factors(23))