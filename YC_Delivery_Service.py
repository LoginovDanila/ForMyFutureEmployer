"""Ответ на задание 'Служба Доставки', Яндекс Контест ID 109747412"""
 

def min_vehicle(data: str, limit: int) -> int:
  """Функция выдает необходимое количество машин."""
  data_list: list[int] = [int(item) for item in data]
  data_list.sort()
  vehicle: int = 0
  left_pointer: int = 0
  right_pointer: int = len(data) - 1
  while left_pointer <= right_pointer:
    if data_list[left_pointer] + data_list[right_pointer] <= limit:
      left_pointer += 1
    vehicle += 1
    right_pointer -= 1
  return vehicle


if __name__ == '__main__':
  data: str = str(input()).split()
  limit: int = int(input())
  print(min_vehicle(data, limit))
