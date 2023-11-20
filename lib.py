def count_common_elements(*lists):
    # Используем оператор * для принятия произвольного числа списков
    # Создаем словарь для отслеживания уникальных элементов и их количества
    element_counts = {}

    # Обходим каждый список
    for lst in lists:
        # Обходим каждый элемент в списке
        for element in lst:
            # Инкрементируем счетчик для текущего элемента
            element_counts[element] = element_counts.get(element, 0) + 1

    # Фильтруем элементы, у которых количество больше 1 (т.е., они встречаются в нескольких списках)
    common_elements = {element: count for element, count in element_counts.items() if count > 1}

    return common_elements

# Пример использования
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

result = count_common_elements(list1, list2, list3)
print("Общие элементы в списках:", result)