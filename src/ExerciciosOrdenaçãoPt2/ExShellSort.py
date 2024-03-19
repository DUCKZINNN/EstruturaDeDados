import random

class ShellSort:
    def sort(self, arr):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

if __name__ == "__main__":
    # Create a vector with 2000 positions and fill it randomly
    vector = [random.randint(1, 1000) for _ in range(2000)]

    # Sort the vector using Shell Sort
    shell_sort = ShellSort()
    shell_sort.sort(vector)

    # Print the sorted vector
    print(vector)