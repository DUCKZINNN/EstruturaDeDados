import random

class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def partition(self, low, high):
        i = low - 1
        pivot = self.arr[high]

        for j in range(low, high):
            if self.arr[j] >= pivot:
                i = i + 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def quicksort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quicksort(low, pi - 1)
            self.quicksort(pi + 1, high)

if __name__ == "__main__":
    arr = [random.randint(1, 1000) for _ in range(2000)]
    print("Unsorted array:", arr)

    qs = QuickSort(arr)
    qs.quicksort(0, len(arr) - 1)

    print("Sorted array:", arr)