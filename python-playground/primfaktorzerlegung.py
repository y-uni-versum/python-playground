def primefactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
zahl = int(input('Geben Sie eine Zahl ein: '))
print(f'Die Zerlegung der Zahl {zahl} ergibt, {primefactors(zahl)}')


'''
def is_prime(n):
    if n <= 1:
        return False
        #print('Die zahl ist nicht größer als 1.')
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            #print('Die Zahl ist keine Primzahl.')
    return True
    #print('Die Zahl ist eine Primzahl.')
'''
'''
def count_prime_factors(numbers):
    prime_factors_count = {}
    for num in numbers:
        factors = primefactors(num)
        for factor in factors:
            if factor in prime_factors_count:
                prime_factors_count[factor] += 1
            else:
                prime_factors_count[factor] = 1
    return prime_factors_count

numbers = [12, 15, 18, 21, 24, 27]
prime_factors_count = count_prime_factors(numbers)
print(prime_factors_count)
'''