"""Ответ на задание 'Шифрованные инструкции', Яндекс Контест ID 110776787"""


import string

SEQ_START_SIGN = '['
SEQ_STOP_SIGN = ']'


def decode(command: str, index: int = 0) -> str:
    """Функция превращает команду в последовательность действий"""
    result: str = ''
    num_for_sum: int = int()
    str_for_sum: str = ''  # Добавил эти строки,т.к. в строке 22 нельзя
    index_from: int = int()  # поместить тдельную анотацию.
    while index != len(command):
        if command[index] in string.digits:
            # num_for_sum должен быть типом int
            # т.к. она участвует в этом качестве в строке 27.
            # но формироваться данная переменная должна по правилам типа str.
            # чтобы "2"+"2" было не "4", а "22"
            # т.к. обрабатываем мы строковое значение, а не какое-то иное.
            # поэтому сначала обрабатываем как str
            # затем приводим к int обратно.
            num_for_sum = int(str(num_for_sum) + command[index])
            index += 1
        elif command[index] in string.ascii_letters:
            result += command[index]
            index += 1
        elif command[index] == SEQ_START_SIGN:
            str_for_sum, index_from = decode(command[index+1:])
            index += index_from + 2
            result += num_for_sum * str_for_sum
            num_for_sum = int()
            str_for_sum = ''
        elif command[index] == SEQ_STOP_SIGN:
            return result, index
    return result


if __name__ == '__main__':
    command = str(input())
    print(decode(command))
