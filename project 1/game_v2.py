"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
def binary_search(number: int = 1) -> int:
    """Реализуем алгоритм бинарного поиска для нахождения нашего числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    a=[0]*101 #задаем список с элементами от 0 до 100
    for i in range(len(a)):
        a[i]=i
    first = 0 #левая граница
    last = len(a)-1 #правая граница
    index = -1 #индекс найденного элемента
    count=0
    while (first <= last) and (index == -1): #цикл работающий до того момента как левая граница равна правой и индекс предполагаемого числа не равен индексу искомого
        count+=1
        mid = (first+last)//2 
        if a[mid] == number:
            index = mid
        else:
            if number<a[mid]: 
                last = mid -1 #меняем правую границу
            else:
                first = mid +1 #меняем левую границу
    return count


def score_game(binary_search) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        binary_search ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(binary_search(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_search)
