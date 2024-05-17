def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # Якщо елемент не знайдено, повертаємо кількість ітерацій і верхню межу
    if low < len(arr):
        return iterations, arr[low]
    else:
        return iterations, None

# Приклад використання:
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0]
target = 6.0
iterations, upper_bound = binary_search(sorted_array, target)

print("Кількість ітерацій:", iterations)
if upper_bound is not None:
    print("Верхня межа:", upper_bound)
else:
    print("Елемент не знайдено")
