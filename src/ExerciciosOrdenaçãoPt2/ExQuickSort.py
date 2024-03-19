import random

class QuickSort:
    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

if __name__ == "__main__":
    vetor = [random.randint(0, 1000) for _ in range(2000)]

    print("Vetor antes da ordenação:")
    print(vetor)

    qs = QuickSort()
    qs.quickSort(vetor, 0, len(vetor) - 1)

    print("Vetor após a ordenação:")
    print(vetor)