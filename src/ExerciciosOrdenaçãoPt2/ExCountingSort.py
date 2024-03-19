import random

class CountingSort:
    def counting_sort(self, arr):
        max_value = max(arr) + 1
        count = [0] * max_value

        for num in arr:
            count[num] += 1

        sorted_arr = []
        for i in range(max_value):
            sorted_arr.extend([i] * count[i])

        return sorted_arr

if __name__ == "__main__":
    vetor = [random.randint(0, 100) for _ in range(2000)]

    counting_sort = CountingSort()
    vetor_ordenado = counting_sort.counting_sort(vetor)

    print(vetor_ordenado)