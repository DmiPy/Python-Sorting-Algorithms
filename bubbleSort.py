def BubbleSort(arr):
    swapped = True                          # swapped ставим на True, чтобы войти в цикл while
    length = len(arr) - 1
    while swapped:                          # пока была хоть одна перестановка в цикле, значит он еще не отсортирован
        swapped = False                     # вначале массива swapped будет False, 
        for i in range(length):             # чтобы позже его изменить на True при хотя бы одной перестановке
            if arr[i] > arr[i+1]:           # если элемент больше следующего, то переставляем их местами
                time_variable = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = time_variable
                swapped = True              # перестановка была, значит меняем swapped на True
        length -= 1                         # после прохода цикла, последний элемент стал максимальным, значит его больше не берем в расчет
    return arr


array = [7, -11, 5, 2, 8, 19, -3]
print(BubbleSort(array))  # [-11, -3, 2, 5, 7, 8, 19]
array = [5, 4, 3, -1, 2, 9]
print(BubbleSort(array))  # [-1, 2, 3, 4, 5, 9]
