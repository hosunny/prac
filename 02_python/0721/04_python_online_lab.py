# 정수 0부터 9까지로 이루어진  list를 전달받아, 연속적으로 나타나는 숫자는 하나만 남기고 제거한 리스트를 출력하기
# 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 함

numbers = [1, 1, 3, 3, 0, 1, 1]

result = []
for idx, item in enumerate(numbers):
    if idx == 0:
        result.append(numbers[idx])
    elif result[-1] != item :
        result.append(item)

print(result)
