# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    d = 256  # Розмір алфавіту
    q = 101  # Просте число
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for s in range(n - m + 1):
        if p == t:
            match = True
            for i in range(m):
                if pattern[i] != text[s + i]:
                    match = False
                    break
            if match:
                return s
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q
    return -1


import timeit

# Функція для вимірювання часу виконання алгоритму
def measure_time(algorithm, text, pattern):
    stmt = f"{algorithm.__name__}('{text}', '{pattern}')"
    setup = f"from __main__ import {algorithm.__name__}"
    time_taken = timeit.timeit(stmt, setup, number=1000)
    return time_taken

# Задаємо тексти та підрядки для перевірки
text_with_pattern = "This is a sample text with a pattern that exists."
text_without_pattern = "This is a sample text with a pattern that does not exist."
pattern = "pattern"

# Вимірюємо час для кожного алгоритму з реальним підрядком
boyer_moore_time_real = measure_time(boyer_moore, text_with_pattern, pattern)
kmp_time_real = measure_time(kmp, text_with_pattern, pattern)
rabin_karp_time_real = measure_time(rabin_karp, text_with_pattern, pattern)

# Вимірюємо час для кожного алгоритму з вигаданим підрядком
boyer_moore_time_fake = measure_time(boyer_moore, text_without_pattern, pattern)
kmp_time_fake = measure_time(kmp, text_without_pattern, pattern)
rabin_karp_time_fake = measure_time(rabin_karp, text_without_pattern, pattern)

# Виводимо результати
print("З реальним підрядком:")
print("- Алгоритм Боєра-Мура:", boyer_moore_time_real, "секунд")
print("- Алгоритм Кнута-Морріса-Пратта:", kmp_time_real, "секунд")
print("- Алгоритм Рабіна-Карпа:", rabin_karp_time_real, "секунд")
print("\nЗ вигаданим підрядком:")
print("- Алгоритм Боєра-Мура:", boyer_moore_time_fake, "секунд")
print("- Алгоритм Кнута-Морріса-Пратта:", kmp_time_fake, "секунд")
print("- Алгоритм Рабіна-Карпа:", rabin_karp_time_fake, "секунд")
