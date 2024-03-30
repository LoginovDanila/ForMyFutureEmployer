"""Код демонстрирует пример исполнения сортировки согласно заданию Яндекс Контеста 'Сортировка по шаблону'"""


def key_sort(q_elements, list_elements, q_keys, list_keys):
    list_elements = [int(item) for item in list_elements]
    list_keys = [int(item) for item in list_keys]
    not_in_key_el = []
    in_key_el = []
    result = ''
    for el in list_elements:
        if el in list_keys:
            continue
        else:
            not_in_key_el.append(el)
    not_in_key_el.sort()
    for el in not_in_key_el:
        list_elements.remove(el)
    for key in list_keys:
        for el in list_elements:
            if el == key:
                in_key_el.append(el)
            else:
                continue
    for el in in_key_el:
        result += f'{el} '
    for el in not_in_key_el:
        result += f'{el} '
    result = result[:len(result)-1]
    return (result)
    

q_elements = int(input())
list_elements = str(input()).split()
q_keys = int(input())
list_keys = str(input()).split()
print(key_sort(q_elements, list_elements, q_keys, list_keys))
