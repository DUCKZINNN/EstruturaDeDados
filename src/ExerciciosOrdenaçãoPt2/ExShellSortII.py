import random

class ShellSort:
    def sort(self, arr):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] < temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

if __name__ == "__main__":
    arr = [random.randint(1, 1000) for _ in range(2000)]
    print("Array antes da ordenação:")
    print(arr)

    sorter = ShellSort()
    sorter.sort(arr)

    print("Array após a ordenação:")
    print(arr)