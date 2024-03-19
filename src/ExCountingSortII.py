import random

class CountingSort:
    def sort(self, arr):
        max_val = max(arr)
        count = [0] * (max_val + 1)
        sorted_arr = [0] * len(arr)

        for num in arr:
            count[num] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for num in arr:
            sorted_arr[count[num] - 1] = num
            count[num] -= 1

        return sorted_arr[::-1]

if __name__ == "__main__":
    arr = [random.randint(0, 1000) for _ in range(2000)]
    print("Original array:", arr)
    
    sorter = CountingSort()
    sorted_arr = sorter.sort(arr)
    print("Sorted array:", sorted_arr)