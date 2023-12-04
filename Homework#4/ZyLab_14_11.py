# Name: Huzaifa Shoeb, ID: 1925670

def selection_sort_descend_trace(numbers_use):
    for i in range(len(numbers_use) - 1):
        max_index = i
        for j in range(i + 1, len(numbers_use)):
            if numbers_use[j] > numbers_use[max_index]:
                max_index = j

        numbers_use[i], numbers_use[max_index] = numbers_use[max_index], numbers_use[i]

        print(' '.join(map(str, numbers_use)), '')


if __name__ == "__main__":
    numbers = list(map(int, input().split()))

    selection_sort_descend_trace(numbers)
