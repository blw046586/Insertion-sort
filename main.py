# Global counters
comparisons = 0
swaps = 0

def read_nums():
    """Read numbers from input and return them in a list"""
    return [int(num) for num in input().split()]

def print_nums(nums):
    """Output numbers, separating each item by spaces"""
    print(' '.join([str(n) for n in nums]), end='')

def swap(nums, n, m):
    """Exchange nums[n] and nums[m]"""
    global swaps
    nums[n], nums[m] = nums[m], nums[n]
    swaps += 1

def insertion_sort(numbers):
    """Sort the list numbers using insertion sort"""
    global comparisons
    for i in range(1, len(numbers)):
        j = i
        while j > 0:
            comparisons += 1
            if numbers[j] < numbers[j - 1]:
                swap(numbers, j, j - 1)
                j -= 1
            else:
                break
        print_nums(numbers)
        print()

if __name__ == '__main__':
    # Step 1: Read numbers into a list
    numbers = read_nums()

    # Step 2: Output the numbers list
    print_nums(numbers)
    print('\n')

    # Step 3: Sort the numbers list
    insertion_sort(numbers)
    print()

    # Step 4: Output the number of comparisons and swaps performed
    print(f'comparisons: {comparisons}')
    print(f'swaps: {swaps}')
