# Метод 1
# Перебор списка с поиском делителя
# Работает только для упорядоченных исходных данных без пропуска простых чисел

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    if number < 2:  # отсеиваем все что меньше 2
        continue
    is_prime = True  # Предполагаем что число простое
    for divider in primes:
        if number % divider == 0:
            not_primes.append(
                number
            )  # если найден делитель - число не является простым
            is_prime = False
            break
    if is_prime:
        primes.append(number)  # если делитель не найден - число простое

print("Решение перебором делителей")
print("Numbers:", numbers)
print("Prime:", primes)
print("Not prime:", not_primes)

# Метод 2
# Решето Эратосфена
# список может быть любым
numbers = [1, 8, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7]

import math

max_number = max(numbers)  # будем искать простые числа от 2 до max_number
smallest_divider = math.ceil(math.sqrt(max_number))
is_prime_ = [True] * (max_number + 1)  # таблица флагов
for i in range(2, smallest_divider):
    if is_prime_[i]:
        for k in range(0, max_number + 1):
            j = i**2 + i * k  # Вычеркиваем все числа кратные простым
            if j > max_number:
                break
            is_prime_[j] = False

primes = [n for n in numbers if is_prime_[n] and n >= 2]
not_primes = [n for n in numbers if n not in primes and n >= 2]
print("-" * 40)
print("Сито Эратосфена")
print("Numbers:", numbers)
print("Prime:", primes)
print("Not prime:", not_primes)
