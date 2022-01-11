

def partition( nums, left, right):
    low = left
    while left < right:
        if nums[left] < nums[right]:
            nums[left], nums[low] = nums[low], nums[left]
            low += 1
        left += 1
    nums[low], nums[right] = nums[right], nums[low]
    return low

def find_kth_element( nums, k):
    if nums:
        pos = partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return find_kth_element(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return find_kth_element(nums[:pos], k)
        else:
            return nums[pos]
        
# an array of number between 0 and 1 (disordered)
nums=[0.4, 0.7, 0.9, 0.2, 0.5, 0.1, 0.3]
print(find_kth_element(nums, len(nums)//2+1))
# quickselect
# https://en.wikipedia.org/wiki/Quickselect


