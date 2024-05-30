"""
# Fibonacci
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(1, 30):
    list_1.append(fib(i))
print(list_1)

# Quick sort

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greate = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greate)

print(quick_sort([14,5,9,6,3,58,7,5,2,7]))

# Merge sort
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_1 = [1,5,6,9,8,7,2,1,55,2,4]
merge_sort(list_1)
print(list_1)

"""
my_l = [4, 234, 45.8, "text", "word", "el", True, None]
print(my_l.__sizeof__())
my_t = (4, 234, 45.8, "text", "word", "el", True, None)
print(my_t.__sizeof__())