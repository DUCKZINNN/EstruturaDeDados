import random

class MergeSort:
    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.mergeSort(left_half)
            self.mergeSort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] > right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def main(self):
        arr = [random.randint(1, 1000) for _ in range(2000)]
        print("Vetor original:")
        print(arr)

        self.mergeSort(arr)

        print("\nVetor ordenado de forma decrescente:")
        print(arr[::-1])

if __name__ == "__main__":
    merge_sort = MergeSort()
    merge_sort.main()